'''
Find length of a string in python 
'''
def strlen(s):
    counter = 0
    for _ in s:
        counter+=1
    return counter    
print("Length:",strlen(input("Enter a string: ")))
