from ifalib import rdf

def test_rdf_python():
    data = [[0,0,0],[1,1,1]]
    cell=10.0
    rcut=5.0
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]

    rdf_data = rdf.rdf_python(data, cell, rcut, nbins)
    flag=0
    for i in range(nbins):
        if not ( (i == 34) and (rdf_data[i]>0) ):
            flag += rdf_data[i]
    assert (flag==0)

def test_rdf_c():
    data = [[0,0,0],[1,1,1]]
    cell=10.0
    rcut=5.0
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]

    rdf_data = rdf.rdf_c(data, cell, rcut, nbins)
    print (rdf_data)
    flag=0
    for i in range(nbins):
        if not ( (i == 34) and (rdf_data[i]>0) ):
            flag += rdf_data[i]
    assert (flag==0)

def test_rdf():
    data = [[i*2,i**2,i**3/4] for i in range(100)]
    rcut=13.0
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]
    cell=26.540779

    rdf_py = rdf.rdf_python(data, cell, rcut, nbins)
    rdf_c = rdf.rdf_c(data, cell, rcut, nbins)

    error=0
    for i in range(nbins):
        error+= (rdf_py[i]-rdf_c[i])**2
    assert (error < 0.5)

# test_rdf_c()