from sys import maxunicode
from ifalib import neighbour


def test_neighbour():
    coord = [[[0,0,0],[1,1,1]] for step in range(5)] 
    types = ['H', 'H']
    cell=10.0
    rcut=5.0
    maxunique = 2

    returned_dict= neighbour.neighbour(coord, types, cell, rcut, maxunique)
    # print (returned_dict)
    print (returned_dict)
    assert (len(returned_dict)>0)
    

def test_h_h2_structures():
    Rcut = 1.0
    Cell = 20.0
    dCell = 2.0
    Nsteps = 2
    Maxunique = 10
    NinCell = int(Cell/dCell)
    Npart = int(NinCell**3*1.5)
    Coords = []
    Types = []
    for step in range(Nsteps):
        Coord_point = []
        Types =[]
        for xi in range(NinCell):
            for yi in range(NinCell):
                for zi in range(NinCell):
                    # H-H distance 0.75, about (0.2^2+0.2^2+0.2^2) x 2
                    Coord_point.append([xi*dCell + 0.2, yi*dCell + 0.2, zi*dCell + 0.2])
                    Types.append("H")
                    if (len(Coord_point) > int(Npart/3)):
                        Coord_point.append([xi*dCell - 0.2, yi*dCell - 0.2, zi*dCell - 0.2])
                        Types.append("H")
        Coords.append(Coord_point)
    
    returned_dict = neighbour.neighbour(Coords, Types, Cell, Rcut, Maxunique)
    print (returned_dict)
    assert(returned_dict['H1']['count_of_molecules'][0]==Npart/3)
    assert(returned_dict['H2']['count_of_molecules'][0]==Npart/3)
    number_of_determined_particles = 0
    for key in returned_dict:
        number_of_determined_particles += returned_dict[key]['count_of_particles'][0]
    assert(number_of_determined_particles == Npart)

def test_h_h2_h3_h4_structures():
    Rcut = 1.0
    Cell = 20.0
    dCell = 2.0
    Nsteps = 2
    Maxunique = 10
    NinCell = int(Cell/dCell)
    Npart = int(NinCell**3*1.5)+3
    Coords = []
    Types = []
    for step in range(Nsteps):
        Coord_point = []
        Types = []
        for xi in range(NinCell):
            for yi in range(NinCell):
                for zi in range(NinCell):
                    # H-H distance 0.75, about (0.2^2+0.2^2+0.2^2) x 2
                    # H1
                    Coord_point.append([xi*dCell + 0.2, yi*dCell + 0.2, zi*dCell + 0.2])
                    Types.append("H")
                    # H2
                    if (len(Coord_point) > (Npart-3)/3):
                        Coord_point.append([xi*dCell - 0.2, yi*dCell - 0.2, zi*dCell - 0.2])
                        Types.append("H")
                    # H3
                    if (len(Coord_point) >= Npart - 5):
                        # print ("here1")
                        Coord_point.append([xi*dCell + 0.2, yi*dCell - 0.2, zi*dCell - 0.2])
                        Types.append("H")
                    # H4
                    if (len(Coord_point) == Npart-1):
                        # print ("here2")
                        Coord_point.append([xi*dCell - 0.2, yi*dCell - 0.2, zi*dCell + 0.2])
                        Types.append("H")
        # print ("Numbers" , len(Coord_point), Npart)
        Coords.append(Coord_point)


    returned_dict = neighbour.neighbour(Coords, Types, Cell, Rcut, Maxunique)
    print (returned_dict)
    assert(returned_dict['H1']['count_of_molecules'][0]==(Npart-3)/3)
    assert(returned_dict['H2']['count_of_molecules'][0]==(Npart-3)/3-2)
    assert(returned_dict['H3']['count_of_molecules'][0]==1)
    assert(returned_dict['H4']['count_of_molecules'][0]==1)
    number_of_determined_particles = 0
    for key in returned_dict:
        number_of_determined_particles += returned_dict[key]['count_of_particles'][0]
    assert(number_of_determined_particles == Npart)

def test_h_h2_e_structures():
    Rcut = 1.0
    Cell = 20.0
    dCell = 2.0
    Nsteps = 2
    Maxunique = 10
    NinCell = int(Cell/dCell)
    Npart = int(NinCell**3*1.5)*2
    Coords = []
    Types = []
    for step in range(Nsteps):
        Coord_point = []
        Types =[]
        for xi in range(NinCell):
            for yi in range(NinCell):
                for zi in range(NinCell):
                    # H-H distance 0.75, about (0.2^2+0.2^2+0.2^2) x 2
                    Coord_point.append([xi*dCell + 0.2, yi*dCell + 0.2, zi*dCell + 0.2])
                    Types.append("H")
                    Coord_point.append([xi*dCell + 0.1, yi*dCell + 0.1, zi*dCell + 0.1])
                    Types.append("e")
                    if (len(Coord_point) > int(Npart/3)):
                        Coord_point.append([xi*dCell - 0.2, yi*dCell - 0.2, zi*dCell - 0.2])
                        Types.append("H")
                        Coord_point.append([xi*dCell - 0.1, yi*dCell - 0.1, zi*dCell - 0.1])
                        Types.append("e")
        Coords.append(Coord_point)
    
    returned_dict = neighbour.neighbour(Coords, Types, Cell, Rcut, Maxunique)
    print (returned_dict)
    assert(returned_dict['H1 e1']['count_of_molecules'][0]==Npart/2/3)
    assert(returned_dict['H2 e2']['count_of_molecules'][0]==Npart/2/3)
    number_of_determined_particles = 0
    for key in returned_dict:
        number_of_determined_particles += returned_dict[key]['count_of_particles'][0]
    assert(number_of_determined_particles == Npart)