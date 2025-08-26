from enum import Enum
from itx_compiler.token import Token
class Elements(Enum):
    DOC_TAG= '<div class="doc-tag"> $$$$ </div>'
    IMAGE_TAG='<div class="doc-tag"> $$$$ </div>'
    PAGE_TAG = '<div class="page-tag"> $$$$ </div>'
    SECTION_TAG='<div class="doc-tag"> $$$$ </div>'
    ROW_TAG='<div class="doc-tag"> $$$$ </div>'
    COULMN_TAG='<div class="doc-tag"> $$$$ </div>'


class Tokens:
    tags:{}
    def resolve(self,elem:str,parent:Token)->[Token,str]:
        match (elem):
            case "<page>":
                if parent.type != Elements.DOC_TAG:
                    return None, "this component in not a valid parent for page elem "
                else:
                    return Token(Tokens.PAGE_TAG, parent=parent),"all tags resolved correctly"

            case "<doc>":

                if parent != None:
                    return None, "Doc element should be the parent element of all elemets"
                else:
                    return Token(Tokens.DOC_TAG, parent=parent), "all tags resolved correctly"

            case "<section>":
                if parent.type != Elements.PAGE_TAG:
                    return None, "A Section element should be a child of a page element"
                else:
                    return Token(Tokens.SECTION_TAG, parent=parent), "all tags resolved correctly"

            case "<row>":
                return Token(Tokens.ROW_TAG,parent=parent) ,"all tags resolved correctly"
            case "<coulmn>":
                return Token(Tokens.COULMN_TAG, parent=parent),"all tags resolved correctly"
            case _:
                return None,"error" +elem+"is not a Valid tag"

