# S - Single Responsibility Principle (Principio de Responsabilidad Única)
# Este principio establece que una clase debe tener una única responsabilidad o razón para cambiar. Cada clase debe ocuparse de una tarea específica.

# Manejo de Usuarios y Validación de Correos


// Una clase que tiene responsabilidad única: manejar usuarios.
class UserManager {
  private users: string[] = [];

  // Método para agregar un usuario
  addUser(user: string): void {
    this.users.push(user);
  }

  // Método para obtener todos los usuarios
  getUsers(): string[] {
    return this.users;
  }
}

// Clase separada para validar correos electrónicos.
// Esta clase tiene la única responsabilidad de validación.
class EmailValidator {
  // Método para verificar si un correo es válido
  isValidEmail(email: string): boolean {
    return email.includes("@");
  }
}

// Uso de las clases:
// Las clases tienen responsabilidades separadas. Una para gestionar usuarios y otra para validación.
const userManager = new UserManager();
const emailValidator = new EmailValidator();

if (emailValidator.isValidEmail("example@mail.com")) {
  userManager.addUser("example@mail.com");
}
