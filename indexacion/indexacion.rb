#lee los índices dentro del archivo y los guarda en un hash
def leerIndices
	indices_archivo = File.new("indices.txt", 'r')
	$indices_array = indices_archivo.readlines #leemos líneas del archivo
	$indices_array = $indices_array.sort #odenamos las líneas alfabéticamente
	$num_lineas = $indices_array.size #contamos las líneas que tiene el archivo de índices

	$indices_hash = Hash.new

	for i in 0...$num_lineas #creando hash de los indices {apellido => linea}
		aux = $indices_array[i].to_s.split(' ')#dividimos la cadena en apellido(llave) y en numero de bloque(valor)
		$indices_hash[aux[0]] = aux[1] #ponemos como llave del hash el apellido y como valor el número de bloque
	end

	indices_archivo.close
end

def leerEliminados
	eliminados_archivo = File.new("eliminados.txt", 'r')
	$indices_eliminados = eliminados_archivo.readlines
	num_eliminados = $indices_eliminados.size

	eliminados_archivo.close
end

# def buscar(apellido)
# 	if $indices_hash[apellido] == nil
# 		puts "No existe ese apellido en la agenda"
# 	else
# 		linea = $indices_hash[apellido].to_i
# 	end
# end

def insertar(nombre, telefono)
	if $indices_eliminados.length != 0 #si hay algun eliminado
		linea = $indices_eliminados[0].to_i
		agenda = File.new("agenda.txt", 'r+')
		agenda.rewind
		agenda.seek(81*(linea-1), IO::SEEK_SET)

		nombre.upcase! #pasamos el nombre a mayúscula
		array_nombre = nombre.split(' ') #dividimos el nombre en sus distintas partes
		telefono = telefono.gsub(/\D/, "") #ponemos al telefono en un formato sin guiones, espacios, etc.

		espacios = agregarEspacios(nombre.length, telefono.length) 
		agenda.puts nombre+' '+telefono+espacios
		agenda.close

		$indices_array.push(nombre+' '+linea.to_s)
		$indices_hash[array_nombre[0]] = linea
		$indices_eliminados.delete_at(0)

		eliminados = File.new("eliminados.txt",'w')

		for i in 0...$indices_eliminados.length
			eliminados.puts $indices_eliminados[i]
		end

		eliminados.close
		
	else
		nombre.upcase! #pasamos el nombre a mayúscula
		array_nombre = nombre.split(' ') #dividimos el nombre en sus distintas partes
		telefono = telefono.gsub(/\D/, "") #ponemos al telefono en un formato sin guiones, espacios, etc.

		#si ya hay una llave con ese apellido, dentro del hash de índices,
		#mándamos mensaje de que la persona ya existe y no se agrega a la agenda
		if $indices_hash[array_nombre[0]] != nil 
			puts "La persona ya existe"
			return false #regresamos false porque la persona no se creó
		else
			#cálculamos los espacios necesarios para que la cadena sea de un tamaño en específico
			espacios = agregarEspacios(nombre.length, telefono.length) 
			#cada linea en la agenda es de 81 caracteres
			File.open("agenda.txt", "a") do |file|
				file.puts nombre+' '+telefono+espacios #agregamos a la persona al archivo
			end

			$num_lineas += 1 #aumentamos el número de líneas que tiene el archivo
			#agregamos a la persona al arreglo de índices
			#Se agrega al arreglo para poder ordenarlo más facilmente
			$indices_array.push(nombre+' '+$num_lineas.to_s) 
			$indices_hash[array_nombre[0]] = $num_lineas #agregamos a la persona al hash
		end
	end
end

#guarda los índices del hash dentro del archivo de índices
def guardarIndices
	$indices_array.sort!

	archivo_indices = File.new("indices.txt", "w")

	$indices_array.each do |a|
		aux = a.split(' ')
		archivo_indices.puts aux.first+' '+aux.last 
	end

	archivo_indices.close
end

#regresa los espacios necesarios que se tienen que agregar
#para que todas las cadenas sean de tamaño 80
def agregarEspacios(tam_nombre,tam_telefono) 

	num_espacios = 80 - (tam_nombre + tam_telefono)
	espacios = ''

	for i in 1...num_espacios 
		espacios += ' '
	end

	return espacios
end

#hace una busqueda por hash de la persona
def buscar(apellido)
	apellido.upcase!
	if $indices_hash[apellido] == nil
		puts "El contacto no existe"
	else
		linea = $indices_hash[apellido].to_i
		contactos = File.new("agenda.txt")
		contactos.rewind
		contactos.seek(81*(linea-1), IO::SEEK_SET)
		persona = contactos.readline
		puts persona
		contactos.close
	end
end

def eliminar(apellido)
	apellido.upcase! #pásamos el apellido a mayúsculas
	if $indices_hash[apellido] == nil #no existe esa persona
		puts "El contacto no existe"
	else
		linea = $indices_hash[apellido].to_i
		contactos = File.new("agenda.txt",'r+')
		contactos.rewind
		contactos.seek(81*(linea-1), IO::SEEK_SET)
		cadena = " "*80
		contactos.puts cadena
		contactos.close
		
		$indices_eliminados.push(linea)
		$indices_hash.delete(apellido) #eliminamos del hash al contacto
		#imprimimos el nuevo hash en el archivo de índices
		indices = File.new("indices.txt",'w')
		$indices_hash.each{|key, value| indices.puts "#{key} #{value}"}
		indices.close

		leerIndices #leemos los indices
		
		eliminados = File.new("eliminados.txt", 'a')
		eliminados.puts linea.to_s
		eliminados.close
	end
end

#Inicio del programa
puts "Escribe 'help' para ayuda (sin las comillas)"
leerIndices #leemos índices
leerEliminados #leemos los eliminados para saber cúantos huecos hay y en dónde
while true do
	print ">>>> "

	opcion = gets.chomp

	case opcion
	when "guardar"
		puts "Guardar contacto"
		puts "Formato para nombre: apellido_paterno apellido_materno nombre1 nombre2"
		print "Ingresa nombre: "
		nombre = gets.chomp
		print "Ingresa telefono: "
		telefono = gets.chomp
		insertar(nombre, telefono)
		guardarIndices #guardamos el indice en el archivo para evitar errores del usuario
		leerIndices
	when "leerIndices"
		puts "Indices:"
		leerIndices
		p $indices_hash
	when "buscar"
		print "Ingresa el apellido: "
		apellido = gets.chomp
		buscar(apellido)
	when "verTodos"
		#mostrar los apellidos de todos los contactos disponibles
	when "eliminar"
		print "Ingresa el apellido de la persona que deseas eliminar: "
		apellido = gets.chomp
		eliminar(apellido)
	when "help"
		puts "Lista de comandos: "
		puts "guardar 			Guarda un contacto"
		puts "buscar 			Busca la información de un contacto en especifico"	
		puts "leerIndices 		Muestra los indices con su llave {apellido indice}"
		puts "bye 				Sale del programa"
	when "bye"
		puts "Adios"
		break
	end
end
