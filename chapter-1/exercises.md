# Chapter 1 Exercises

1.1 Suppose you have a list with 128 names and you are performing a binary search. What would be the maximum number of steps you would take to find the desired name?

`The maximum number of steps in a binary search would be 7. This is because (2^7 = 128), and 7 is the number of times you can divide 128 in half until you reach 1.`

1.2 Suppose you double the size of the list. What would be the maximum number of steps now?

`If you double the size of the list, the maximum number of steps in a binary search would be 8, as (2^8 = 256).`

1.3 You have a name and want to find the phone number for that name in a phone book.

`O(log n)`

1.4 You have a phone number and want to find its owner in a phone book. (Hint: you should search through the entire phone book!)

`O(n)`

1.5 You want to read the number of each person in the phone book.

`O(n)`

1.6 You want to read the numbers only of the names that start with A. (This is tricky! This algorithm involves concepts that will be covered more deeply in Chapter 4. Read the answer - you'll be surprised!)

`O(n)`
