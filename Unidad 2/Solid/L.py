# L - Liskov Substitution Principle (Principio de Sustitución de Liskov)
# El principio establece que los objetos de una clase derivada deben poder sustituir a los objetos de la clase base sin alterar el funcionamiento del programa.

# Figura Geométrica

// Clase base
class Shape {
  area(): number {
    return 0; // La clase base no tiene una implementación específica
  }
}

// Clase derivada: Cuadrado
class Square extends Shape {
  constructor(public side: number) {
    super();
  }

  // Sobrescribimos el área para el cuadrado
  area(): number {
    return this.side * this.side;
  }
}

// Clase derivada: Círculo
class Circle extends Shape {
  constructor(public radius: number) {
    super();
  }

  // Sobrescribimos el área para el círculo
  area(): number {
    return Math.PI * this.radius * this.radius;
  }
}

// Uso de las clases: Puedes sustituir cualquier objeto de Shape con Square o Circle
let shapes: Shape[] = [new Square(4), new Circle(3)];

shapes.forEach(shape => {
  console.log(shape.area()); // Funciona sin importar si es un cuadrado o círculo
});
