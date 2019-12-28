
class SNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return self.value

class SList:
  def __init__(self):
    self.head = None
    self.count = 0

  def add_to_front(self, val):
    current_head = self.head
    new_node = SNode(val)
    new_node.next = current_head
    self.head = new_node
    self.count += 1
    return self
  
  def add_to_back(self, val):
    if self.head is None:
      self.add_to_front(val)
      return self
    new_node = SNode(val)
    runner = self.head
    while(runner.next is not None):
      runner = runner.next
    runner.next = new_node
    self.count += 1
    return self

  def insert_at(self, val, n):
    if n < 0: 
      raise Exception('cannot insert before the first element!')
    elif n > self.count:
      raise Exception('cannot insert one or more positions after the last element!')
    if n == 0:
      self.add_to_front(val)
    elif n == self.count:
      self.add_to_back(val)
    else:
      runner = self.head
      for _ in range(n-1):
        runner = runner.next
      new_node = SNode(val)
      new_node.next, runner.next = runner.next, new_node
    return self
      
  def remove_from_front(self):
    if self.head is None:
      return None
    current_node = self.head
    second_node = self.head.next
    if second_node is None:
      self.head = None
    else:
      self.head = second_node
    self.count -= 1
    return current_node

  def remove_from_back(self):
    if self.head is None:
      return None
    previous_node = None
    current_node = self.head
    second_node = self.head.next
    while second_node is not None:
      previous_node, current_node, second_node = current_node, second_node, second_node.next
    else:
      if previous_node is None:
        self.head = None
      else:
        previous_node.next = None
      self.count -= 1
      return current_node

  def remove_val(self, val):
    if self.head is None:
      return None
    previous_node = None
    current_node = self.head
    while current_node is not None:
      if current_node.value is val:
        if previous_node is None:
          self.head = current_node.next
        else:
          previous_node.next = current_node.next
        self.count -= 1
        return current_node
      previous_node, current_node = current_node, current_node.next
    return None

  def __str__(self):
    values = []
    runner = self.head
    while(runner is not None):
      values.append(runner.value)
      runner = runner.next
    return ' --> '.join(values)

if __name__ == '__main__':
  my_list = SList()	# create a new instance of a list
  n = my_list.add_to_front('are').add_to_front('Linked lists').add_to_back('fun!').insert_at('boring', 1)
  print(my_list)
  n = my_list.add_to_front('are').add_to_front('Linked lists').add_to_back('fun!').remove_val('boring')
  print(my_list)
  while n is not None:
    print('removed', n)
    n = my_list.remove_from_back()
