
![Selection sort](https://github.com/nikhl/coding-interview/blob/master/python/sorting/selection_sort/README.png?raw=true)


<!---
From http://mathurl.com/jl6yqld

##### BEGIN
\textbf{Selection sort}
\\

Selection sort is the most intuitive sorting algorithm. Given an array of size \textbf{n}, in the first step, we iterate through the whole array finding the minimum element and moving it to the first place\textbf{(index 0)} in the array. In the second step, we iterate through last (n-1) \textbf{(from index 1 to n)} elements of array finding the next minimum and move it to the second place\textbf{(index 1)} position in the array. In general, in \textbf{kth} iteration, we iterate through last all (n-k)\textbf{(from index k to n)} elements finding the minimum and moving it to the kth\textbf{(index k)} position in the array.
\\

In worst case, the first iteration takes \textbf{n} steps, the second iteration take \textbf{n-1} steps and kth iteration takes \textbf{n-k} steps forming arithmetic sequence which can be expressed as 

\[n + (n-1) + (n-2) + (n-k) + 3 + 2 + 1 = \frac{n(n-1)}{2} = n^{2}\]
\\

So, Time complexity is 

\[\theta(n^{2})\]
\\

Space complexity is constant as we are doing the sorting inplace with no extra space

\[\theta(1)\]
##### END

-->
