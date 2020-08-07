# Strings are ordered sequences. Which means both INDEXING and SLICING can be used to grab sub-sections of the string
# 
# INDEXING notation uses [] notation after the string (or variable assigned the string)
# INDEXING allows you to grab a single character from the string
# These actions use [] and a number index to indicate positions of what you wish to grab
#        Character: H  E  L  L  O
#            Index: 0  1  2  3  4
# Reverse Indexing: 0 -4 -3 -2 -1
# SLICING allows you to grab a subsection of multiple characters, a "slice" of the string
# This has the following syntax:
# [start:stop:step]    
# Start is a numerical index for the slice start
# Stop is the index it will stop at but not include
# Step is the size of the "jump" to the next index
# white spaces count as characters inside of the string

# Indexing 0,1,2,3,4
# this  = 'this is also a string'
# print(this)
# print(this[5])
# print(this[3])
# print(len(this))

# helloWorld = "Hello, \n world"
# print(helloWorld)

# worldhello= "Hello, \nworld"
# print(worldhello)

# helloTabWorld = "Hello, \tworld"
# print(helloTabWorld)

# mystring = "Hello World"
# print(mystring[-2])

#Slicing start : stop : skip 
# mystring = 'abcdefghijk'
# print(mystring[2:4])
# prints cd
# slice cgk
# mystring = 'abcdefghijk'
# print(mystring[2::4])
# cgk
# slice fghi
# mystring = 'abcdefghijk'
# print(mystring[5:9])
# slice every other letter
# mystring = 'abcdefghijk'
# print(mystring[::2])
# print the string backwords
# mystring = 'abcdefghijk'
# print(mystring[::-1])