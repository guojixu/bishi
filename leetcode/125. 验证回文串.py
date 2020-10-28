
s = input()

s1 = "".join(ch.lower() for ch in s if ch.isalnum())

print(s == s[::-1])