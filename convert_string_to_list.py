#  How would you convert a string into list of elements?
#  Example:
# Input:
# string = '320,321,320,ATR'
# Output:
# ['320','321','ATR']
string = '320,321,320,ATR'
print(list(set(list(string.split(',')))))