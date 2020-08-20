# CycFlowDec
Cyclic Flow Decomposition Python Module

# Description
Takes a flow matrix representing a closed, steady flow network and determines the simple cycle flow decomposition consistent with Min-Ping Qian's decycling algorithm [1]. The algorithm here accomplishes decycling by percolating the network with starting from an arbitrary node, and then logging the simple cycles encountered. More information on the percolating algorithm can be found in reference [TBD].

# Requirements
* Python3
* NumPy library
* MatPlotLib library (for `example.py` only)

# Installation
Download CycFlowDec.py and place it in your `$PYTHONPATH`.  On a Unix system, this can be accomplished by the following:

`mkdir ~/python_modules`

Place `CycFlowDec.py` in `~/python_modules`. Update your `~/.bashrc` to include 

`export PYTHONPATH="~/python_modules":$PYTHONPATH`.

# Usage
Include `from CycFlowDec import CycFlowDec` in your Python script. See the definitions section and `example.py` for specific usage hints.

# Definitions
## `CycFlowDec(F,state,tol)`
Constructor of the CycFlowDec class.

`F`: NumPy (*N* x *N*) array. Flow matrix of the network to decycle, where *N* is the number of network nodes.  The entry *F[m,n]* corresponds to the flow from node *n* to node *m*.

`state`: Integer. The arbitrary starting node for percolation.

`tol`: Float. The minimum contribution tolerance to extend percolation in the network. Should be on the range \[0,1\]. For small networks (*N* < ~6) `tol=0` should be fine.  For larger networks, `tol` can be be increased to accelerate percolation at the cost of maximum achievable accuracy.

## `CycFlowDec.run(burnin,nstep)`
Class method for running percolating cyclic flow decomposition on `F`. Stores cycles with weights in `CycFlowDec.cycles`.

`burnin`: Integer. Number of steps to equilibrate percolation.

`nstep`: Integer. Number of steps to log cycles. 2 is usually optimal, unless `burnin` is too small.

## `CycFlowDec.scale_cycles()`
Scales cycle weights to flow values using the total network flow.

## `CycFlowDec.calc_MRE(tol)`
Returns the mean relative error (MRE) of the decycled network flows with respect to the original network flows. Scales cycles weights to flow values with `CycFlowDec.scale_cycles()` if it hadn't been called previously.

`tol`: Float. Minimum flow tolerance for edges to contribute to the MRE calculation.

# Example
See `example.py`. Requires `matplotlib`.

# References
[1] Minping, Qian, and Qian Min. "Circulation for recurrent Markov chains." Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 59.2 (1982): 203-210.
