class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head
    self.length = 1
  
  def append(self, value):
    newNode = Node(value)
    newNode.prev = self.tail
    self.tail.next = newNode
    self.tail = newNode
    self.length += 1
    return self
  
  def prepend(self, value):
    newNode = Node(value)
    self.head.prev = newNode
    newNode.next = self.head
    self.head = newNode
    self.length += 1
    return self

  def _print(self):
    print(f"Head: {self.head.value}")
    currentNode = self.head
    while currentNode.next:
      print(currentNode.value)
      currentNode = currentNode.next
    print(currentNode.value)
    print(f"Tail: {self.tail.value}")


list = LinkedList(5)
list.append(2)
list.prepend(8)
list._print()
