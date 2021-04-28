nums = [4,5,6]
msg = "Numbers:{0},{1},{2}".format( nums[0],nums[1],nums[2] )
print(msg)

#string formatting can also be done with named arguments
a = "{x},{y}".format(x = 5, y = 12)
print(a)

# different useful functions
print("!".join(["spam","eggs","ham"]))
print("Hello Me".replace("Me","World"))
print("This is a sentence".startswith("This"))
print("This is sentence".endswith("sentence"))
print("This is a sentence".upper())
print("I LOVE INIDA".lower())
print("spam,eggs,ham".split(","))
