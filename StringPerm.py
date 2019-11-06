"""
StringPerm.py
Simple Program to print all permutations of a string.
I play a single player game on my phone where they give you a collection of letters
and you are supposed to make as many words out of those letters as you can, and it
caught me as a good computer science problem to try and solve for myself.
Elijah Theander
11/06/19
"""

def toString(List):
    return ''.join(List)

#Function to print Permutations of strings
#Takes string, starting index of string, ending index of string, and a list of all the strings
def permutation(letters,start,end,stringlist):
    if start==end:
        stringlist.append(toString(letters))
    else:
        for i in range(start,end+1):
            letters[start],letters[i] = letters[i],letters[start]
            permutation(letters,start+1,end,stringlist)
            letters[start],letters[i] = letters[i],letters[start]


#driver program to test above function

thestring = "EICSP"
n = len(thestring)
a = list(thestring)
perms = {thestring}
stringList = [thestring]
permutation(a,0,n-1,stringList)
print(stringList)

