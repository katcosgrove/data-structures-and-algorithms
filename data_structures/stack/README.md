# Data Structures Practice
## Stack

* Create a Class for a Stack which creates an empty Stack when instantiated
* This class should be aware of a default None value assigned to top when the isntance is created
* This class should be aware of the len of the stack, which represents the count of Nodes in the stack at any time
* This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the stack for each value in the iterable
* Define any further magic methods such as len and str to support user functionality and informative responses
* Define a method called push which takes any value as an argument and adds that value to the top of the stack with an O(1) Time performance
* Define a method called pop which takes no arguments and removes / returns the Node at the top of the stack
* Define a method called peek which takes no arguments and returns the Node at the top of the stack