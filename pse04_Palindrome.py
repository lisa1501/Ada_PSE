def is_palindrome(a):
    if len(a) < 2:
        raise Exception("String length should greater than 2.")
    
    if a.isalpha():#o(n)
        a_lower_case = a.lower() #o(n)
        return a_lower_case == a_lower_case[::-1] #o(n)
    else:
        raise Exception("Please input a valid letter!")

# answer_1 = is_palindrome("racecar")
# answer_2 = is_palindrome(None)
# answer_3 = is_palindrome("ABCDcba")
# answer_4 = is_palindrome("a%vdv%a")

print(type(True))

"ab343ba"

#1.Time and space complexity #o(n)/#o(n)
#2.edge case : special requirement for the length of string. empty string, length <2
#3.is there any requirement for upper case and lower case
#4.there are no letter character in the string. like number or symbol
#5.if input is Null
#6. raise the exception is the they want it .

def insertion_sort(array):
    i = 1
    while i < len(array):
        to_insert = array[i] 
        j = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i]
        while j > 0 and array[j-1] > to_insert:
            array[j] = array[j-1]
            j -= 1
        array[j] = to_insert
        i += 1




