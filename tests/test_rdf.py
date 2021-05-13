from ifalib import rdf
import random

def test_rdf_one_type_one_step_python():
    data = [[0,0,0],[1,1,1]]
    cell=10.0
    rcut=5.0
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]

    bins, rdf_data = rdf.rdf_one_type_one_step_python(data, cell, rcut, nbins)
    flag=0
    for i in range(nbins):
        if not ( (i == 34) and (rdf_data[i]>0) ):
            flag += rdf_data[i]
    assert (flag==0)

def test_rdf_one_type_one_step():
    data = [[0,0,0],[1,1,1]]
    cell=10.0
    rcut=5.0
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]

    bins, rdf_data = rdf.rdf_one_type_one_step(data, cell, rcut, nbins)
    # print (rdf_data)
    flag=0
    for i in range(nbins):
        if not ( (i == 34) and (rdf_data[i]>0) ):
            flag += rdf_data[i]
    assert (flag==0)

def test_rdf_two_types_many_steps():
    coord1 = [[[0,0,0],[1,1,1]] for step in range(5)] 
    coord2 = [[[0,0,0],[1,1,1]] for step in range(5)]
    data = [[0,0,0],[1,1,1]]
    cell=10.0
    rcut=5.0
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]

    bins, rdf_data = rdf.rdf_two_types_many_steps(coord1, coord2, cell, rcut, nbins)
    bins, rdf_data_one = rdf.rdf_one_type_one_step(data, cell, rcut, nbins)
    # print (rdf_data)
    flag=0
    for i in range(nbins):
        if not ( (i == 34) and (rdf_data[i]>0) ):
            flag += rdf_data[i]
    if not (rdf_data[34]-rdf_data_one[34] < 0.01):
        flag +=1
    assert (flag==0)

def test_rdf_all():
    data = [[26*i/100,26*i/100,26*i/100] for i in range(50)]
    coord1 = [ [[26*i/100,26*i/100,26*i/100] for i in range(50)] for step in range(50) ]
    coord2 = [ [[26*i/100,26*i/100,26*i/100] for i in range(50)] for step in range(50) ]
    print(data)
    rcut=13.0
    cell=26.4
    nbins=100
    dbins=rcut/nbins
    bins=[dbins/2+i*dbins for i in range(nbins)]
    
    bins, rdf_py = rdf.rdf_one_type_one_step_python(data, cell, rcut, nbins)
    bins, rdf_c = rdf.rdf_one_type_one_step(data, cell, rcut, nbins)
    bins, rdf_steps = rdf.rdf_two_types_many_steps(coord1, coord2, cell, rcut, nbins)

    error=0
    for i in range(nbins):
        error+= (rdf_py[i]-rdf_py[i])**2
        error+= (rdf_py[i]-rdf_steps[i])**2
    assert (error**0.5 < 0.5)