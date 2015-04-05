#Definicion del nodo, tiene el dato y referencia de un nodo a la izquierda y un nodo a la derecha

class Nodo: 
	def __init__(self, dato = 0, idNodo = 0):
		self.dato = dato
		self.idNodo = idNodo
		self.izq = None
		self.der = None
	def __str__(self):
		return "Dato: "+str(self.dato)+" idDato: "+str(self.idNodo)

class ABB:
	def __init__(self):
		self.ABB = Nodo()
		self.ABB.izq = self.ABB 
		self.ABB.der = self.ABB		

	def esVacio(self):
		return self.ABB.izq == self.ABB and self.ABB.der == self.ABB

	def meter(self,  ABB,dato, idNodo):
		if self.esVacio():
			ABB.dato = dato
			ABB.idNodo = idNodo
			ABB.der = None
			ABB.izq = None
		elif idNodo < ABB.idNodo:
			if ABB.izq is not None:
				self.meter(ABB.izq, dato, idNodo)
			else:
				nodoNuevo = Nodo(dato, idNodo)
				ABB.izq = nodoNuevo
		elif idNodo > ABB.idNodo:
			if ABB.der is not None:
				self.meter(ABB.der, dato, idNodo)		
			else:
				nodoNuevo = Nodo(dato, idNodo)
				ABB.der = nodoNuevo
		else:
			return False

		return True	

	def buscarId(self, ABB, idNodo):
		if self.esVacio() or ABB is None:
			return None
		if idNodo < ABB.idNodo:
			self.buscarId(ABB.izq, idNodo)
		if idNodo > ABB.idNodo:
			self.buscarId(ABB.der, idNodo)
		if idNodo == ABB.idNodo:
			return ABB




