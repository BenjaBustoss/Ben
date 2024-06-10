sistema_escolar = {
    'Curso1': {
        'nombre': 'Curso de Python',
        'precio': 100,
        'profesor': 'Juan Pérez',
        'contacto': 'juan.perez@bigbaydata.com',
        'alumnos': ['Ana', 'Miguel', 'Elena'],
        'evaluacion_promedio': 8.5
    },
    'Curso2': {
        'nombre': 'Curso de Data Science',
        'precio': 150,
        'profesor': 'María García',
        'contacto': 'maria.garcia@bigbaydata.com',
        'alumnos': ['Pedro', 'Lucía', 'Carlos'],
        'evaluacion_promedio': 9.0
    },
    'Curso3': {
        'nombre': 'Curso de Machine Learning',
        'precio': 200,
        'profesor': 'Luis Martínez',
        'contacto': 'luis.martinez@bigbaydata.com',
        'alumnos': ['Sofía', 'Javier', 'Laura'],
        'evaluacion_promedio': 8.8
    }
}

def mostrar_cursos():
    print("Cursos disponibles en BigBayData.com:")
    for curso, info_curso in sistema_escolar.items():
        print(f"\n{curso}:")
        print(f"Nombre: {info_curso['nombre']}")
        print(f"Precio: ${info_curso['precio']}")
        print(f"Profesor: {info_curso['profesor']}")
        print(f"Contacto: {info_curso['contacto']}")
        print(f"Alumnos: {', '.join(info_curso['alumnos'])}")
        print(f"Evaluación promedio: {info_curso['evaluacion_promedio']}")

def main():
    mostrar_cursos()

if __name__ == "__main__":
    main()
