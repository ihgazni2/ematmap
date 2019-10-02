.. contents:: Table of Contents
   :depth: 5


*ematmap*
------------



Installation
============

    ::
    
        $ pip3 install ematmap

Usage
=====
    
    ::
        
        import ematmap.ematmap as emem

APIS
~~~~

- mapf
- mapx
- mapy
- mapv
- mapo
- mapfx
- mapfy
- mapfv
- mapfo
- mapxy
- mapxv
- mapxo
- mapyv
- mapyo
- mapvo
- mapfxy
- mapfxv
- mapfxo
- mapfyv
- mapfyo
- mapfvo
- mapxyv
- mapxyo
- mapxvo
- mapyvo
- mapfxyv
- mapfxyo
- mapfxvo
- mapfyvo
- mapxyvo
- mapfxyvo


LEVEL0 API
~~~~~~~~~~

- def init_mat(layer_length_list,**kwargs):
- def append_non_empty_lyr(layer,m):
- def append_ele_at_depth(depth,ele,m):
- def get_matsize(m):
- def get_maxlyrlen(m):
- def get_maxlenlyr_depth(m,*args):
- def get_maxlenlyr(m,*args):
- def xy2loc(x,y):
- def xy2ele(x,y,m):
- def loc2ele(loc,m):
- def xyset(x,y,value,m):
- def locset(loc,value,m):


License
=======

- MIT
