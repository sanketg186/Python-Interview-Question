# Write a function that takes in a list of dictionaries with a key and list of integers and 
# returns a dictionary with the standard deviation of each list.
# Note that this should be done without using the numpy built in functions. 
# input = [ { 'key': 'list1', 'values': [4,5,2,3,4,5,2,3], }, { 'key': 'list2', 'values': [1,1,34,12,40,3,9,7], } ]
 # output -> {'list1': 1.12, 'list2': 14.19}

import math

def mean(x):
  m = 0.0
  for num in x:
    m = m+num
  m = m/len(x)
  return m

def deviation(x):
  m = mean(x)
  var = 0.0
  for num in x:
    var = var + (num-m)**2
  sd = (var/len(x))**(.5)
  return sd

 def compute_deviation(input):
  op = {}
  for lis in input:
    vals = lis['values']
    sd = deviation(vals)
    op[lis['key']] = sd
  return op

op = compute_deviation(input)
print(op)