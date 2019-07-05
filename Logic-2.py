# make_bricks:
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
# bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is
# a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
  big_needed = min(big, goal // 5)
  return goal - (big_needed * 5) <= small

# lone_sum:
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values,
# it does not count towards the sum.

def lone_sum(a, b, c):
  sum = a+b+c
  if a == b:
    if a == c:
      sum -= 3 * a
    else:
      sum -= 2 * a
  elif b == c:
    sum -= 2 * b
  elif a == c:
    sum -= 2 * a
  return sum

# lucky_sum:
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the
# sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
  array = [a, b, c]
  sum = 0
  i = 0

  while i < len(array) and array[i] != 13:
    sum += array[i]
    i += 1
  return sum

# no_teen_sum:
# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19
# inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper
# "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you
# avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level
# as the main no_teen_sum().

def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)

  return a + b + c

def fix_teen(n):
  # checks if n is a teen
  if 13 <= n <= 19:

    # checks if n is 15 or 16 but checking if it is found in the set
    # if True then leave n as it is
    if n in {15, 16}:
      n = n
      return n

    # if it fails then n = 0
    else:
      n = 0
      return n

  # if n is not in the teens return it as is
  return n

# round_sum:
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15
# rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12
# rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a
# separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level
# as round_sum().

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)


def round10(num):
  n = num % 10
  if (n >= 5):
    return (num - n + 10)
  else:
    return (num - n)

# close_far:
# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  return (is_close(a, b) and is_far(a, b, c)) or (is_close(a, c) and is_far(a, c, b))


def is_close(a, b):
  return abs(a - b) <= 1


def is_far(a, b, c):
  return abs(a - c) >= 2 and abs(b - c) >= 2

# make_chocolate:
# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be
# done.

def make_chocolate(small, big, goal):
  maxBig = goal / 5

  if big >= maxBig:
    if small >= (goal - maxBig * 5):
      return goal - maxBig * 5
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1