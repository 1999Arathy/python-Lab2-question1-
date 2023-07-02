#Python Program to Compute all the Permutation of the String

def permutation(str1,i=0):
    if i== len(str1):
        print("".join(str1))
    for j in range(i,len(str1)):
        words = [c for c in str1]
        words[i], words[j] = words[j], words[i]
        permutation(words,i+1)
print(permutation('aeiou'))