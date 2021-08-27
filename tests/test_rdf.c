#include "../ifalib/rdf.c"

int main(){
    double rcut=40.0, cell=26.4;
    int nbins=100;
    int Npart=1000, Nsteps=1;
    double * coord1 = calloc(Npart*Nsteps*3, 0);
    double * coord2 = calloc(Npart*Nsteps*3, 0);
    for (int step=0; step< Nsteps; step++)
        for (int idp=0; idp<Npart; idp++){
            coord1[step*Npart*3+idp*3+0] = cell*idp/Npart;
            coord1[step*Npart*3+idp*3+1] = cell*idp/Npart;
            coord1[step*Npart*3+idp*3+2] = cell*idp/Npart;
            coord2[step*Npart*3+idp*3+0] = cell*idp/Npart;
            coord2[step*Npart*3+idp*3+1] = cell*idp/Npart;
            coord2[step*Npart*3+idp*3+2] = cell*idp/Npart;
        }
    double *g_r = malloc(nbins);
    rdf(nbins, rcut, g_r, Npart, Npart, Nsteps, coord1, coord2, cell);
    return 0;
}