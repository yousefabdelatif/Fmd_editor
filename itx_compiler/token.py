from enum import Enum
from abc import ABC,abstractmethod
from xml.sax.handler import property_dom_node

from itx_compiler.tokens.Formats import  Tokens



class Token:

    def __init__(self,type:str,parent=None):
        self.type:str=type
        self.parentToken:Token=parent
        self.children:list=[]
    def apply(self)->str:
        action = self.type
        children_actions = ""
        for token in self.children:children_actions =children_actions+(token.apply())

        if len(self.children) == 0: action =action.replace("$$$$", "")

        return action.replace("$$$$",children_actions)

    def addChild(self,token):
        self.children.append(token)

class TokenTree:
    def __init__(self,seedToken:Token):
        self.__currentToken:Token=seedToken
        self.__depth:int=0

    def insert(self, tag:str):
        match (tag):
            case "<page>":
                self.__currentToken.addChild(token=Token(Tokens.PAGE_TAG, parent=self.__currentToken ))
        pass
    def goUforward(self):
        self.__depth =self.__depth+1
        self.__currentToken=self.__currentToken.children[-1]
        pass
    def gobackward(self):
        if self.__currentToken.type != Tokens.DOC_TAG:
            self.__depth =self.__depth-1
            self.__currentToken=self.__currentToken.parentToken






