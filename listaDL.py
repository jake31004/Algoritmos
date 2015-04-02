class Nodo:
	
	def __init__(self, dato = 0):
		self.dato = dato
		self.sig = None
		self.ant = None
	
	def __str__(self):
		return str(self.dato)

class LDL:
	def __init__(self):
		self.l = Nodo()
		self.first = self.l
		self.l.sig = self.l
		self.l.ant = self.l

	def __str__(self):
		cad = "[ "

		if not self.esVacia():
			aux = self.first

			while aux is not None:
				if aux.sig == None:
					cad += aux.__str__()+" "
				else:
					cad += aux.__str__()+", "
				aux = aux.sig

		return cad+"]"

	def esVacia(self):
		return self.l.sig == self.l and self.l.ant == self.l

	def insertar(self, dato):
		if self.esVacia():
			self.l.dato = dato
			self.l.sig = None
			self.l.ant = None
		else:
			nodoNuevo = Nodo(dato)
			nodoNuevo.sig = self.l.sig
			nodoNuevo.ant = self.l
			self.l.sig = nodoNuevo

			if self.l.ant is None:
				self.first = self.l

			self.l = nodoNuevo

	def buscar(self, x):
		if self.esVacia():
			return None
		else:
			if self.first.dato == x:
				return self.first
			else:
				aux = self.first.sig

				while aux is not None:
					if aux.dato == x:
						return aux
					aux = aux.sig

				return None
		

	def buscarInsertar(self, x, y):
		aux = self.buscar(x)

		if aux is not None:
			aux2 = self.first

			while aux2 is not None:
				if aux == aux2:
					aux.dato = y
					break

				aux2 = aux2.sig
		else:
			print("El nodo donde querías insertar no existe")

	def sacar(self, x):
		aux = self.buscar(x)

		if aux is not None:
			if aux.ant is None and aux.sig is None:
				aux.sig = aux
				aux.ant = aux
			elif aux.ant is None:
				aux.sig.ant = aux.ant
				self.first = self.first.sig
			elif aux.sig is None:
				self.l = aux.ant
				aux.ant.sig = aux.sig
			else:
				aux.ant.sig = aux.sig
				aux.sig.ant = aux.ant

			return aux
		else:
			print("El nodo no existe")
			return None


