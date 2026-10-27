sentence = "My home area is \"abz\""  #escape character
#print(sentence)

#operations
#-> functions e.g. print function

#print(sentence.upper())

sentence = sentence.upper()

print(sentence)
print(sentence.capitalize())  #first letter is caps
print(sentence.title())  #first letter of every word is caps

name = "Dalton"

print(name.count("D"))  #call a function -- use it, parameter is the D data

print(name.find("D"))

print(name.rfind("D"))

print(len(sentence))
replaced_sentence = sentence.lower().replace("home", "city") #replace is case-sensitive, we have chained functions
print(replaced_sentence.title())
print(replaced_sentence.istitle())

k ="123"
print(k.isnumeric()) #functions that start with is always check