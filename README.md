# Comparing search algorithms for efficiency

## The algorithms
3 search algorithms were compared in this study.
- Linear search
- Binary search
- Binary search, recursive implementation

## The measurements
The algorithms time efficiency were compared against increasingly larger datasets. The datapoints are measured in seconds.

## The results
The results indicate that the linear search algorithm demands increasingly larger time in a linear fashion. After 10 to the 10th power of volume, measurements were stopped for this algorithm, since it became very time consuming, and at the same time, the results are obvious.

The binary search algorithms implementations did not need any significant time, even up until 10 to the 18th power of volume, where the Python collection object gave up (length upper limit).

![An image of the results](chart1.png?raw=true "Results")

## Further research suggested
Even though the binary search did not consume any significant time at 10 to the 18th power volume, maybe with a special datatype library, it would be possible to draw an expected logarithmic chart with the data. Another solution could be a less performant machine or virtual machine as a running environment.


## Description of files in this project
data.txt contains the measurements in csv format.

- First column: the number of records to be searched in
- Second column: linear search duration measurement result (in seconds)
- Third column: binary search duration measurement result (in seconds)
- Fourth column: recursive binary search duration measurement result (in seconds)
