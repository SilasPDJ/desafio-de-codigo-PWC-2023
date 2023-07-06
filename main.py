class Desafios:
    title = "Phrase (before and after):"

    def reverse_phrase_part_1(self, string_phrase: str) -> str:
        """ outputs string_phrase as it is and reversed, finally returns it reversed
        :param string_phrase: any string text
        :return: reversed phrase keeping letters' ordering
        """
        revered_phrase = " ".join(string_phrase.split()[-1::-1])

        print(f"{self.title} {string_phrase}")
        print(f"{' ' * (len(self.title) - 1)}: {revered_phrase}")

        return revered_phrase


if __name__ == '__main__':
    desafio = Desafios()
    desafio_01 = desafio.reverse_phrase_part_1('Hello, World! OpenAI is amazing!')

    print('debuging')

