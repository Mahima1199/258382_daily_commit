# tuples are very similar to lists except that they are immutable
# Tuples are created using paranthesis rather than sqaure brackets
word = ("spam","eggs","sausages")
print(word[0])
# Typing to reassign values in tuple causes TypeError
# Tuples can be created without parenthesis by just separating values with commas
my_tuple = "one","two","three"
print(my_tuple[0])
# Tuples are faster than lists but they cannot be changed
#List_Slices
squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[0:4])
print(squares[5:9])
print(squares[3:10])
print(squares[:7])
print(squares[7:])
print(squares[::2])
print(squares[2:8:3])
print(squares[2:8:2])
print(squares[9::-1])





























