## Specification

* Create a new branch in your data-structures-and-algorithms repository called linked-list. If you call it anything else, you will get ZERO CREDIT with NO COMMENTS

* Create two files called node.py and linked_list.py in your linked_list directory
* Create a Class for a Node which is aware of the value as val and next as _next
* Ensure that you have a __str__ method defined to return the value of the node when printed
* Create a Class for a LinkedList which creates an empty Linked List when instantiated.

    - This class should be aware of a default None value assigned to head when the list is created.
    - his class should be aware of the len of the list, which represents the count of Nodes in the list at any time
    - This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the list for each value in the iterable.

* Define any further magic methods such as len and str to support user functionality and informative responses.
* Define a method called insert which takes any value as an argument and adds that value to the head of the list with an O(1) Time performance.
* Define a method called find which takes any value as an argument and returns True or False depending on whether that value exists as a Node value within the list.
* At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.

* Every bit of functionality that you have should be tested and documented.