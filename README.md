# CycFlowDec
Cyclic Flow Decomposition Module

# Description
Takes a flow matrix representing a closed, steady flow network and determines the cyclic flow decomposition according to cycles defined by Min-Ping Qian's decycling algorithm [1]. The algorithm here accomplishes decycling by percolating the network with walks starting from an arbitrary node, and then logging the simple cycles encountered by those walks. More information on the percolating algorithm can be found in reference [TBD].

# Requirements
* Python3
* NumPy library

# Installation
Download CycFlowDec.py and place it in your `$PYTHONPATH`.  On a Unix system, this can be accomplished by the following:

`mkdir ~/python_modules`

Place `CycFlowDec.py` in `~/python_modules`. Update your `~/.bashrc` to include 

`export PYTHONPATH="~/python_modules":$PYTHONPATH`.

# Usage
1. Include `from CycFlowDec import CycFlowDec` in your Python script.  

2. Instantiate the CycFlowDec class with `myCycFlowDec = CycFlowDec(F,state,tol)`.

`F`: NumPy (*N* x *N*) array. Flow matrix of the network to decycle, where *N* is the number of network nodes.  *F*[*m*,*n*] should correspond to the flow from node *n* to node *m*.

`state`: Integer. The arbitrary starting node for percolation.

`tol`: Float. The minimum contribution tolerance for walks to further percolate the network. Should be on the range \[0,1\]. For small networks (*N* ~< 6) `tol=0` should be fine.  For larger networks, `tol` can be be increased to accelerate percolation at the cost of maximum achievable accuracy.

3. Execute `myCycFlowDec.run(burnin,nstep)`

**Description**

Runs cyclic flow decomposition on `F`.

**Parameters**

`burnin`: Integer. Number of steps to equilibrate percolation.
`nstep`: Integer. Number of steps to log cycles. The lower the better (e.g. 1. More may be required if burnin is too small. If the network only contains even cycles, then 2).

4. Execute `myCycFlowDec.calc_MRE(tol)`

**Description**

Returns the mean relative error (MRE) of the decycled network flows with respect to the original network flows. Scales cycles weights to flow values with `CycFlowDec.scale_cycles()` if it hadn't been called previously.

**Parameters**

`tol`: Float. Minimum flow tolerance for edges to contribute to the MRE calculation.

# References
[1] Minping, Qian, and Qian Min. "Circulation for recurrent Markov chains." Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 59.2 (1982): 203-210.
