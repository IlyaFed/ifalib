import os
import ctypes 

# Загрузка библиотеки
basedir = os.path.abspath(os.path.dirname(__file__))
libpath = os.path.join(basedir, 'librdf.so')
rdf_ctypes = ctypes.CDLL(libpath)

def rdf_c(r_list, cell, rcut,nbins):
    x_c_double=(ctypes.c_double * len(r_list)) ()
    y_c_double=(ctypes.c_double * len(r_list)) ()
    z_c_double=(ctypes.c_double * len(r_list)) ()
    g_r_c_double = (ctypes.c_double * nbins) ()
    for i in range(len(r_list)):
        x_c_double[i]=r_list[i][0]
        y_c_double[i]=r_list[i][1]
        z_c_double[i]=r_list[i][2]

    rdf_ctypes.rdf.restype = ctypes.c_double #ctypes.POINTER(ctypes.c_double) # * nbins) #ctypes.c_int #
    rdf_ctypes.rdf.argtypes = [ctypes.POINTER(ctypes.c_double),
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.POINTER(ctypes.c_double), 
                               ctypes.c_int, ctypes.c_double, ctypes.c_double,ctypes.c_int]
    rdf_c_double=rdf_ctypes.rdf(g_r_c_double, x_c_double,y_c_double,z_c_double,len(r_list),cell, rcut, nbins)
    return list(g_r_c_double)

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


def read_file(filename):
    f = open(filename,"r")
    N=int(f.readline())
    f.readline()
    id_r_list=[]
    r_list=[]
    for i in range(N):
        line=f.readline()
        id_x=line.split()[0]
        if id_x == '1':
            r_list.append([float(item) for item in line.split()[1:]])
    return r_list

def test_rdf():
    data = read_file("intlib/test.xyz")
    rcut=13.0
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]
    cell=26.540779

    import intlib.rdf as rdflib
    rdf_py = rdflib.rdf_python(data, cell, rcut, nbins)
    rdf_c = rdflib.rdf_c(data, cell, rcut, nbins)

    error=0
    for i in range(nbins):
        error+= (rdf_py[i]-rdf_c[i])**2

    if (error < 0.5):
        print ("rdf: OK")
        return 0
    else:
        print ("rdf: Error")
        quit()
    
if __name__ == '__main__':
    test_rdf()