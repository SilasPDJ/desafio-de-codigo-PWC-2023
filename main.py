class Desafios:
    title = "Phrase (before and after):"

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
        """ outputs only the palindromes and the largest one that is the substring that will be returned
        :param string_phrase: any string text
        :return: the largest palindrome in the string_phrase passed by parameter if it exists, else an empty string
        """
        words_list = string_phrase.split()
        words_list_in_reverse = [word[-1::-1] for word in words_list]
        palindrome_words = [word for e, word in enumerate(words_list_in_reverse) if word.upper() == words_list[e].upper()]

        # finding palindrome in any place of a word
        palindrome_word_found_list = {}
        for word in words_list:

            # The minimum number of letters possible for palindromes is 3
            if len(word) < 3:
                continue

            # find palindromes
            palindrome_word_found_list[word] = []
            for start_index in range(len(word)):
                # i + 3 because the minimum number of letters possible for palindromes is 3
                for end_index in range(start_index + 3, len(word)+1):
                    term = word[start_index:end_index]
                    if term == term[::-1] and term not in palindrome_word_found_list:
                        palindrome_word_found_list[word].append(term)

        if palindrome_words:
            print("Ex.3) Find Largest palindrome word")
            largest_palindrome_substring = max(palindrome_words)
            print(f"{self.title} {palindrome_words}")
            print(f"{' ' * (len(self.title) - 1)}: {largest_palindrome_substring}")

            return largest_palindrome_substring

        # palindrome_words list could be empty
        return ''


if __name__ == '__main__':
    desafio = Desafios()
    desafio_01 = desafio.reverse_phrase_part_1('Hello, World! OpenAI is amazing!')

    desafio_02 = desafio.remove_duplicated_characters('Hello, World!')
    desafio_02_extra = desafio.remove_duplicated_characters('Sem caracteres duplicados!')

    desafio_03_extra_1 = desafio.find_largest_palindrome_substring('babaddalalalana')
    desafio_03 = desafio.find_largest_palindrome_substring('babad')
    desafio_03_extra_2 = desafio.find_largest_palindrome_substring('hello world anna natan')

    print('debuging')

