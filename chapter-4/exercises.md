# Chapter 4 Exercises

4.1 Write code for the *sum* function, previous view

[View source code](/chapter-4/sum_recursive.py)

4.2 Write a recursive function that counts the number of items in a list

[View source code](/chapter-4/count_fat.py)

4.3 Find the highest value in a list

[View source code](/chapter-4/get_highest_recursive.py)

4.4 Do you remember the binary search from Chapter 1? It is also a divide-and-conquer algorithm. Can you determine the base case and the recursive case for binary search?

```text
The base case occurs when the search range no longer contains elements, i.e., when low is greater than high. At this point, the function returns None, indicating that the element was not found.

In the recursive case, we divide the search range in half. If the element in the middle is equal to the target element, the search is successful, and the function returns the position of the element. If the middle element is greater, the search continues in the lower half; if it is smaller, the search continues in the upper half. This process repeats recursively until the base case is reached.
```

How long would it take, in Big O notation, to complete each of these operations:

4.5 Print the value of each element in an array

`O(n)`

4.6 Duplicate the value of each element in an array

`O(n)`

4.7 Duplicate the value of only the first element of the array

`O(1)`

4.8 Create a multiplication table with all the elements of the array. Thus, if your array is [2,3,7,8,10], you will first multiply each element by 2. Then, you will multiply each element by 3, and then by 7, and so on.

`O(n²)`
