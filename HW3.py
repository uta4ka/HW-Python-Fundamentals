philosophy = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

better_count = philosophy.count("better")
never_count = philosophy.count("never")
is_count = philosophy.count("is")

uppercase_philosophy = philosophy.upper()

replaced_philosophy = philosophy.replace("i", "&")

number = 1234

product = 1
digits = []
n = number
while n > 0:
    digit = n % 10
    product *= digit
    digits.append(digit)
    n //= 10

reverse_number = int("".join(map(str, digits))

sorted_number = int("".join(sorted(map(str, digits)))

a = 5
b = 10

a, b = b, a

print(f"Occurrences of 'better': {better_count}")
print(f"Occurrences of 'never': {never_count}")
print(f"Occurrences of 'is': {is_count}")
print(uppercase_philosophy)
print(replaced_philosophy)
print(f"Product of digits: {product}")
print(f"Number in reverse order: {reverse_number}")
print(f"Number in ascending order: {sorted_number}")
print(f"a: {a}, b: {b}")