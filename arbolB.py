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

	#metodo para agregar un nuevo nodo
	def meter(self,  ABB,dato, idNodo, padre = None):
		if self.esVacio():
			ABB.dato = dato
			ABB.idNodo = idNodo
			ABB.der = None
			ABB.izq = None
		elif idNodo < ABB.idNodo: #si el id es menor que el nodo anterior, se mete el nodo a la izquierda
			if ABB.izq is not None: #si el nodo de la izquiera no esta vacio, metemos el nodo a la izquierda de ese nodo
				self.meter(ABB.izq, dato, idNodo, ABB) #el nodo se metera haste que encuentre un espacio vacio
			else: #si el nodo de la izquierda si esta vacio, se agrega el nodo 
				nodoNuevo = Nodo(dato, idNodo)
				ABB.izq = nodoNuevo #se crea un nuevo nodo y hacemos que el nodo en el que estamos apunte hacia el
				ABB.izq.padre = ABB #el nuevo nodo hace referencia a su padre
		elif idNodo > ABB.idNodo: #si el id es mayor que el nodo anterior, se mete el nodo a la derecha
			if ABB.der is not None: #si el nodo de la derecha esta ocupado, nos desplazamos otra vez hacia la derecha
				self.meter(ABB.der, dato, idNodo, ABB)	#agregamos el nodo hasta encontrar un espacio vacio	
			else: #cuando encontramos el espacio vacio, creamos un nuevo nodo y referenciamos a la derecha
				nodoNuevo = Nodo(dato, idNodo)
				ABB.der = nodoNuevo
				ABB.der.padre = ABB #referenciamos al nodo creado con su padre
		else: #si no se pudo crear el nodo, porque este ya existia (id repetido no contenido), regresamos un false
			return False

		return True	#regresamos un true si se logro crear el nuevo nodo

	#metodo para buscar un nodo, regresa el nodo que buscamos y su padre
	def buscar(self, ABB, idNodo):
		if self.esVacio() or ABB is None: #si el arbol esta vacio o el nodo no existe regresamos none
			return None, None
		elif idNodo < ABB.idNodo: #si el nodo es menor que el nodo en el que estamos, lo buscamos a la izquierda
			return self.buscar(ABB.izq, idNodo)
		elif idNodo > ABB.idNodo: #si el nodo es mayor que el nodo en el que estamos, lo buscamos a la derecha
			return self.buscar(ABB.der, idNodo)
		else: #cuando encontramos el nodo que estabamos buscando lo regresamos y tambien al padre
			return ABB, ABB.padre

	#metodo para buscar un nodo, funciona igual que buscar() pero este metodo no regresa al padre
	def buscarNoDad(self, ABB, idNodo):
		if self.esVacio() or ABB is None:
			return None
		elif idNodo < ABB.idNodo:
			return self.buscarNoDad(ABB.izq, idNodo)
		elif idNodo > ABB.idNodo:
			return self.buscarNoDad(ABB.der, idNodo)
		else:
			return ABB

	#metodo para sacar un nodo del arbol, regresa el nodo que queremos sacar
	def sacar(self, ABB, idNodo):
		aux, padre = self.buscar(ABB, idNodo) #buscamos el nodo que queremos sacar

		if aux is not None: #si el nodo si existe se ejecuta el siguiente codigo
			if aux.izq == None and aux.der == None: #aux es hoja (no tiene hijos)
				if padre.izq == aux: #si el nodo es el hijo izquierdo,la referencia izquierda del padre apuntara a None 
					padre.izq = None 
				else:
					padre.der = None #si el nodo es el hijo derecho, la referencia derecha del padre apuntara a None
			elif aux.izq is not None and aux.der is None: #tiene un hijo, y es el izquierdo
				if padre.izq == aux: #si el nodo es el hijo izquierdo, el padre.izquierdo ahora apuntara al hijo izquierdo del nodo que queremos sacar
					padre.izq = aux.izq
					aux.izq.padre = padre #el padre del hijo del nodo ahora sera el padre del nodo que sacamos
				else: #si el nodo es el hijo derecho, el padre.derecho ahora apuntara al hijo izquierdo del nodo que queremos sacar
					padre.der = aux.izq 
					aux.izq.padre = padre #el padre del hijo del nodo ahora sera el padre del nodo que sacamos
			elif aux.izq is None and aux.der is not None: #tiene un hijo y es el derecho
				if padre.izq == aux: #funciona igual que el elif de arriba, solo que las referencias seran hacia el hijo derecho
					padre.izq = aux.der
					aux.der.padre = padre
				else: 
					padre.der = aux.der
					aux.der.padre = padre
			else: #tiene 2 hijos
				aux2 = Nodo(aux.dato,aux.idNodo) #guardamos la informacion del nodo antes de ser sobreescrita, para poder enviarla
				aux2.padre = aux.padre 
				sucesor, padreS = self.minimo(aux.der, aux) #encotramos el nodo sucesor(menor de los mayores) y el padre de este
				aux.dato = sucesor.dato #el nodo ahora tiene la informacion del sucesor
				aux.idNodo = sucesor.idNodo
				
				if padreS.izq == sucesor: #si habia mas de un nodo mayor al nodo que sacamos
					padreS.izq = sucesor.der #el padre del sucesor ahora apunta a los hijos del sucesor
				else: #si solo habia un nodo mayor al nodo que sacamos
					padreS.der = sucesor.der #el padre del sucesor ahora apunta a los hijos del sucesor
				
				return aux2 #regresamos la info del nodo que quitamos

			return aux #regresamos la info del nodo que quitamos
		return None #si el nodo que queriamos quitar no existe regresamos None


	#metodo que regresa el dato que tenga el idNodo minimo, y su padre
	def minimo(self, ABB, padre = None):
		if ABB.izq is not None: #recorremos hacia la izquierda hasta encontrar el idNodo mas chico
			return self.minimo(ABB.izq, ABB)

		return ABB, padre

	#metodo que regresa el dato que tenga el idNodo maximo y su padre
	def maximo(self, ABB, padre = None):
		if ABB.der is not None: #recorremos hacia la derecha hasta encontrar el idNodo mas grande
			return self.maximo(ABB.der, ABB)

		return ABB, padre

	#imprimimos los nodos,recorriendo el arbol en preOrden. 
	#Primero imprimimos el dato y luego recorremos a la izquierda y despues a la derecha
	def preOrden(self, ABB):
		if self.esVacio():
			return None
		if ABB is None:
			return None

		print(ABB)
		self.preOrden(ABB.izq)
		self.preOrden(ABB.der)

	#imprimimos los nodos, recorriendo el arbol en inOrden.
	#Primero recorremos a la izquierda, luego imprimimos y despues recorremos a la derecha
	def inOrden(self, ABB):
		if self.esVacio():
			return None
		if ABB is None:
			return None

		self.inOrden(ABB.izq)
		print(ABB)
		self.inOrden(ABB.der)


	#imprimimos los nodos, recorriendo el arbol en postOrden.
	#Primero recorremos a la izquierda, luego recorremos a la derecha y al final imprimimos
	def postOrden(self, ABB):
		if self.esVacio():
			return None
		if ABB is None:
			return None

		self.postOrden(ABB.izq)
		self.postOrden(ABB.der)
		print(ABB)




