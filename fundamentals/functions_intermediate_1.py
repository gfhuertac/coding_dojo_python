import random
def randInt(min=0, max=100):
  if min>=max:
    raise Exception('max should be greater than min')
  if min < 0 or max < 0:
    raise Exception('min and max should be greater or equal than 0')
  num = random.random()*(max-min) + min
  return round(num)

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500