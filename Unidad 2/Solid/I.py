# I - Interface Segregation Principle (Principio de Segregación de Interfaces)
# Este principio establece que una clase no debe estar obligada a implementar interfaces que no usa. En lugar de tener una gran interfaz con métodos innecesarios, es mejor dividirlas en interfaces más específicas.

# Manejo de Animales

// Interfaz grande (NO cumple con ISP)
interface Animal {
  eat(): void;
  fly(): void;   // No todos los animales vuelan
  swim(): void;  // No todos los animales nadan
}

// Cumpliendo con el principio de segregación de interfaces
// Creamos interfaces más específicas

interface Eater {
  eat(): void;
}

interface Flyer {
  fly(): void;
}

interface Swimmer {
  swim(): void;
}

// Clases que implementan solo las interfaces que necesitan
class Dog implements Eater, Swimmer {
  eat(): void {
    console.log("Dog is eating");
  }
  
  swim(): void {
    console.log("Dog is swimming");
  }
}

class Bird implements Eater, Flyer {
  eat(): void {
    console.log("Bird is eating");
  }
  
  fly(): void {
    console.log("Bird is flying");
  }
}

class Fish implements Eater, Swimmer {
  eat(): void {
    console.log("Fish is eating");
  }
  
  swim(): void {
    console.log("Fish is swimming");
  }
}

// Uso: Los animales solo implementan lo que necesitan
const dog = new Dog();
dog.eat();  // "Dog is eating"
dog.swim(); // "Dog is swimming"

const bird = new Bird();
bird.fly(); // "Bird is flying"
