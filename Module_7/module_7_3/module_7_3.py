# Оператор "with"
import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        print(self.file_names)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            words = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                                    # для СЕБЯ text = line.translate(str.maketrans('', '', string.punctuation)).lower()
                    punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    text = ''.join([c for c in line.lower() if c not in punctuations])
                    words.extend(text.split())
            all_words.update({name: words})
        return all_words

    def find(self, word):
        results = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                results.update({name: words.index(word.lower()) + 1})
        return results

    def count(self, word):
        results = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                results.update({name: words.count(word.lower())})
        return results

finder1 = WordsFinder('module_7_3.txt', 'module_7_3_ex.txt')

print(finder1.get_all_words())  # Все слова

print(finder1.find('TEXT'))  # 3 слово по счёту

print(finder1.count('teXT'))  # 4 слова teXT в тексте всего
