"""
StringPerm.py
Simple Program to print all permutations of a string.
I play a single player game on my phone where they give you a collection of letters
and you are supposed to make as many words out of those letters as you can, and it
caught me as a good computer science problem to try and solve for myself.
Elijah Theander
11/06/19
"""
import sys
import keyboard


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
            
#Function to take a list of string permutations,truncate it for all permutations of length 2-n
#and then add those permutations into a set to remove all duplicates.
#takes starting length, overall length of string,the list of strings, and the set of strings
def createSet(startlength,length,stringlist,permset):
    if(startlength==length):
        for i in stringlist:
            permset.add(i)
        return
    else:
        for i in stringlist:
            permset.add(i[0:startlength])
        createSet(startlength+1,length,stringlist,permset)

#Function to turn the Set of permutations, load it into a list, and sort alphabetically
def setToList(permset):
    stringlist = list(permset)
    stringlist.sort()
    return stringlist

#function to generate list of lists.
def listList(length):
    returnlist = []
    for x in range(0,length-1):
        returnlist.append([])
    
    return returnlist 
    

#Function to sort the list by length.
def sortList(listList,length,startlength,stringlist):
    if (startlength==length):
        for i in stringlist:
            if(len(i) == length):
                listList[length-2].append(i)
        return
    else:
        for i in stringlist:
            if(len(i) == startlength):
                listList[startlength-2].append(i)
        sortList(listList,length,startlength+1,stringlist)

#Function that ties all of the above functions together, and returns the list of lists
def stringPerm(theString):
    length = len(theString)
    letters = list(theString)
    perms=set()
    stringList = [theString]

    permutation(letters,0,length-1,stringList)
    createSet(2,length,stringList,perms)
    stringList = setToList(perms)

    nestedList = listList(length)
    sortList(nestedList,length,2,stringList)
    
    
    return nestedList
 


#driver program to test above function

print("Press Enter to input your letters,or press Esc to exit:")

while True:
    try:
        if keyboard.is_pressed('ENTER'):
            print("Enter your letters without spaces:")
            string_input = input()
            n = len(string_input)
            perm_list = stringPerm(string_input)
            for x in range(0,n-1):
                print("Letter Permutations with "),print(x+2),print("letters:")
                print(perm_list[x]),print('\n')
            print("Press Enter again to try a new set of letters, or Esc to close")

        if keyboard.is_pressed('Esc'):
            print("Exiting...")
            sys.exit(0)
    except:
        break
       
            
            

