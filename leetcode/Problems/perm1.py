import itertools

'''
## combinations order does't matter 
combinations = itertools.combinations(my_list, 3)
for c in combinations:
    print c 

'''

'''
## permutations order matters 
my_list = [1,2,3]

permutations = itertools.permutations(my_list, 2)
for p in permutations:
    print p 
'''

my_list = [1,2,3,4,5,6]

word = "sample"
my_letters = "plmeas"

combinations = itertools.combinations(my_list,3)
permutations = itertools.permutations(my_letters,6)


## this example showes that order does't matter 
## print [ result for result in combinations if sum(result) == 10]

for p in permutations:
    print p 
    if "".join(p) == word:
        print "Match !"
        break 
else:
    print "No Match !"



