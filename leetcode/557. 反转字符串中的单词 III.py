

def reverseWords():
    s = [x[::-1] for x in input().split()]
    print(" ".join(s))

if __name__ == '__main__':
    reverseWords()