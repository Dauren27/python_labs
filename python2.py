#Задание 1
sentence = input("Введите строку: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Самое длинное слово:", longest_word)
#Задание 2
sentence = input("Введите строку, разделенную точкой запятой: ")
words = sentence.split(';')
longest_word = max(words, key=len)
print("Самое длинное слово:", longest_word)
#Задание 3
sentence = input("Введите строку: ")
delimiter = input("Введите знак разделения: ")
words = sentence.split(delimiter)
shortest_word = min(words, key=len)
print("Самое короткое слово:", shortest_word)
#Задание 4
sentence = input("Введите строку: ")
search_word = input("Введите слово для поиска: ")
if search_word in sentence:
    print(f"Слово '{search_word}' найдено в строке.")
else:
    print(f"Слово '{search_word}' не найдено в строке.")
#Задание 5
sentence = input("Введите предложение: ")
word_count = len(sentence.split())
print("Количество слов в предложении:", word_count)