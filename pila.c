//Pila NO dinámica
#include <stdio.h>
#include <stdlib.h>

//creacion de la pila, tiene un tope, un maximo de elementos y un apuntador a los elementos
typedef struct{
	int tope;
	int max;
	int *elem;
}Pila;

Pila *crearPila(int);
int esVacia(Pila *);
int push(Pila *, int);
int pop(Pila *);
void imprimirPila(Pila *);
void impPila(Pila *); //imprime la pila de forma vertical

int main(int argc, char const *argv[])
{
	int i, max, elem;

	printf("Ingresa el tamanio de la pila: ");
	scanf("%d", &max);

	Pila *p = crearPila(max);

	printf("\nLa pila que se creo es:\n\n" );
	imprimirPila(p); //solo se imprimen los corchetes porque está vacía la Pila

	for(i = 0; i < max; i++)
	{
		printf("Ingresa el elemento %d: ", i);
		scanf("%d", &elem);
		push(p, elem);
	}

	printf("La pila que creaste es: \n");
	//imprimiendola de forma horizontal
	printf("\nPila horizontal: \n");
	imprimirPila(p);
	//imprimiendola de forma vertical
	printf("\nPila vertical: \n");
	impPila(p);

	//quitando elementos de la pila

	for(i = 0; i < max; i++)
	{
		printf("Se quito a: %d\n", pop(p));
		impPila(p);
	}

	return 0;
}

//la pila que se crea, está vacía
Pila *crearPila(int max){
	Pila *p = (Pila *)malloc(sizeof(Pila));
	p->tope = -1;
	p->max = max;
	p->elem = (int *)malloc(max * sizeof(int)); //creamos un arreglo para el numero de elementos que queremos en la pila
	return p;
}


int esVacia(Pila *p){
	return (p->tope < 0); //si es tope es -1 (cuando se creó), la pila está vacía, 0 es falso y 1 es verdadero
}

int push(Pila *p, int x){
	if(p->tope < (p->max)-1)//si todavía no llega al tope inserta el nodo x
	{	
		p->elem[++(p->tope)] = x; //insertalo en la poscicion que sigue
		return ((p->max-1) - (p->tope)); //regresa los espacios que todavía me quedan en la pila
	}else
		return (-1); //regresa -1 si ya se llegó al tope de la pila
}

int pop(Pila *p){
	if(esVacia(p))
		return -10000; //regresa un número de error
	else
		return (p->elem[(p->tope)--]); //regresa el número de la última poscición y disminuye el tope en uno
}

void imprimirPila(Pila *p){
	int i;
	printf("[ ");

	for(i = 0; i <= (p->tope); i++)
	{	
		if(i == p->tope) //el último elemento no se imprime con la coma
			printf(" %d ", p->elem[i]);	
		else
			printf(" %d, ", p->elem[i]);
	}

	printf(" ]\n");	
}

void impPila(Pila *p){
	int i;

	if(esVacia(p))
		printf("[ ]\n");
	else
		for(i = p->tope; i >= 0; i--)
			printf("[ %d ]\n", p->elem[i]);
}