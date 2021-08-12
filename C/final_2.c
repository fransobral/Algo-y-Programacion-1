void evaluando_royos(int royos[], int peso[], int *puntero){

    int id_royo;
    int peso_royo;
    int iterador = 0;
    int ingresar_rollos = 1;
    while(ingresar_rollos == 1){
        puntero++;
        printf("Ingresa por favor el peso del royo ");
        scanf(" %d", &peso_royo);
        printf("Ingrese por favor el id del royo ");
        scanf(" %d", &id_royo);
        royos[iterador]=id_royo;
        peso[iterador]=peso_royo;
        iterador++;

        printf("Marque 1 si desea ingresar mas royos o 2 para finalizar ");
        scanf(" %d", &ingresar_rollos);
    }
}

int main(){

    int ultima_posicion;
    int *puntero_ultima_posicion;
    puntero_ultima_posicion = &ultima_posicion;
    int id_de_rollos[100]={};
    int peso_de_los_rollos[100]={};
    evaluando_royos(id_de_rollos,peso_de_los_rollos, puntero_ultima_posicion);
    return 0;
}
