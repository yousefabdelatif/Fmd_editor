import re

from matplotlib.pyplot import switch_backend

from itx_compiler.token import Token, TokenTree
from itx_compiler.tokens.Formats import Tokens


class Itx_Compiler:
    def __init__(self):
        self.__template: str
        self.__output: str
        self.__seedToken: Token = Token(Tokens().DOC_TAG)
        self.__tokenTree: TokenTree = TokenTree(seedToken=self.__seedToken)

    def compile(self, src: str) -> [bool, str]:

        self.__lexing(seq_tags=self.parse(src=src))
        print(self.__seedToken.apply())
        return self.__seedToken.apply()

    # this take list of parsed elements from the code
    def __lexing(self, seq_tags: []):
        a_tag_already_open: bool = False
        last_open_tag: str = ""
        depth: int = 0
        for elem in seq_tags:
            if (elem[0]) == "<" and elem[1] != "/":

                if a_tag_already_open:
                    depth = depth + 1
                    last_open_tag = elem
                    self.__tokenTree.insert(elem)
                    self.__tokenTree.goUforward()

                else:
                    a_tag_already_open = True
                    self.__tokenTree.insert(elem)
                    self.__tokenTree.gobackward()


            elif elem[:2] == "</":
                if last_open_tag == elem:
                    a_tag_already_open = False
                else:
                    last_open_tag = elem
                self.__tokenTree.gobackward()





            else:
                self.preprocessing(elem)

    # parse the code
    def parse(self, src: str):
        return re.findall(r'@.*?\+|@.*?\(.*?\)', src)

    def preprocessing(self, src: str) -> str:
        print(re.findall(r"@.*?\(.*?\)", src))
