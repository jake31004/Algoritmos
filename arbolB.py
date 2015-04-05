#Definicion del nodo, tiene el dato y referencia de un nodo a la izquierda y un nodo a la derecha
#Tambien tiene la referencia de su nodo padre
class Nodo: 
	def __init__(self, dato = 0, idNodo = 0):
		self.dato = dato
		self.idNodo = idNodo
		self.padre = None
		self.izq = None
		self.der = None
		#Imprime el nodo: imprime el dato, su id y su padre, si es la raiz el padre es None
	def __str__(self):
		if self.padre is not None:
			return "Dato: "+str(self.dato)+" idNodo: "+str(self.idNodo)+" Padre: "+str(self.padre.idNodo)
		else:
			return "Dato: "+str(self.dato)+" idNodo: "+str(self.idNodo)+" Padre: None"

class ABB:
	def __init__(self):
		self.ABB = Nodo()
		self.ABB.izq = self.ABB #Condicion para que el arbol creado este vacio
		self.ABB.der = self.ABB		

	def esVacio(self):
		return self.ABB.izq == self.ABB and self.ABB.der == self.ABB

	def meter(self,  ABB,dato, idNodo, padre = None):
		if self.esVacio():
			ABB.dato = dato
			ABB.idNodo = idNodo
			ABB.der = None
			ABB.izq = None
		elif idNodo < ABB.idNodo: #si el id es menor que el nodo anterior, se mete el nodo a la izquierda
			if ABB.izq is not None:
				self.meter(ABB.izq, dato, idNodo, ABB)
			else:
				nodoNuevo = Nodo(dato, idNodo)
				ABB.izq = nodoNuevo
				ABB.izq.padre = ABB
		elif idNodo > ABB.idNodo:
			if ABB.der is not None:
				self.meter(ABB.der, dato, idNodo, ABB)		
			else:
				nodoNuevo = Nodo(dato, idNodo)
				ABB.der = nodoNuevo
				ABB.der.padre = ABB
		else:
			return False

		return True	

	def buscar(self, ABB, idNodo):
		if self.esVacio() or ABB is None:
			return None, None
		elif idNodo < ABB.idNodo:
			return self.buscar(ABB.izq, idNodo)
		elif idNodo > ABB.idNodo:
			return self.buscar(ABB.der, idNodo)
		elif idNodo == ABB.idNodo:
			return ABB, ABB.padre

	def buscarNoDad(self, ABB, idNodo):
		if self.esVacio() or ABB is None:
			return None
		elif idNodo < ABB.idNodo:
			return self.buscarNoDad(ABB.izq, idNodo)
		elif idNodo > ABB.idNodo:
			return self.buscarNoDad(ABB.der, idNodo)
		elif idNodo == ABB.idNodo:
			return ABB

	def sacar(self, ABB, idNodo):
		aux, padre = self.buscar(ABB, idNodo)

		if aux is not None:
			if aux.izq == None and aux.der == None: #aux es hoja
				if padre.izq == aux:
					padre.izq = None
				else:
					padre.der = None
			elif aux.izq is not None and aux.der is None: #tiene un hijo, y es el izquierdo
				if padre.izq == aux:
					padre.izq = aux.izq
					aux.izq.padre = padre
				else:
					padre.der = aux.izq
					aux.izq.padre = padre
			elif aux.izq is None and aux.der is not None: #tiene un hijo y es el derecho
				if padre.izq == aux:
					padre.izq = aux.der
					aux.der.padre = padre
				else: 
					padre.der = aux.der
					aux.der.padre = padre
			else: #tiene 2 hijos
				aux2 = Nodo(aux.dato,aux.idNodo) #guardamos la informacion del nodo antes de ser sobreescrita
				aux2.padre = aux.padre
				sucesor, padreS = self.minimo(aux.der, aux)
				aux.dato = sucesor.dato
				aux.idNodo = sucesor.idNodo
				
				if padreS.izq == sucesor:
					padreS.izq = sucesor.der
					return aux2 #regresamos la info del nodo que quitamos
				else:
					padreS.der = sucesor.der
					return aux2 #regresamos la info del nodo que quitamos

			return aux
		return None



	def minimo(self, ABB, padre = None):
		if ABB.izq is not None:
			return self.minimo(ABB.izq, ABB)

		return ABB, padre

	def maximo(self, ABB, padre = None):
		if ABB.der is not None:
			return self.maximo(ABB.der, ABB)

		return ABB, padre

	def preOrden(self, ABB):
		if self.esVacio():
			return None
		if ABB is None:
			return None

		print(ABB)
		self.preOrden(ABB.izq)
		self.preOrden(ABB.der)

	def inOrden(self, ABB):
		if self.esVacio():
			return None
		if ABB is None:
			return None

		self.inOrden(ABB.izq)
		print(ABB)
		self.inOrden(ABB.der)

	def postOrden(self, ABB):
		if self.esVacio():
			return None
		if ABB is None:
			return None

		self.postOrden(ABB.izq)
		self.postOrden(ABB.der)
		print(ABB)




