from itx_compiler.token import Token
from itx_compiler.tokens.Formats import *


class page_t(Token):
    def __init__(self,children:Token):
        self.children:list[Token]=children


    def apply(self) -> str:
        action =Tokens.PAGE_TAG
        children_action=""
        for token in self.children:
            children_action.join(token.apply())
        action.replace("<$>",children_action)
        return action

