# Assignment 01

# Name: Krushnal Jagannath Patil
# Student Id: CT_S_PCCOER_DATA_SCIENCE_196
# Contact No: 9096945134
# Email ID: krushnalpatil1111@gmail.com
# Internship Repository: https://github.com/Krushnal121/DataPulse.git

# 01. Right Half Pyramid
print("Right Half Pyramid:\n")
[print(i*'*') for i in range(1,6)]

# 02. Inverted Right Half Pyramid
print("\n\nInverted Right Half Pyramid:\n")
[print(i*'*') for i in range(5,0,-1)]

# 03. Left Half Pyramid
print("\n\nLeft Half Pyramid:\n")
[print((i*'*').rjust(5)) for i in range(1,6)]

# 04. Inverted Left Half Pyramid
print("\n\n inverted Left Half Pyramid:\n")
[print((i*'*').rjust(5)) for i in range(5,0,-1)]

# 04. Full Pyramid
print("\n\n Full Pyramid:\n")
[print((i*'*').center(9,)) for i in range(1,10,2)]

# 04. Inverted Full Pyramid
print("\n\n Inverted Full Pyramid:\n")
[print((i*'*').center(9,)) for i in range(9,0,-2)]