# Braydn Ballard
# UWYO COSC 1010
# 09/23/24
# Lab 03 
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
allstates = ["Wyoming", "Colorado", "Montana"]


#print the entire list
print(allstates)

#now print the first element in the list
print(allstates[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(allstates[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided

print(f"{allstates[1].upper()} is south of {allstates[0].upper()}")


print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
allstates.append("Washington")
allstates.append("Oregon")
allstates.append("California")
print(allstates)
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
allstates[-2] = "Maine"
print(allstates)
#Insert the state Texas to be the third element in the list, again printing your list
allstates.insert(2,"Texas")
print(allstates)
#Using the `del` statement remove the fourth item from the list, print your list 
del allstates[3]
print(allstates)
#Remove Texas using its value, print the list

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(allstates))
print(allstates)
#Permanently sort your list in reverse order, printing it out
allstates.sort(reverse=True)
print(allstates)
#Using the reverse method reverse the list and print it
allstates.reverse()
print(allstates)
