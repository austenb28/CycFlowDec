from CycFlowDec import CycFlowDec
import numpy as np
import matplotlib.pyplot as plt
import pickle

with open('F.pickle','rb') as myfile:
	F = pickle.load(myfile)

n_points = 10
init_steps = 300
step_add = 300
run_post = 4

myCycFlowDec = CycFlowDec(F,50,1E-7)
myCycFlowDec.run(init_steps-run_post,run_post)
steps = [init_steps]
MREs = [myCycFlowDec.calc_MRE(1E-1)]

j = 1
while j < n_points:
	myCycFlowDec.run(step_add-run_post,run_post)
	steps.append(steps[-1] + step_add)
	print(steps[-1])
	MREs.append(myCycFlowDec.calc_MRE(1E-1))
	j += 1

print('{:>11s} {:>6s}'.format(
	'Cycle',
	'Flow'
))
for cycle in myCycFlowDec.cycles.keys():
	if myCycFlowDec.cycles[cycle] > 0.009:
		print('{:>11s} {:>6.2f}'.format(
			str(cycle),
			myCycFlowDec.cycles[cycle]
		))

plt.xlabel('Steps')
plt.ylabel('MRE')
plt.plot(steps,MREs,'bo')
plt.yscale('log')
plt.show()
