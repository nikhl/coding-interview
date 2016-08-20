
![nth power of x](https://github.com/nikhl/coding-interview/blob/master/python/pow_x_n/README.png?raw=true)


<!---
From http://mathurl.com/jld6kgc

##### BEGIN
\textbf{nth\_power of a number}
\\

To calculate the \textbf{n}th power of a number, the naive way is to multiply the number itself \textbf{n} number of times. We can do better using \textbf{Divide and conquer} design paradigm.
\\

To calculate the \textbf{n}th power, we first compute \textbf{(n/2)}th power and multiply with itself. This works in case of \textbf{n} being even numbers. In case of \textbf{n} being odd number, we compute \textbf{(n-1)/2}th power recursively and multiply it by itself and also with \textbf{x}
\\

\textbf{Time complexity is } \[\theta(log(n))\]
\\

\textbf{Space complexity is} \[\theta(log(n))\]
##### END

-->
