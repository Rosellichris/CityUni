# CS 11A PE02 - Binary Search
# Name: Chris Rosselli


def binary_search(my_list, target):

    # Starting index of the list
    low = 0

    # Ending index of the list
    high = len(my_list) - 1

    # Continue searching while there are elements left
    while low <= high:

        # Find the middle index
        mid = (low + high) // 2

        # Check if middle value is the target
        if my_list[mid] == target:
            return mid

        # If target is larger, search right side
        elif my_list[mid] < target:
            low = mid + 1

        # If target is smaller, search left side
        else:
            high = mid - 1

    # Target was not found
    return -1


# Testing binary search
my_list = [2, 5, 8, 12, 16, 23, 38, 45]

print("Original list:")
print(my_list)

print("\nSearching for 16:")
print("Position:", binary_search(my_list, 16))


# Add additional values
my_list.append(50)
my_list.append(60)

# Keep list sorted
my_list.sort()

print("\nUpdated list:")
print(my_list)

print("\nSearching for 60:")
print("Position:", binary_search(my_list, 60))





##################################################
# Task #2 - Singly Linked List
##################################################

# Create a Node class
class Node:

    # Initialize a node with data
    def __init__(self, data):
        self.data = data      # Store the value
        self.next = None      # Store the next node reference


# Create a Linked List class
class LinkedList:

    # Initialize an empty linked list
    def __init__(self):
        self.head = None      # Head points to the first node


    # Add a new node to the end of the list
    def append(self, data):

        # Create a new node
        new_node = Node(data)

        # If the list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            return

        # Start at the first node
        current = self.head

        # Move through the list until the last node
        while current.next:
            current = current.next

        # Connect the last node to the new node
        current.next = new_node


    # Display all values in the linked list
    def display(self):

        # Start at the head node
        current = self.head

        # Continue until there are no more nodes
        while current:
            print(current.data)
            current = current.next



# Create a linked list object
linked_list = LinkedList()

# Add values to the linked list
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)


# Display the linked list
print("\nLinked List:")
linked_list.display()