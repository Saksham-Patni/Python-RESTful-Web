import re

file = open('regex_sum_7282.txt', 'r')
#file = open('Regex.txt', 'r')
list_integers = list()

for line in file:
    line = line.rstrip()
#print (line)
    integers_list = re.findall('[0-9]+', line )
#print (integers_list)
    str_to_int = [int(i) for i in integers_list]
#print (str_to_int)
    list_integers.append(sum(str_to_int))
#print (list_integers)
    total = sum(list_integers)
    print (total)
