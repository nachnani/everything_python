word = "panasonic"
# treat a string like a list
print(word[0])

# get the length of string
l = len(word)

# loop through all the items from the start
print('Printing the string straight')
for i in range(l):
    print(word[i])

# loop through the items in reverse
print('Printing the string in reverse')
for i in range(l):
    print(word[l - i - 1])

# comparing and returning if palindrome
palindrome_flag = True
for i in range(l):
    if word[i] != word[l - i - 1]:
        palindrome_flag = False
        break
    else:
        palindrome_flag = True

if palindrome_flag:
    print("The string is a palindrome")
else:
    print('The string is not a palindrome')


# converting the above code into a function
def check_palindrome(word):
    # get the length of the string
    l = len(word)
    for i in range(l):
        if word[i] != word[l - i - 1]:
            return False
    return True


# call the above function
print(check_palindrome("racecar"))