\#\#\# nth\_power of a number

To calculate the nth power of a number, the naive way is to multiply the number itself \*\*n\*\* number of times. We can do better using \*\*\*Divide and conquer\*\*\* design paradigm.

To calculate the \*\*n\*\*th power, we first compute \*\*(n/2)\*\* power and multiply with itself. This works in case of n being even numbers. In case of \*\*n\*\* being odd number, we compute \*\*(n-1)/2\*\*th power recursively and multiply it by itself and also \*\*x\*\*

\* Time complexity is \*\*(log(n))\*\* \* Space complexity is \*\*constant\*\*