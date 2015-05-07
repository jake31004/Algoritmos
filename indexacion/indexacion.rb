indices_archivo = File.new("indices.txt", 'r')
indices_array = indices_archivo.readlines #leemos líneas del archivo
indices_array = indices_array.sort #odenamos las líneas alfabéticamente
$num_lineas = indices_array.size #contamos las líneas que tiene el archivo de índices

$indices_hash = Hash.new

for i in 0...$num_lineas #creando hash de los indices {apellido => linea}
	aux = indices_array[i].to_s.split(' ')
	$indices_hash[aux[0]] = aux[1]
end


def buscar(apellido)
	if $indices_hash[apellido] == nil
		puts "No existe ese apellido en la agenda"
	else
		linea = $indices_hash[apellido].to_i
	end
end

