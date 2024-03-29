# Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list

# You are given the example Linked List Node class:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

# Solution:
def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
    return previous

# Testing Solution

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a, b, c, d with values 1, 2, 3, 4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse(a)
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)