# Solution

the `data` variable is initialized with a list of 1 million random integers in the range of 1 to 100. The `parts` variable is set to 4, indicating that the dataset should be divided into 4 equal parts. The `chunk_size` variable is then computed by dividing the length of the dataset by the number of parts.

A `multiprocessing.Pool` object is created with the `processes` argument set to `parts`, which creates 4 separate processes. A `results` list is created to store the results from each process.

A `for` loop is used to divide the dataset into 4 equal parts and submit each part to a separate process for computation. The `compute_sum()` function is applied to each part using the `apply_async()` method of the `Pool` object, which returns a `multiprocessing.pool.AsyncResult` object representing the result of the computation. Each `AsyncResult` object is appended to the `results` list.

After all the processes have been submitted, the `close()` and `join()` methods of the `Pool` object are called to wait for all the processes to complete.

The final result is computed by summing up the results from each process using a generator expression and the built-in `sum()` function. The final result is printed to the console.