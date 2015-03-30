//pila NO dinámica en java

class Pila{
	int max;
	double[] elem;
	int tope;

	public Pila(int max){ //constructor de la pila
		this.max = max;
		this.elem = new double[this.max];
		this.tope = -1; //pila vacía
	}

	boolean push(double x){
		if(this.estaLlena())
			return false;

		this.elem[++this.tope] = x;
		return true;
	}

	double pop(){
		if(this.esVacia())
			return Double.NaN;

		return this.elem[this.tope--];
	}

	boolean esVacia(){
		return (this.tope == -1);
	}

	boolean estaLlena(){
		return (this.tope == this.max-1);
	}

	@Override
	public String toString(){
		int i;
		String cad = "[ ";

		for (i = 0; i < this.tope; i++ )
		{
			if( i == this.tope-1)
				cad += this.elem[i]+" ";
			else	
				cad += this.elem[i]+", ";
		}

		cad += " ]";
		return cad;	
	}

	void impPila(){
		int i;

		if(esVacia())
			System.out.println("[ ]");
		else
			for(i = this.tope; i >= 0; i--)
				System.out.println("[ "+this.elem[i]+" ]");
	}
}

class Principal{
	public static void main(String[] args) {
		int i;

		Pila p = new Pila(5);

		System.out.println("La cola creada es: ");
		System.out.println(p);
		System.out.println("Intentado sacar elementos de la pila cuando está vacía");
		System.out.println(p.pop()); //intentando sacar elementos cuando está vacía

		System.out.println("Llenando la pila");
		for (i = 0; i < p.max; i++) { //llenando pila
			p.push(i);
			System.out.println(p);
		}

		System.out.println("Pila llena: ");
		p.impPila();

		//vaciando pila
		System.out.println("Vaciando pila");
		while(!p.esVacia()){
			p.pop();
			System.out.println(p);
		}

		System.out.println("Pila vacía");
		p.impPila();


	}
}