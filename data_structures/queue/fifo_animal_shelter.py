from node import Node


class Dog:
    """Create a dog class."""
    def __init__(self):
        self.species = 'dog'
        self.name = 'Fido'

    def __str___(self):
        """Return species."""
        return self.species


class Cat:
    """Create a cat class."""
    def __init__(self):
        self.species = 'cat'
        self. name = 'Fluffy'

    def __str___(self):
        """Return species."""
        return self.species


class Iguana:
    """Create a cat class."""
    def __init__(self):
        self.species = 'iguana'
        self. name = 'Hank'

    def __str___(self):
        """Return species."""
        return self.species


class AnimalShelter:
    """Create a FIFO AnimalShelter class"""
    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._size = 0

        for item in iter:
            self.enqueue(item)

    def __repr__(self):
        """Returns the animal at the front of the queue."""
        return f'The animal in the shelter longest is: {self.front.val}'

    def enqueue(self, animal=None):
        """Insert an animal to the back of the queue"""
        node = Node(animal.species)

        if animal.species != 'dog' and animal.species != 'cat':
            raise ValueError('Sorry, we only take dogs or cats!')

        if self.front is None:
            self.front = self.back = node
        self.back._next = node
        self.back = node
        self._size += 1
        return None

    def dequeue(self, pref=None):
        """Remoe the next animal in queue according to preference."""
        if self._size == 0:
            raise IndexError('All of the animals were adopted!')

        if type(pref) is not str:
            raise TypeError('That isn\'t an animal! Please enter dog or cat.')

        if pref is None or self.front.val == pref:
            adopted = self.front
            self.front = self.front._next
            self._size -= 1
            return adopted.val

        if pref != 'dog' and pref != 'cat':
            raise ValueError('Sorry, we only have dogs or cats!')

        current = self.front._next
        temp = self.front

        while current:
            if current.val == pref:
                adopted = current
                temp._next = current._next
                self._size -= 1
                return adopted.val

            current = current._next
            temp = temp._next
