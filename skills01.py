# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
	odd_list = []
	for item in number_list:
		if item % 2 != 0:
			odd_list.append(item)
	return odd_list
    
print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even_list = []
    for item in number_list:
    	if item % 2 == 0:
    		even_list.append(item)
    return even_list

print all_even(number_list)

# Write a function that takes a list of strings and return a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_string_list = []
    for item in word_list:
    	if len(item) >= 4:
    		new_string_list.append(item)
    return new_string_list
    
print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
	lowest_num = number_list[0]
	for item in number_list:
		if item < lowest_num:
			lowest_num = item
	return lowest_num

print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
	largest_num = number_list[0]
	for item in number_list:
		if item > largest_num:
			largest_num = item
	return largest_num

print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    half_list = []
    for item in number_list:
    	half_list.append(item / 2.0)
    return half_list
    
print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
	length_of_words = []
	for item in word_list:
		length_of_words.append(len(item))
	return length_of_words
    
print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
	sum_of_numbers = 0
	for item in number_list:
		sum_of_numbers = item + sum_of_numbers
	return sum_of_numbers

print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
	product = 1
	for item in number_list:
		product = item * product
	return product

print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
	sum_of_words = ""
	for item in word_list:
		sum_of_words = sum_of_words + item
	return sum_of_words

print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
	sum_of_nums = 0
	for item in number_list:
		sum_of_nums = item + sum_of_nums
	avg_of_nums = sum_of_nums / len(number_list)
	return avg_of_nums

print average(number_list)