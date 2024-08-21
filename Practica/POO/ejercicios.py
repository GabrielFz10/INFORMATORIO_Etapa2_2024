""" Ejecicio 1 : Sistema de Gestión de Biblioteca

Crea un sistema para gestionar los libros en una biblioteca. 
El sistema debe permitir agregar nuevos libros(al menos 4 atributos, entre ellos uno para saber si lo puedo prestar), 
buscar libros por título o autor, y mostrar la lista de todos los libros disponibles.
"""

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = disponible
        
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.anio}) - {'Disponible' if self.disponible else 'No disponible'}"
    
# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        return resultados

    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible]
        if disponibles:
            print("Libros disponibles:")
            for libro in disponibles:
                print(libro)
        else:
            print("No hay libros disponibles en este momento.")

# Ejemplo de uso
biblioteca = Biblioteca()

# Agregamos algunos libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("1984", "George Orwell", 1949, disponible=False)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro4 = Libro("El nombre de la rosa", "Umberto Eco", 1980)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)

# Buscamos un libro por título
resultado_titulo = biblioteca.buscar_por_titulo("1984")
if resultado_titulo:
    print("\nResultado de la búsqueda por título:")
    for libro in resultado_titulo:
        print(libro)
else:
    print("\nNo se encontró ningún libro con ese título.")

# Buscamos un libro por autor
resultado_autor = biblioteca.buscar_por_autor("Gabriel García Márquez")
if resultado_autor:
    print("\nResultado de la búsqueda por autor:")
    for libro in resultado_autor:
        print(libro)
else:
    print("\nNo se encontró ningún libro de ese autor.")

# Mostramos todos los libros disponibles
print("\nLista de libros disponibles:")
biblioteca.mostrar_libros_disponibles()












"""
Ejecicio 1 : Sistema de Gestión de Biblioteca

Crea un sistema para gestionar los libros en una biblioteca. 
El sistema debe permitir agregar nuevos libros
(al menos 4 atributos, entre ellos uno para saber si lo puedo prestar), 
buscar libros por título o autor, y mostrar la lista de todos los libros disponibles.
"""


"""
Ejercicio 2 : Sistema de Gestión de Estudiantes

Desarrolla un sistema para gestionar los datos de estudiantes en una universidad. 
El sistema debe permitir agregar nuevos estudiantes, matricular estudiantes en cursos, 
y mostrar los estudiantes de la universidad
"""


"""
Ejercicio 3 : Sistema de Gestión de Reservas de Hotel

Diseña un sistema para gestionar las reservas en un hotel. 
El sistema debe permitir gestionar las habitaciones, hacer reservas, y mostrar la disponibilidad de habitaciones.
"""









