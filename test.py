from mathgenerator import mathgen

# test your generators here
print(mathgen.addition())
print(mathgen.addition(format='latex'))

# prints each generator in genList
list = mathgen.getGenList()
for item in list:
    pass
    # print(item[2])

# print(mathgen.getGenList())
# print(mathgen.genById(10))

#Make a pdf with 10 problems of generator id 1
# mathgen.makePdf(0, 10)
