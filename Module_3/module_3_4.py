# Произвольное число параметров

def single_root_words(root_word, *other_words):
    same_words = []
    for word_ in other_words:
        if root_word.lower() in word_.lower() or word_.lower() in root_word.lower():
            same_words.append(word_)
    return same_words


result_1 = single_root_words('first', 'second', 'third', 'fIRst of all', 'UnFirstable', 'FIR')
result_2 = single_root_words('TelePhoneGramm', 'ring', 'tele', 'kinder', 'LEPH')
print()
print(result_1)
print(result_2)
