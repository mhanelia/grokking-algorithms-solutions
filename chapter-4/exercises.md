# Chapter 4 Exercises

4.1 Escreva um código para a função *soma*, vista anteriormente

[View source code](/chapter-4/sum_fat.py)

4.2 Escreva uma função recursiva que conte o número de itens em uma lista

[View source code](/chapter-4/count_fat.py)

4.3 Encontre o valor mais alto em uma lista

[View source code](/chapter-4/get_highest_recursive.py)

4.4 Do you remember the binary search from Chapter 1? It is also a divide-and-conquer algorithm. Can you determine the base case and the recursive case for binary search?

`
The base case occurs when the search range no longer contains elements, i.e., when low is greater than high. At this point, the function returns None, indicating that the element was not found.

In the recursive case, we divide the search range in half. If the element in the middle is equal to the target element, the search is successful, and the function returns the position of the element. If the middle element is greater, the search continues in the lower half; if it is smaller, the search continues in the upper half. This process repeats recursively until the base case is reached.
`
