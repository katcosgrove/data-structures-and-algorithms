# Data Structures Practice
## Queue

* Create a Class for a Queue which creates an empty Queue when instantiated
* This class should be aware of a default None value assigned to front when the isntance is created
* This class should be aware of a default None value assigned to back when the isntance is created
* This class should be aware of the len of the queue, which represents the count of Nodes in the queue at any time
* This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the queue for each value in the iterable
* Define any further magic methods such as len and str to support user functionality and informative responses
* Define a method called enqueue which takes any value as an argument and adds that value to the back of the queue with an O(1) Time performance
* Define a method called dequeue which takes no arguments and removes / returns the Node at the front of the queue
* Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
* enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
* dequeue(pref): returns either a dog or a cat. If pref, a string, is ‘cat’ return the longest-waiting cat. If pref is ‘dog’, return the longest-waiting dog. For anything else, return either a cat or a dog.

## Solution
![Whiteboarding](https://github.com/katcosgrove/data-structures-and-algorithms/assets/queue-dequeue.jpg)