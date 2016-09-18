import unittest
from datetime import time


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.head = node
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = node

    def pop_head(self):
        if self.head is not None:
            head_to_pop = self.head
            self.head = self.head.next_node
            return head_to_pop
        else:
            return None

    def size(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next_node
        return size


# Animal Definitions


class Animal:
    def __init__(self, name):
        self.time_admitted = time.clock()
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)


class AnimalShelter(LinkedList):
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, animal):
        animal_node = Node(animal)
        self.linked_list.insert(animal_node)

    def dequeue_any(self):
        return super(AnimalShelter, self).pop_head()

    def dequeue_cat(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if type(current_node) is Cat:
                previous_node.next_node = current_node.next_node
                return current_node.data
        return None

    def dequeue_dog(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if type(current_node) is Dog:
                previous_node.next_node = current_node.next_node
                return current_node.data
        return None


class Tests(unittest.TestCase):
    def enqueue(self):
        animal_shelter = AnimalShelter()
        animal_shelter.enqueue(Cat("Fluffy"))
        animal_shelter.enqueue(Dog("Sparky"))
        animal_shelter.enqueue(Cat("Sneezy"))
        self.assertEquals(
            animal_shelter.size(), 3, "Amount of animals in queue should be 3"
        )
