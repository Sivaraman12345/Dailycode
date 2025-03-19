def vowelCount(s):
    
    vowels={'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
    for c in s:
        if c in vowels:
            vowels[c]+=1
    return vowels
s=input("Enter a String: ")
print(vowelCount(s))