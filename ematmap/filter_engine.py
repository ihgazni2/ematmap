import efuntool.efuntool as eftl
import elist.elist as elel
import copy

#MAP

def _get_fo(x,y,**kwargs):
    cond_func = eftl.dflt_kwargs("cond_func",lambda ele:ele,**kwargs)
    other_args = eftl.dflt_kwargs("other_args",[],**kwargs)
    cond_func_mat = eftl.dflt_kwargs("cond_func_mat",None,**kwargs)
    other_args_mat = eftl.dflt_kwargs("other_args_mat",None,**kwargs)
    if(cond_func_mat == None):
        pass
    else:
        cond_func = cond_func_mat[x][y]
    if(other_args_mat == None):
        pass
    else:
        other_args = other_args_mat[x][y]
    return((cond_func,other_args))


def udlr_wrap(func):
    @eftl.deepcopy_wrapper
    def wrapper(m,**kwargs):
        rslt = []
        lngth = len(m)
        for x in range(lngth):
            layer = m[x]
            llen = len(layer)
            for y in range(llen):
                cond_func,other_args = _get_fo(x,y,**kwargs)
                cond = func({
                    "f":cond_func,
                    "x":x,
                    "y":y,
                    "o":other_args,
                    "m":m
                })
                if(cond):
                    rslt.append(m[x][y])
                else:
                    pass
        return(rslt)
    return(wrapper)


def udrl_wrap(func):
    @eftl.deepcopy_wrapper
    def wrapper(m,**kwargs):
        rslt = []
        lngth = len(m)
        for x in range(lngth):
            layer = m[x]
            llen = len(layer)
            for y in range(llen-1,-1,-1):
                cond_func,other_args = _get_fo(x,y,**kwargs)
                cond = func({
                    "f":cond_func,
                    "x":x,
                    "y":y,
                    "o":other_args,
                    "m":m
                })
                if(cond):
                    rslt.append(m[x][y])
                else:
                    pass
        return(rslt)
    return(wrapper)



def dulr_wrap(func):
    @eftl.deepcopy_wrapper
    def wrapper(m,**kwargs):
        rslt = []
        lngth = len(m)
        for x in range(lngth-1,-1,-1):
            layer = m[x]
            llen = len(layer)
            for y in range(llen):
                cond_func,other_args = _get_fo(x,y,**kwargs)
                cond = func({
                    "f":cond_func,
                    "x":x,
                    "y":y,
                    "o":other_args,
                    "m":m
                })
                if(cond):
                    rslt.append(m[x][y])
                else:
                    pass
        return(rslt)
    return(wrapper)


def durl_wrap(func):
    @eftl.deepcopy_wrapper
    def wrapper(m,**kwargs):
        rslt = []
        lngth = len(m)
        for x in range(lngth-1,-1,-1):
            layer = m[x]
            llen = len(layer)
            for y in range(llen-1,-1,-1):
                cond_func,other_args = _get_fo(x,y,**kwargs)
                cond = func({
                    "f":cond_func,
                    "x":x,
                    "y":y,
                    "o":other_args,
                    "m":m
                })
                if(cond):
                    rslt.append(m[x][y])
                else:
                    pass
        return(rslt)
    return(wrapper)





def vfltre(d):
    m = d['m']
    cond_func = d['f']
    other_args = d['o']
    x = d['x']
    y = d['y']
    v = m[x][y]
    ele = cond_func(v,*other_args)
    return(ele)
































