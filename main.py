"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64 + 32)

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
number_1 = 64
number_2 = 32
print(number_1 + number_2)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
year = "2021"
month = "February"
day = "2"
sentence_1 = "Today is " + month + " " + day + "," + year
print (sentence_1)

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence_2 = "This is my first Python program."
print(len(sentence_2))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
def overscan_value(percentage):
    """This is the fuction to calculate overscan percentage of resolution 1920*1080.
    
    Args:
        percentage(int) = percentage number of overscan
        
    Calculate:
        value_1(int) = calculate overscan percentage of 1920.
        value_2(int) = calculate overscan percentage of 1080.
        
    Convert:
        value_str1(str) = convert value_1(int) into string.
        value_str2(str) = convert value_2(int) into string.
        percentage_value(str) = convert percentage(int) into string.

    Returns:
        str:message
        
    """
    value_1 = 1920 * (1 + percentage *0.01)
    value_2 = 1080 * (1 + percentage *0.01)
    value_str1 = str(value_1)
    value_str2 = str(value_2)
    percentage_value = str(percentage)
    message = "The " + percentage_value + "% overscan of 1920 is " + value_str1 + ", and the 1080 is " + value_str2 + "."
    return message
print(overscan_value(10))