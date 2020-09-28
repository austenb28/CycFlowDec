from CycFlowDec import CycFlowDec
import numpy as np
import matplotlib.pyplot as plt

F = np.zeros([3,3])
F[1,0] = 40
F[2,0] = 4
F[0,1] = 38
F[2,1] = 5
F[0,2] = 6
F[1,2] = 3

n_points = 10
init_steps = 20
step_add = 10
run_post = 2

myCycFlowDec = CycFlowDec(F,0,0)
myCycFlowDec.run(init_steps-run_post,run_post)
steps = [init_steps]
MREs = [myCycFlowDec.calc_MRE(0)]

j = 1
while j < n_points:
	myCycFlowDec.run(step_add-run_post,run_post)
	steps.append(steps[-1] + step_add)
	MREs.append(myCycFlowDec.calc_MRE(0))
	j += 1

print('{:>11s} {:>6s}'.format(
	'Cycle',
	'Flow'
))
for cycle in myCycFlowDec.cycles.keys():
	print('{:>11s} {:>6.2f}'.format(
		str(cycle),
		myCycFlowDec.cycles[cycle]
	))

plt.xlabel('Steps')
plt.ylabel('MRE')
plt.plot(steps,MREs,'bo')
plt.yscale('log')
plt.show()
