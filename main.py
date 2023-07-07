import re
from itertools import permutations
import requests
from typing import List


class Desafios:
    title = "(before and after):"

    def reverse_phrase_part_1(self, string_phrase: str) -> str:
        """ outputs string_phrase as it is and reversed, finally returns it reversed
        :param string_phrase: any string text
        :return: reversed phrase keeping letters' ordering
        """
        revered_phrase = " ".join(string_phrase.split()[-1::-1])

        print("Ex.1)")
        print(f"{self.title} {string_phrase}")
        print(f"{' ' * (len(self.title) - 1)}: {revered_phrase}")

        return revered_phrase

    def remove_duplicated_characters(self, string_phrase: str) -> str:
        """ outputs string_phrase as it is and reversed, finally returns it without duplicated characters
        :param string_phrase: any string text
        :return: string_without_duplicates
        """
        string_without_duplicates = ''.join(dict.fromkeys(string_phrase).keys())

        print("Ex.2)")
        print(f"{self.title} {string_phrase}")
        print(f"{' ' * (len(self.title) - 1)}: {string_without_duplicates}")

        return string_without_duplicates

    def find_largest_palindrome_substring(self, string_phrase: str) -> str:
        """ outputs the largest palindrome substring that is in each word. After that, outputs the largest between them.
            If a palindrome in each word have same size, it shows the first

        :param string_phrase: any string text
        :return: the largest palindrome in the string_phrase passed by parameter if it exists, else an empty string
        """
        words_list = string_phrase.split()
        # finding palindrome in any place of a word
        palindrome_words_list = {}
        for word in words_list:

            # The minimum number of letters possible for palindromes is 3
            if len(word) < 3:
                continue

            # find palindromes
            palindrome_words_list[word] = []
            for start_index in range(len(word)):
                # i + 3 because the minimum number of letters possible for palindromes is 3
                for end_index in range(start_index + 3, len(word) + 1):
                    term = word[start_index:end_index]
                    if term == term[::-1] and term not in palindrome_words_list[word]:
                        palindrome_words_list[word].append(term)

        # remove keywords without palindromes in it
        palindrome_words_list = {key: val for key, val in palindrome_words_list.items() if val}
        if palindrome_words_list:
            # largest palindromes per word & largest palindrome substring of all
            largest_palindrome_in_each_word = {key: max(val) for key, val in palindrome_words_list.items()}
            largest_palindrome_substring = max(largest_palindrome_in_each_word.values())

            print("Ex.3) Find Largest palindrome word")
            print(f"{self.title} {largest_palindrome_in_each_word}")
            print(f"{' ' * (len(self.title) - 1)}: largest palindrome is {largest_palindrome_substring}")

            return largest_palindrome_substring
        # palindrome_words_list list could be empty
        return ''

    def capitalize_phrasal_strings(self, string_phrase: str) -> str:
        """ outputs the param and the return
        :param string_phrase: any string text
        :return: string phrase capitalized when it starts a new sentence
        """
        pattern = r'([.?!]\s*\w)'

        def sets_repl(match: re.Match): return match.group(1).upper()

        capitalized_string_phrase = string_phrase.capitalize()
        capitalized_string_phrase = re.sub(pattern, sets_repl, capitalized_string_phrase)

        print("Ex.4) Capitalize string that initializes a phrase")
        print(f"{self.title} {string_phrase}")
        print(f"{' ' * (len(self.title) - 1)}: {capitalized_string_phrase}")

        return capitalized_string_phrase

    def is_anagram_of_palindrome(self, word: str) -> bool:
        """ outputs when if it's an anagram of palindrome, or only anagram or only palindrome
        :param word: only one word
        :return bool: if True -> is an anagram of palindrome. else False
        """
        # Only one word per argument, if *words as argument, then try to yield instead returning
        if len(word.split()) > 1:
            raise ValueError('It is supposed to be only one word per string')

        print(f"Ex.5) Get Anagrams of palindromes for word \033[1;34m{word}\033[m")

        # get anagrams & check idiom Andof word
        anagrams_dict = self._get_anagrams_dict(main_word=word)
        # load a txt dictionary from the web
        portuguese_real_words, english_real_words = self._loads_pt_and_en_words_dictonary()
        anagrams_of_palindrome_words = []

        # All palindromes are anagrams as well
        if self._is_palindrome(word):
            # racecar case
            anagram = word[-1::-1].lower()
            if anagram in portuguese_real_words or anagram in english_real_words:
                anagrams_of_palindrome_words.append(word[-1::-1].lower())

        for key, values in anagrams_dict.items():
            # check if any anagram is a palindrome
            for anagram in values:
                if self._is_palindrome(anagram) and anagram not in anagrams_of_palindrome_words:
                    anagrams_of_palindrome_words.append(anagram)
        if any(anagrams_of_palindrome_words):
            # Yes it is anagram of palindrome
            print("\033[1;32mYes!!!\033[m", anagrams_of_palindrome_words[0])
            # in this case it will be always only one word...
            return True
        elif any(anagrams_dict.values()):
            # Despite having anagrams, it doesn't contains palindrome words
            only_anagrams_list = [words for words in list(anagrams_dict.values()) if words]
            print(
                f"Despite having anagrams like {only_anagrams_list}, It DOESN'T have any anagram of palindrome")
            return False
        else:
            # Nor a palindrome neither an anagram
            print("We don't have any palindromes or anagrams found in any dictionary")
            return False

    def _get_anagrams_dict(self, main_word: str) -> dict:
        """
        :param main_word: any single word
        :return: dict containing each unique letter in main_word
        """
        if len(main_word.split()) > 1:
            raise ValueError('It is supposed to be only one word per string')
        # Get dictionary words
        portuguese_real_words, english_real_words = self._loads_pt_and_en_words_dictonary()

        # Check if main_word is in english or portuguese
        _word_in_english = _word_in_portuguese = False
        if main_word.lower() in english_real_words:
            _word_in_english = True
        if main_word.lower() in portuguese_real_words:
            _word_in_portuguese = True

        # declare dictionary_as_list based on word_in_english and word_in_portuguese
        if _word_in_english and _word_in_portuguese:
            dictionary_as_list = sorted(portuguese_real_words + english_real_words)
        elif _word_in_portuguese:
            dictionary_as_list = portuguese_real_words
        elif _word_in_english:
            dictionary_as_list = english_real_words
        else:
            dictionary_as_list = english_real_words

        # Get all sequence possible through word using permutation
        permuted_sequence = self._get_permutation_word_sequence(any_word=main_word)

        dict_with_words_by_initial = {}
        # loop through all main_word letters  that did not repeat yet
        for e, initial_letter in enumerate(sorted(set(letter.lower() for letter in main_word))):
            dict_with_words_by_initial[initial_letter] = []
            # filter in dictionary by the initial letter of the real word to check if term exists
            real_words = list(filter(lambda w: w.startswith(initial_letter), dictionary_as_list))
            # filter only terms that contain the initial letter
            for term in filter(lambda w: w.startswith(initial_letter), permuted_sequence):
                # # an anagram needs to be an existent and real word
                if term in real_words:
                    dict_with_words_by_initial[initial_letter].append(term)

            # print(f'5 - Debugging finished for words that starts with the letter of main_word: {initial_letter} in position: {e}')
        return dict_with_words_by_initial

    def _is_palindrome(self, any_word: str) -> bool:
        """
        :return: if any_word is palindrome or not
        """
        return any_word == any_word[-1::-1]

    def _get_permutation_word_sequence(self, any_word: str, custom_lower_case=True) -> list:
        """
        :param any_word: any single word
        :param custom_lower_case: True by default. It is better to validate if the custom_lower_case argument is always True
        :return: All sequences possible of any_word
        """
        # Generate all permutations (all sequences possible for each letter of a word)
        list_of_sequences_possible = list(permutations(any_word))

        # Creates each word joining each sequence generated
        words = [''.join(sequenced_word) for sequenced_word in list_of_sequences_possible]

        #
        if custom_lower_case:
            return [w.lower() for w in words]
        else:
            return words

    def _loads_pt_and_en_words_dictonary(self) -> List[List[str]]:
        """ If the files don't exist yet, it requests the contents and save them
        :return: This method loads two lists containing portuguese and english words from dictionary.
        """
        destination_files = ["br-utf8.txt", 'en-words.txt']

        urls = ["https://www.ime.usp.br/~pf/dicios/br-utf8.txt",
                "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"]
        en_with_pt_lists = []

        for destination_file, url in zip(destination_files, urls):
            try:
                with open(destination_file, 'r') as file:
                    en_with_pt_lists.append([val.lower().replace('\n', '') for val in file.readlines()])

            except FileNotFoundError:
                response = requests.get(url)
                content = response.content.decode("utf-8")
                content_list = content.split('\n')

                if destination_file == 'en-words.txt':
                    # omg, the racecar word is not yet on this txt
                    content_list.insert(content_list.index('racecard'), 'racecar')

                with open(destination_file, "w") as file:
                    file.write("\n".join(content_list))

                en_with_pt_lists.append([val.lower() for val in content_list])

        return en_with_pt_lists


if __name__ == '__main__':
    desafio = Desafios()
    desafio_01 = desafio.reverse_phrase_part_1('Hello, World! OpenAI is amazing!')
    print()

    desafio_02 = desafio.remove_duplicated_characters('Hello, World!')
    desafio_02_extra = desafio.remove_duplicated_characters('Sem caracteres duplicados!')
    print()

    desafio_03 = desafio.find_largest_palindrome_substring('babad')
    desafio_03_extra_1 = desafio.find_largest_palindrome_substring('babaddalalalana ana')
    desafio_03_extra_2 = desafio.find_largest_palindrome_substring('hello world ana ama')
    print()

    desafio_04 = desafio.capitalize_phrasal_strings("hello. how are you? i'm fine, thank you")
    print()

    for word in ['racecar', 'Alegria', 'Amor', 'osso']:
        desafio_05_output = desafio.is_anagram_of_palindrome(word)
        print(f'Is {word} an anagram of palindrome? ',end='')
        if desafio_05_output:
            print('\033[1;32m', desafio_05_output, '\033[1;31m')
        else:
            print('\033[1;31m', desafio_05_output, '\033[1;31m')

    print('debuging')
