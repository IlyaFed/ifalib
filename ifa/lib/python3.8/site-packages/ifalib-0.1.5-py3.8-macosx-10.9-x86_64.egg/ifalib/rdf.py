import os, glob
import ctypes 

# Загрузка библиотеки
basedir = os.path.abspath(os.path.dirname(__file__))
libpath = os.path.join(basedir, 'librdf*.so')
libpath = glob.glob(libpath)[0]
rdf_ctypes = ctypes.CDLL(libpath)

def rdf_c(r_list, cell, rcut,nbins):
    Rpart1_c_double=(ctypes.c_double * (len(r_list)*3)) ()
    Rpart2_c_double=(ctypes.c_double * (len(r_list)*3)) ()
    rdf_c_double = (ctypes.c_double * nbins) ()
    for i in range(len(r_list)):
        for j in range(3):
            Rpart1_c_double[i*3+j]=r_list[i][j]
            Rpart2_c_double[i*3+j]=r_list[i][j]
    rdf_ctypes.rdf.restype = ctypes.c_int
    rdf_ctypes.rdf.argtypes = [ctypes.c_int, ctypes.c_double,
                               ctypes.POINTER(ctypes.c_double),
                               ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.c_double]
    rdf_ctypes.rdf(nbins, rcut, rdf_c_double, len(r_list), len(r_list), len(r_list), 1,
                                Rpart1_c_double,Rpart2_c_double,cell)
    return list(rdf_c_double)

def get_nearest_axes(r1,r2,cell):
    dx = r2-r1
    c = int(dx/cell)
    dx = dx - c * cell
    if abs(dx-cell) < abs(dx):
        dx=dx-cell
        
    return dx

def rdf_python(r_list, cell, rcut,nbins):
    N=len(r_list)
    rho = N/cell**3
    l_list=[]
    naveraged=0
    for i in range(N):
        for j in range(N):
            r1=r_list[i]
            r2=r_list[j]
            l_r=0
            for l in range(3):
                l_r +=get_nearest_axes(r1[l],r2[l], cell)**2
            l_r = l_r**0.5
            if (l_r > 0) and (l_r < rcut):
                l_list += [l_r]#get_distances(r1, r2, cell, rcut)
            
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]
    counts = [0 for i in range(nbins)]
    for l in l_list:
        counts[ int(l/dbins) ] += 1
    g_r=[]
    for index in range(len(counts)):
        g_r.append(1.0*(counts[index]/( 4*3.14*(bins[index]**2)*dbins) / rho / N))
    return g_r
