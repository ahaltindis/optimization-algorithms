Simulated Annealing
==================

This is the implementation of Simulated Annealing optimization algorithm.

####Dependencies
  * Python 3
  * Numpy


####Usage
  ```
  simulated_ann.py -k <kA> -i <maxIteration> --x1 <x1> --x2 <x2>
  ```

####Output
  This will execute the algorithm with given parameters for 30 times and then
  calculates its mean and std, prints all with input parameters.


###Example
  
  If you execute following command:
  ```
  simulated_ann.py -k 0.1 -i 100000 --x1 0 --x2 2
  ```

  It will print this output:
  ```
  ========================================
  x1: 0  x2: 2  kA: 0.1  maxI: 100000
  ---------------------------
  mean: 0.000146646576821
  std: 0.000126314166481
  ```

