# слово изначально
worded = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"] # здесь хранятся неизветсные буквы
word = input("Какое слово  ")
word = list(word.lower())
print(word)
s = len(word)
print(s)
print(worded[0:s])
