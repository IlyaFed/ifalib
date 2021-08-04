#include "../ifalib/neighbour.c"
#include <stdlib.h>
#include <time.h>

int test_h2_structures(){
    double Rcut=1.0;
    double Cell=20.0;
    double dCell=2.0;
    int Nsteps=2;
    int NinCell=(int) Cell/dCell;
    int Npart = pow(NinCell, 3)*2; // because H2 has two molecules
    struct  SystemState sysState;
    sysState.types = (int *) malloc (sizeof(int)*Npart);
    sysState.Npart = Npart;
    sysState.r = (double *) malloc (sizeof(double)*Npart*3*Nsteps);
    sysState.cell = Cell;
    sysState.maxtypes = 1;
    sysState.Nsteps = Nsteps;
    for (int step=0; step< Nsteps; step++){
        int idp=0;
        for (int xi=0; xi < NinCell; xi++)
            for (int yi=0; yi < NinCell; yi++)
                for (int zi=0; zi < NinCell; zi++){
                    // H-H distance 0.75, about (0.2^2+0.2^2+0.2^2) x 2
                    sysState.r[step*Npart*3 + idp*3+0] = dCell*xi + 0.2;
                    sysState.r[step*Npart*3 + idp*3+1] = dCell*yi + 0.2;
                    sysState.r[step*Npart*3 + idp*3+2] = dCell*zi + 0.2;
                    sysState.types[idp] = 0;
                    idp++;
                    sysState.r[step*Npart*3 + idp*3+0] = dCell*xi - 0.2;
                    sysState.r[step*Npart*3 + idp*3+1] = dCell*yi - 0.2;
                    sysState.r[step*Npart*3 + idp*3+2] = dCell*zi - 0.2;
                    sysState.types[idp] = 0;
                    idp++;
                }
    }
    
    struct MolsInfo *molsInfo = neighbour(sysState, Rcut, 10);
    printf ("Test H2 molecule: ");
    printf ("step: %d (%s) | ", molsInfo->step, molsInfo->step==Nsteps-1 ? "True" : "False");
    
    printf ("exist: %d (%s) | ", molsInfo->molInfo[0].exist, molsInfo->molInfo[0].exist==1 ? "True" : "False");
    printf ("quantity: %d (%s) | ", molsInfo->molInfo[0].quantityByStep[0], molsInfo->molInfo[0].quantityByStep[0] == Npart/2 ? "True" : "False");
    printf ("nomore: (%s) \n", molsInfo->molInfo[1].exist==0 ? "True" : "False");
    freeMolsInfo(molsInfo);
    return 0;
}

int test_h_h2_structures(){
    double Rcut=1.0;
    double Cell=20.0;
    double dCell=2.0;
    int Nsteps=2;
    int NinCell=(int) Cell/dCell;
    int Npart = pow(NinCell, 3)*1.5; // because H2 has two molecules
    struct  SystemState sysState;
    sysState.types = (int *) malloc (sizeof(int)*Npart);
    sysState.Npart = Npart;
    sysState.r = (double *) malloc (sizeof(double)*Npart*3*Nsteps);
    sysState.cell = Cell;
    sysState.maxtypes = 1;
    sysState.Nsteps = Nsteps;
    for (int step=0; step< Nsteps; step++){
        int idp=0;
        for (int xi=0; xi < NinCell; xi++)
            for (int yi=0; yi < NinCell; yi++)
                for (int zi=0; zi < NinCell; zi++){
                    // H-H distance 0.75, about (0.2^2+0.2^2+0.2^2) x 2
                    sysState.r[step*Npart*3 + idp*3+0] = dCell*xi + 0.2;
                    sysState.r[step*Npart*3 + idp*3+1] = dCell*yi + 0.2;
                    sysState.r[step*Npart*3 + idp*3+2] = dCell*zi + 0.2;
                    sysState.types[idp] = 0;
                    idp++;
                    if (idp > sysState.Npart/3){
                        sysState.r[step*Npart*3 + idp*3+0] = dCell*xi - 0.2;
                        sysState.r[step*Npart*3 + idp*3+1] = dCell*yi - 0.2;
                        sysState.r[step*Npart*3 + idp*3+2] = dCell*zi - 0.2;
                        sysState.types[idp] = 0;
                        idp++;
                    }
                }
    }
    struct MolsInfo* molsInfo = neighbour(sysState, Rcut, 3);
    printf ("Test H2 and H: ");
    printf ("step: %d (%s) | ", molsInfo->step, molsInfo->step==Nsteps-1 ? "True" : "False");
    
    printf ("One exist: %d (%s) | ", molsInfo->molInfo[0].exist, molsInfo->molInfo[0].exist==1 ? "True" : "False");
    printf ("One quantity: %d (%s) | ", molsInfo->molInfo[0].quantityByStep[0], molsInfo->molInfo[0].quantityByStep[0] == (int) Npart/3 ? "True" : "False");
    printf ("Two exist: %d (%s) | ", molsInfo->molInfo[1].exist, molsInfo->molInfo[1].exist==1 ? "True" : "False");
    printf ("Two quantity: %d (%s) | ", molsInfo->molInfo[1].quantityByStep[0], molsInfo->molInfo[1].quantityByStep[0] == (int) Npart/3 ? "True" : "False");
    printf ("nomore: (%s) \n", molsInfo->molInfo[2].exist==0 ? "True" : "False");
    freeMolsInfo(molsInfo);
    return 0;
}

