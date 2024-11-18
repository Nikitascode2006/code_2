def find_maximum_difference(a, b):
#     # code implementation here...
   largest_value = max(max(a), max(b))
    
    # Find the smallest number from the other list
   smallest_value = min(a) if largest_value in b else min(b)

    # Calculate the difference
   maximum = largest_value - smallest_value
   return maximum
print(find_maximum_difference([1,5,600],[100,7,3,29,39]))
print(find_maximum_difference([1,5 ,600], [100 ,7, 3 , 602, 39]))

