from pathlib import  Path

from numpy.ma.testutils import assert_equal

from itx_compiler.itx_compiler import Itx_Compiler
def test_parsecode():
    instance= Itx_Compiler()
    assert_equal(instance.parse("<page></page>"),["<page>","</page>"])
    assert_equal(instance.parse("<page><page><page></page><page></page></page><page></page></page>"),["<page>","<page>","<page>","</page>","<page>","</page>","</page>","<page>","</page>","</page>"])
def test_lexing():
    instance= Itx_Compiler()

    assert  instance.compile("<page><page><page><page></page><page><page></page></page><page>")=="""<div class="doc-tag"> <div class="page-tag">  </div><div class="page-tag"> <div class="page-tag"> <div class="page-tag">  </div><div class="page-tag"> <div class="page-tag">  </div> </div><div class="page-tag">  </div> </div> </div> </div>"""

