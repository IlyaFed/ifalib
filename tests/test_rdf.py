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

def test_rdf_one_and_many_steps():
    rcut=13.0
    cell=26.4
    nbins=100
    Npart=200
    Nsteps=10
    # data = [[26*i/Npart,26*i/Npart,26*i/Npart] for i in range(Npart)]
    # coord1 = [ [[26*i/Npart,26*i/Npart,26*i/Npart] for i in range(Npart)] for step in range(Nsteps) ]
    # coord2 = [ [[26*i/Npart,26*i/Npart,26*i/Npart] for i in range(Npart)] for step in range(Nsteps) ]
    data = [[cell*random.random(),cell*random.random(),cell*random.random()] for i in range(Npart)]
    coord1 = [  data for step in range(Nsteps) ]
    # coord2 = [ [[cell*random.random(),cell*random.random(),cell*random.random()] for i in range(Npart)] for step in range(Nsteps) ]
    
    # bins, rdf_py = rdf.rdf_one_type_one_step_python(data, cell, rcut, nbins)
    bins, rdf_c = rdf.rdf_one_type_one_step(data, cell, rcut, nbins)
    bins, rdf_steps = rdf.rdf_two_types_many_steps(coord1, coord1, cell, rcut, nbins)

    error=0
    for i in range(nbins):
        # error+= (rdf_py[i]-rdf_py[i])**2
        error+= (rdf_c[i]-rdf_steps[i])**2
    assert (error**0.5 < 0.5)

def test_rdf_many_steps():
    rcut=13.0
    cell=26.4
    nbins=100
    Npart=500
    Nsteps=400
    # data = [[26*i/Npart,26*i/Npart,26*i/Npart] for i in range(Npart)]
    # coord1 = [ [[26*i/Npart,26*i/Npart,26*i/Npart] for i in range(Npart)] for step in range(Nsteps) ]
    # coord2 = [ [[26*i/Npart,26*i/Npart,26*i/Npart] for i in range(Npart)] for step in range(Nsteps) ]
    coord1 = [ [[cell*random.random(),cell*random.random(),cell*random.random()] for i in range(Npart)] for step in range(Nsteps) ]
    coord2 = [ [[cell*random.random(),cell*random.random(),cell*random.random()] for i in range(Npart)] for step in range(Nsteps) ]
    
    bins, rdf_steps = rdf.rdf_two_types_many_steps(coord1, coord1, cell, rcut, nbins)

    assert (True)