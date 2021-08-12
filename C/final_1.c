#include <stdio.h>

void impostor(int cant,int impostor[]){

    for(int i=0;i<cant;i++){
        int asesinatos;
        printf("\nIngrese la cantidad de asesinatos en la partida %i: ",(i+1));
        scanf(" %i",impostor[i]);
    }
    for(int i=0;i<cant;i++){
        printf("\nJuego %d - %d asesinatos.\n",(i+1),impostor[i]);
    }
}

void tripulante(int cant_t,int tripulante[]){
    for(int i=0;i<cant_t;i++){
        int asesinatos;
        printf("\nIngrese la cantidad de muertes en la partida %i: ",(i+1));
        scanf(" %i",asesinatos);
        tripulante[i] -> asesinatos;
    }

    for(int i=0;i<cant_t;i++){
        printf("\nJuego %d - %d muertes.\n",(i+1),tripulante[i]);
    }
}

int main(){
    int cant_i,cant_t;
    printf("\nIngrese la cantidad de partidas en las cuales fue impostor: ");
    scanf(" %d",&cant_i);

    printf("\nIngrese la cantidad de partidas en las cuales fue tripulante: ");
    scanf(" %d",&cant_t);

    int impostorr[cant_i] = {1};

    impostor(cant_i,impostorr);

    int tripu[cant_t] = {0};

    tripulante(cant_t,tripu);



    return 0;
}
//Asesinados totales / ( Nº de veces de tripulante - Nº de veces que murió).
//2) Utilizar mas de 2 funciones y/o procedimientos.