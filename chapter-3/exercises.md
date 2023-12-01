# Chapter 3 Exercises

3.1 Suppose I provide a call stack like this:

![stack image](/chapter-3/stack.png)

What information can you extract based solely on this call stack?

`Examining this call stack, it reveals that the initial function called was "greet," involving a variable named "name" with the value "maggie." Shortly after, the "greet" function invoked another function, "greet2," which retained the variable "name" and its value "maggie." At the moment when this call stack was recorded, the execution of the "greet2" function had not been completed.`

3.2 Imagine you accidentally write a recursive function that keeps running infinitely. As you've seen, your computer allocates memory on the stack for each function call. What happens to the stack when the recursive function keeps running indefinitely?

`If a recursive function runs infinitely, it will keep adding calls to the call stack until the stack reaches its limit, resulting in a stack overflow. This typically leads to an error or program failure.`
