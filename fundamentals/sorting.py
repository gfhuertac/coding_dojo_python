
def bubble_sort(to_sort):
  final_index = len(to_sort)
  while final_index > 0:
    for i in range(final_index - 1):
      if to_sort[i]>to_sort[i+1]:
        to_sort[i], to_sort[i+1] = to_sort[i+1], to_sort[i]
    final_index -= 1
  return to_sort

def selection_sort(to_sort):
  start = 0
  length = len(to_sort)
  while start < length:
    pos = start
    min = to_sort[pos]
    for i in range(start+1, length):
      if to_sort[i] < to_sort[pos]:
        pos = i
        min = to_sort[pos]
    if pos != start:
      to_sort[start], to_sort[pos] = to_sort[pos], to_sort[start]
    start += 1
  return to_sort

def insertion_sort(to_sort):
  length = len(to_sort)
  for i in range(1, length):
    current = to_sort[i]
    j = i
    while j > -1 and current < to_sort[j]:
      to_sort[j+1] = to_sort[j]
      j -= 1
    to_sort[j] = current
  return to_sort

if __name__ == '__main__':
  import random
  l = []
  for i in range(20):
    l.append(random.randint(1,100))
  print(l)
  print(bubble_sort(l))
  print(selection_sort(l))
  print(insertion_sort(l))
