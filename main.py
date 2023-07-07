import re
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
                for end_index in range(start_index + 3, len(word)+1):
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
        """
        :param string_phrase:
        :return:
        """
        pattern = r'([.?!]\s*\w)'
        def sets_repl(match: re.Match): return match.group(1).upper()

        capitalized_string_phrase = string_phrase.capitalize()
        capitalized_string_phrase = re.sub(pattern, sets_repl, capitalized_string_phrase)

        print("Ex.3) Find Largest palindrome word")

        return capitalized_string_phrase


if __name__ == '__main__':
    desafio = Desafios()
    desafio_01 = desafio.reverse_phrase_part_1('Hello, World! OpenAI is amazing!')

    desafio_02 = desafio.remove_duplicated_characters('Hello, World!')
    desafio_02_extra = desafio.remove_duplicated_characters('Sem caracteres duplicados!')

    desafio_03 = desafio.find_largest_palindrome_substring('babad')
    desafio_03_extra_1 = desafio.find_largest_palindrome_substring('babaddalalalana ana')
    desafio_03_extra_2 = desafio.find_largest_palindrome_substring('hello world ana ama')

    desafio_04 = desafio.capitalize_phrasal_strings("hello. how are you? i'm fine, thank you")
    print('debuging')

