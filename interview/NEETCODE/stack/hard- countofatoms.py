class Solution:
    def countOfAtoms(self, formula):
        # will contain hash-maps with count of elements in last meeted brackets
        n = len(formula)
        result_counter = {}
        parenthesis_stack = []
        cur_ind = 0

        while cur_ind < n:
            cur_char = formula[cur_ind]

            if cur_char == "(":
                cur_ind += 1
                parenthesis_stack.append({})
                continue

            if cur_char == ")":
                mult = ""
                cur_ind += 1

                while cur_ind < n and formula[cur_ind].isdigit():
                    mult += formula[cur_ind]
                    cur_ind += 1

                last_counter = parenthesis_stack.pop()
                target = parenthesis_stack[-1] if parenthesis_stack else result_counter
                for elem, counter in last_counter.items():
                    if elem not in target:
                        target[elem] = 0
                    target[elem] += counter * (int(mult) if mult else 1)
                continue

            cur_elem = ""
            cur_counter = ""
            target = parenthesis_stack[-1] if parenthesis_stack else result_counter

            while cur_ind < n and cur_char not in "()":
                if cur_char.isalpha():
                    if cur_char.isupper() and cur_elem != "":
                        if not cur_elem in target:
                            target[cur_elem] = 0
                        target[cur_elem] += int(cur_counter) if cur_counter else 1
                        cur_counter = ""
                        cur_elem = ""
                    cur_elem += cur_char
                else:
                    cur_counter += cur_char
                cur_ind += 1
                if cur_ind != n:
                    cur_char = formula[cur_ind]

            target = parenthesis_stack[-1] if parenthesis_stack else result_counter
            if not cur_elem in target:
                target[cur_elem] = 0
            target[cur_elem] += int(cur_counter) if cur_counter else 1

        parts = [
            elem + str(counter) if not counter == 1 else elem for elem, counter in result_counter.items()
        ]
        parts.sort()

        return "".join(parts)

'''
🎯 Problem Description
You are given a string formula which represents some valid chemical formula. Your task sounds very easy - you need to count chemical elements in this string (for details look description)

📥⤵️ Input:
String array formula representing a valid chemical formula
📤⤴️ Output:
Counted elements as new string sorted by elements' names (element followed by irs number in formula)

1️⃣🧠 Approach: Stack Of Hashmaps
🤔 Intuition
This problem just blew my mind. At first glance it seems like an easy task, but when you think about implementation...

First of all, when problem asks you to process some string which contains brackets it's already a good tip for using stack.
But what we want to store in stack? Since in one pair of brackets we can have multiple elements and since we want to somehow efficiently count them and multiply counters if we find multiplier after bracket it's a good choice to store every "pair of bracket" in stack as a hashmap (dictionary) where key is element's name and value is its counter for current bracket.
Let's think about how we want to process characters in the formula:
First of all, as long as character we're considering now is not "(" or ")" we understand that we're looking at normal formula without brackets, so we will jave only letters and numbers. But where we want to add this counters? If are currently not in bracket then we want to add this counter to final result, in the other case we want to add this counter to the LAST pair of brackets we founded (this is idea behind using stack)
If we found "(" all we want to do is to add new element in the stack -> just append empty hashmap to the stack.
If we found ")" we know for sure that we have at least one element in stack. We want to parse multiplier for this bracket if it exists and then add counter multiplied by multiplier to the:
Result hashmap if there's no more elements in stack (this was one-level nesting and we ended up in normal formula without brackets)
Hashmap in stack that was before this, since that means that this pair of brackets was nested in some other pair
After we counted all elements in result hashmap we want to sort them and create string as required in problem statement
👩🏻‍💻 Coding
Initialize result_counter as an empty dictionary to store the counts of each element.

Initialize parenthesis_stack as an empty list to store dictionaries for counts of elements inside parentheses.

Initialize cur_ind to 0 to serve as the current index while iterating through the formula.

Start a while loop that runs until cur_ind is less than n.

If cur_char is an opening parenthesis (:

Increment cur_ind by 1.
Append an empty dictionary to parenthesis_stack.
If cur_char is a closing parenthesis ):

Initialize mult as an empty string to store the multiplier.
Increment cur_ind by 1.
While the current character is a digit, append it to mult and increment cur_ind.
Pop the last dictionary from parenthesis_stack into last_counter.
Set target to the last dictionary in parenthesis_stack if it exists, otherwise set it to result_counter.
For each element and count in last_counter, add the count multiplied by mult (or 1 if mult is empty) to the corresponding count in target.
If cur_char is not any of brackets:

Initialize cur_elem as an empty string to store the current element.
Initialize cur_counter as an empty string to store the current element's count.
Set target to the last dictionary in parenthesis_stack if it exists, otherwise set it to result_counter.
While the current character is not a parenthesis and the index is within bounds:
If the character is an alphabet:
If the character is uppercase and cur_elem is not empty, add cur_elem to target with its count.
Reset cur_counter and cur_elem.
Append the character to cur_elem.
Otherwise, append the character to cur_counter.
Increment cur_ind by 1 and update cur_char.
Add the last element and its count to target.
Construct the output by joining element names and their counts (if greater than 1) sorted by element names.

Return the resulting string.

📘 Complexity Analysis
⏰ Time complexity: O(n^2), since at the end we use sorting (n log n), but in the loop we constantly readding characters from hashmap to hashmap and in the worst case we will do this n // 2 times with every hashmap containing up to n - (number of brackets so in total this result in O(n^2) TC
🧺 Space complexity: O(n), since stack will have size up to n // 2 -> O(n
'''