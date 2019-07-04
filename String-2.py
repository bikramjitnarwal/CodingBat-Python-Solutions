# double_char:
# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  string = ""
  for i in range(len(str)):
    string += str[i]*2
  return string

# count_hi:
# Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      count += 1
  return count

# cat_dog:
# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    dogCount = 0
    catCount = 0

    length = len(str)

    for i in range(length - 2):
        if str[i] == 'd' and str[i + 1] == 'o' and str[i + 2] == 'g':
            dogCount += 1
        elif str[i] == 'c' and str[i + 1] == 'a' and str[i + 2] == 't':
            catCount += 1

    if dogCount == catCount:
        return True
    else:
        return False

# count_code:
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any
# letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
    count = 0

    for i in range(len(str) - 3):
        if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
            count += 1

    return count

# end_other:
# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring
# upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
    if a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()):
        return True
    else:
        return False

# xyz_there:
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a
# period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    return str.count('.xyz') != str.count('xyz')