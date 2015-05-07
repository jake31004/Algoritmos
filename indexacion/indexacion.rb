def leerIndices
	indices_archivo = File.new("indices.txt", 'r')
	$indices_array = indices_archivo.readlines #leemos líneas del archivo
	$indices_array = $indices_array.sort #odenamos las líneas alfabéticamente
	$num_lineas = $indices_array.size #contamos las líneas que tiene el archivo de índices

	$indices_hash = Hash.new

	for i in 0...$num_lineas #creando hash de los indices {apellido => linea}
		aux = $indices_array[i].to_s.split(' ')
		$indices_hash[aux[0]] = aux[1]
	end

	indices_archivo.close
end

# def buscar(apellido)
# 	if $indices_hash[apellido] == nil
# 		puts "No existe ese apellido en la agenda"
# 	else
# 		linea = $indices_hash[apellido].to_i
# 	end
# end

def insertar(nombre, telefono)
	if $indices_hash == nil
		leerIndices
		insertar(nombre, telefono)
	else
		nombre.upcase!
		array_nombre = nombre.split(' ')
		telefono = telefono.gsub(/\D/, "")

		if $indices_hash[array_nombre[0]] != nil
			puts "La persona ya existe"
			return false
		else
			espacios = agregarEspacios(nombre.length, telefono.length)

			File.open("agenda.txt", "a") do |file|
				file.puts nombre+' '+telefono+espacios
			end

			$num_lineas += 1
			$indices_array.push(nombre+' '+$num_lineas.to_s)
			$indices_hash[array_nombre[0]] = $num_lineas
		end
	end
end

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



puts "Escribe 'help' para ayuda (sin las comillas)"

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
		guardarIndices
	when "leerIndices"
		puts "Indices:"
		leerIndices
		p $indices_hash
	when "help"
		puts "Lista de comandos: "
		puts "guardar 			Guarda un contacto"
		puts "bye 				Sale del programa"
		puts "leerIndices 		Muestra los indices con su llave {apellido indice}"
	when "bye"
		puts "Adios"
		break
	end
end
