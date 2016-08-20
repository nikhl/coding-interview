### Binary Search

Binary search comes under ***Divide and conquer*** design paradigm. This implementation uses iterative approach by using **start** and **end** values. At beginning, **start** and **end** are initialized to **0** and **len(array)-1** respectively.

In each iteration we compare the **key** to the mid element of the given array. Based on the comparison we divide the problem into half the size of the original problem by adjusting the **start** and **end** values. Thus in the worst case, the number of iterations will be ***log(n)*** and in each iteration the work done is constant.

* Time complexity is **theta(log(n))**
* Space complexity is **constant**