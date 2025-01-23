#1. Even Odd
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
        
# print(is_even(3))

# &&-----------------------------------------------------------------------------------------------------------------------

#2. Factorial
def factorial(num):
    fact = 1
    while True:
        if num < 2:
            return fact
        else:
            fact *= num
            num -= 1
        
# print(factorial(3))

# ChatGPT Factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# print(factorial(3))  # Output: 6

# &&-----------------------------------------------------------------------------------------------------------------------

#3.  Check is palindrom

def is_palindrom(str):
    lower_str = str.replace(" ", "").lower()
    strTrim=""
    for char in lower_str:
        # Check if the character is alphanumeric
        if char.isalpha():
            strTrim += char
    if strTrim == strTrim[::-1]:
        return True
    else:
        return False
    
print(is_palindrom("A man, a plan, a canal: Panama"))

# &&-----------------------------------------------------------------------------------------------------------------------

#4. FIZZBUZZ
def fizz_buzz(n):
    list= []
    for x in range(1,n+1):
        if x%3==0 and x%5==0:
            list.append("FizzBuzz")
        elif x%3==0:
            list.append("Fizz")
        elif x%5==0:
            list.append("Buzz")
        else:
            list.append(str(x))
    return list
    
# print(fizz_buzz(15))

# &&-----------------------------------------------------------------------------------------------------------------------

#5. Count the vowels
def count_vowels(s):
    count =0
    for char in s.lower():
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            count +=1
    return count
        
# print(count_vowels("Hello World"))

#ChatGPT solution
def count_vowels(s):
    count = 0
    vowels = "aeiou"  # You can use a string or set for vowels
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# print(count_vowels("Hello World")) # Output: 3

# &&-----------------------------------------------------------------------------------------------------------------------

#6. Sum of digits 
def sum_of_digits(n):
    sum = 0
    while n>0:
        reminder = n%10
        sum += reminder
        n = int(n/10)
    return sum

# print(sum_of_digits(12345))
    
# &&-----------------------------------------------------------------------------------------------------------------------


#7. Reverse String
def reverse_string(s):
    return s[::-1]
    
# print(reverse_string("Hello"))

# &&-----------------------------------------------------------------------------------------------------------------------


#8. Common Elements
def common_elements(list1, list2):
    result = []
    for x in list1:
        if x in list2 and x not in result:
            result.append(x)
    return result
list1 = [1, 2, 3,3, 4]
list2 = [3, 4, 5,4,2, 6]
# print(common_elements(list1, list2))

#chat GPT solution
def common_elements(list1, list2):
    return list(set(list1) & set(list2))  # Using set intersection to find common elements

list1 = [1, 2, 3, 3, 4]
list2 = [3, 4, 5, 4, 2, 6]
# print(common_elements(list1, list2))  # Output: [2, 3, 4]

# &&-----------------------------------------------------------------------------------------------------------------------


#9. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    if len(left)>0:
        sortedLeft = merge_sort(left)
    if len(right)>0:
        sortedRight = merge_sort(right)
    return merge(sortedLeft,sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge elements from both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from the left list
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from the right list
    while j < len(right):
        result.append(right[j])
        j += 1
    # print(result)
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))

#chat GPT solution

# Merge Sort
def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    sortedLeft = merge_sort(left)
    sortedRight = merge_sort(right)
    
    # Merge the sorted halves
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge elements from both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from the left list
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from the right list
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

# Test the function
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))

# &&-----------------------------------------------------------------------------------------------------------------------
    
    
    
    
    
    


