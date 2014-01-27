from nutils import *

@util.withrepr
def SchwarzP ( ndims, L, t, inverse ):
  assert ndims in [2,3] and L > 0.
  L = float(L)
  lvl = lambda x : function.cos(2.*numpy.pi*x[0]/L)+function.cos(2.*numpy.pi*x[1]/L)-1-t if ndims==2 else function.cos(2.*numpy.pi*x[0]/L)+function.cos(2.*numpy.pi*x[1]/L)+function.cos(2.*numpy.pi*x[2]/L)-t
  return lvl if not inverse else lambda x: -lvl(x)                  

@util.withrepr
def Gyroid ( L, t, inverse ):
  L = float(L)
  lvl = lambda x : function.sin(2.*numpy.pi*x[0]/L)*function.cos(2.*numpy.pi*x[1]/L) + \
                   function.sin(2.*numpy.pi*x[1]/L)*function.cos(2.*numpy.pi*x[2]/L) + \
                   function.sin(2.*numpy.pi*x[2]/L)*function.cos(2.*numpy.pi*x[0]/L) - t
  return lvl if not inverse else lambda x: -lvl(x)                  
