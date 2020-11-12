from CycFlowDec import CycFlowDec
import numpy as np
import matplotlib.pyplot as plt

F = np.zeros([7,7])
F[1,0] = 4
F[6,0] = 1
F[0,1] = 3
F[6,1] = 2
F[3,2] = 1
F[6,2] = 5
F[2,3] = 1
F[6,3] = 2
F[5,4] = 6
F[6,4] = 3
F[4,5] = 4
F[6,5] = 3
F[0,6] = 2
F[1,6] = 1
F[2,6] = 5
F[3,6] = 2
F[4,6] = 5
F[5,6] = 1

n_points = 10
init_steps = 10
step_add = 10
run_post = 2

myCycFlowDec = CycFlowDec(F,6,0)
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
