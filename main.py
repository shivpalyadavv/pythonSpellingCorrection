from textblob import TextBlob
def Convert(string):
    li = list(string.split())
    return li
str1 = input("Eter you word : ")
words=Convert(str1)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words: ",words)
print("corrected Wordsare :")
for i in corrected_words:
    print(i.correct(), end=" ")