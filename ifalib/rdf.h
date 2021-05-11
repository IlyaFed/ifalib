#ifndef _CTYPES_H_
#define _CTYPES_H_

#ifdef  __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <unistd.h>
#include <math.h>
#include <stdlib.h>

int get_nearests(double x1, double x2, double cell, double rcut);
int get_distances(double * r1, double * r2, double cell, double rcut);
int rdf(int nbins, double rcut, double * g_r, int Npart1, int Npart2, int Nrho, int Nsteps, double * Rpart1, double * Rpart2, double cell);

#ifdef  __cplusplus
}
#endif

#endif  /* _CTYPES_H_ */