int test_h_structures(){
    double Rcut=1.0;
    double Cell=20.0;
    double dCell=2.0;
    int Nsteps=2;
    int NinCell=(int) Cell/dCell;
    int Npart = pow(NinCell, 3); // because H2 has two molecules
    struct  SystemState sysState;
    sysState.types = (int *) malloc (sizeof(int)*Npart);
    sysState.Npart = Npart;
    sysState.r = (double *) malloc (sizeof(double)*Npart*3*Nsteps);
    sysState.cell = Cell;
    sysState.maxtypes = 1;
    sysState.Nsteps = Nsteps;
    for (int step=0; step< Nsteps; step++){
        int idp=0;
        for (int xi=0; xi < NinCell; xi++)
            for (int yi=0; yi < NinCell; yi++)
                for (int zi=0; zi < NinCell; zi++){
                    // H-H distance 0.75, about (0.2^2+0.2^2+0.2^2) x 2
                    sysState.r[step*Npart*3 + idp*3+0] = dCell*xi + 0.2;
                    sysState.r[step*Npart*3 + idp*3+1] = dCell*yi + 0.2;
                    sysState.r[step*Npart*3 + idp*3+2] = dCell*zi + 0.2;
                    sysState.types[idp] = 0;
                    idp++;
                }
    }
    struct MolsInfo *molsInfo = neighbour(sysState, Rcut, 2);
    printf ("Test H: ");
    printf ("step: %d (%s) | ", molsInfo->step, molsInfo->step==Nsteps-1 ? "True" : "False");
    
    printf ("exist: %d (%s) | ", molsInfo->molInfo[0].exist, molsInfo->molInfo[0].exist==1 ? "True" : "False");
    printf ("quantity: %d (%s) | ", molsInfo->molInfo[0].quantityByStep[0], molsInfo->molInfo[0].quantityByStep[0] == Npart ? "True" : "False");
    printf ("nomore: (%s) \n", molsInfo->molInfo[1].exist==0 ? "True" : "False");
    freeMolsInfo(molsInfo);
    return 0;
}

int test_h_random(){
    srand ( time(NULL) );
    int random_number;
    double Rcut=1.0;
    double Cell=10.0;
    int Nsteps=2;
    int Npart = 10000;
    struct  SystemState sysState;
    sysState.types = (int *) malloc (sizeof(int)*Npart);
    sysState.Npart = Npart;
    sysState.r = (double *) malloc (sizeof(double)*Npart*3*Nsteps);
    sysState.cell = Cell;
    sysState.maxtypes = 1;
    sysState.Nsteps = Nsteps;

    for (int step=0; step< Nsteps; step++){
        for (int idp=0; idp < Npart; idp++){
            random_number = rand();
            sysState.r[step*Npart*3 + idp*3+0] = (float) random_number/ (float) RAND_MAX *Cell;
            random_number = rand();
            sysState.r[step*Npart*3 + idp*3+1] = (float) random_number/ (float) RAND_MAX *Cell;
            random_number = rand();
            sysState.r[step*Npart*3 + idp*3+2] = (float) random_number/ (float) RAND_MAX *Cell;
            sysState.types[idp] = 0;
        }
    }
    struct MolsInfo *molsInfo = neighbour(sysState, Rcut, 4);
    printf ("Test H random: ");
    printf ("step: %d (%s) | ", molsInfo->step, molsInfo->step==Nsteps-1 ? "True" : "False");
    
    printf ("exist: %d (%s) | ", molsInfo->molInfo[0].exist, molsInfo->molInfo[0].exist==1 ? "True" : "False");
    printf ("quantity: %d | ", molsInfo->molInfo[0].quantityByStep[0]);
    int type_id = 0;
    int sum = 0;
    while (molsInfo->molInfo[type_id].exist==1){
        sum += molsInfo->molInfo[type_id].quantityByStep[0];
        type_id++;
    }
    printf ("Sum of nparticles: %d (%s) \n", sum, sum==Npart ? "True" : "False");

    freeMolsInfo(molsInfo);
    return 0;
}

int test_diag_line(){
    double Rcut=0.3, Cell=26.4;
    int Npart=1000, Nsteps=20;

    struct  SystemState sysState;
    sysState.types = (int *) malloc (sizeof(int)*Npart);
    sysState.Npart = Npart;
    sysState.r = (double *) malloc (sizeof(double)*Npart*3*Nsteps);
    sysState.cell = Cell;
    sysState.maxtypes = 1;
    sysState.Nsteps = Nsteps;
    for (int step=0; step< Nsteps; step++){
        for (int idp=0; idp<Npart; idp++){
            sysState.r[step*Npart*3 + idp*3+0] = Cell*idp/Npart;
            sysState.r[step*Npart*3 + idp*3+1] = Cell*idp/Npart;
            sysState.r[step*Npart*3 + idp*3+2] = Cell*idp/Npart;
            sysState.types[idp] = 0;
        }
    }
    struct MolsInfo *molsInfo = neighbour(sysState, Rcut, 10);
    
    printf ("Test random line: ");
    printf ("step: %d | ", molsInfo->step);
    printf ("exist: %d | ", molsInfo->molInfo[0].exist);
    printf ("quantity: %d \n", molsInfo->molInfo[0].quantityByStep[0]);
    freeMolsInfo(molsInfo);
    return 0;
}

int main(){
    // test_h2_structures();
    // test_h_structures();
    // test_h_h2_structures();
    // test_diag_line();
    test_h_random();
    return 0;    
}