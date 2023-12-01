# Chapter 2 Exercises

2.1 Suppose you are creating an application to track your finances. Every day, you will record everything you spent and where you spent it. At the end of the month, you will need to review your expenses and summarize how much you spent. Therefore, you will have a lot of inserts and few reads. Should you use an array or a list to implement this application?

`As I don't know exactly how many expenses I will have, it will be more efficient to use a linked list due to its efficiency in terms of insertion.`

2.2 Suppose you are creating an application to take customer orders in a restaurant. Your application needs a list of orders. Waiters add orders to this list, and chefs remove orders from the list. It operates like a queue. Waiters place orders at the end, and chefs remove orders from the beginning to cook them. Would you use an array or a linked list to implement this list? (Hint: linked lists are good for insertions/deletions, and arrays are good for random access. What to do in this case?)

`To implement this list of orders in a restaurant, I would choose to use a linked list due to its efficiency in terms of insertion and removal, especially when orders are added and removed in a sequential order, like a queue.`

2.3 Let's analyze an experiment. Imagine that Facebook maintains a list of users. When someone tries to access Facebook, a search is performed based on the username. If the person's name is in the list, they can proceed with access. People access Facebook very frequently, so there are numerous searches in this list. Assume that Facebook uses binary search to look for a name in the list. Binary search requires random access - you need to be able to access the middle of the list of names instantly. Knowing this, would you implement this list as an array or a linked list?

`For random access using binary search, the best choice is an array.`

2.4 People also sign up for Facebook very frequently. Suppose you decide to use an array to store the list of users. What are the disadvantages of an array regarding insertions? In particular, imagine you are using binary search to look up logins. What happens when you add new users to an array?

`In an array, adding items to the end of the list can be costly because either you need to know the maximum number of users in advance or you have to move all the new users to a new memory address. Regarding binary search, it expects the list to be sorted, so you would always need to maintain the array's sorting for the search to be efficient.`

2.5 In fact, Facebook doesn't use either arrays or linked lists to store information. Let's consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot points to a list containing names starting with A, the second to a list with names starting with B, and so on. Suppose Adit B signs up for Facebook, and you want to add him to the list. You go to slot 1 of the array, then to the linked list in slot 1, and add Adit B at the end. Now, suppose you want to look up Zakhir H. You go to slot 26. Then, you search through the list until you find Zakhir H. Compare this hybrid structure with arrays and linked lists. Is it faster or slower for insertions and deletions in this case? You don't need to answer by providing the runtime in Big(O), just say if the new data structure is faster or slower than arrays and linked lists.

`A hybrid data structure can be more efficient for insertion and deletion operations compared to pure arrays or linked lists, especially in situations where data can be grouped or organized in a way that facilitates access through specific slots.`
