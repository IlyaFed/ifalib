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
        for xi in range(NinCell):
            for yi in range(NinCell):
                for zi in range(NinCell):
                    # H-H distance 0.75, about (0.2^2+0.2^2+0.2^2) x 2
                    Coord_point.append([xi*dCell + 0.2, yi*dCell + 0.2, zi*dCell + 0.2])
                    Types.append("H")
                    if (len(Coord_point) > Npart/3):
                        Coord_point.append([xi*dCell - 0.2, yi*dCell - 0.2, zi*dCell - 0.2])
                        Types.append("H")
        Coords.append(Coord_point)
    
    returned_dict = neighbour.neighbour(Coords, Types, Cell, Rcut, Maxunique)
    print (returned_dict)
    assert(returned_dict['H1']['count'][0]==Npart/3)
    assert(returned_dict['H2']['count'][0]==Npart/3)