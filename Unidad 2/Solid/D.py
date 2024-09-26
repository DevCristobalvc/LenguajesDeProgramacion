# D - Dependency Inversion Principle (Principio de Inversión de Dependencias)
# Este principio establece que las clases de alto nivel no deben depender de clases de bajo nivel, sino de abstracciones (interfaces). Además, las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones.

# Sistema de Notificaciones

// Interfaz que representa la abstracción
interface NotificationService {
  sendMessage(message: string): void;
}

// Clase concreta que implementa la abstracción
class EmailService implements NotificationService {
  sendMessage(message: string): void {
    console.log("Sending email with message:", message);
  }
}

// Otra clase concreta que implementa la abstracción
class SMSService implements NotificationService {
  sendMessage(message: string): void {
    console.log("Sending SMS with message:", message);
  }
}

// Clase de alto nivel que usa la abstracción en lugar de depender de una implementación concreta
class NotificationSender {
  private service: NotificationService;

  constructor(service: NotificationService) {
    this.service = service; // Inyección de dependencia
  }

  sendNotification(message: string): void {
    this.service.sendMessage(message); // Se usa el servicio sin importar su implementación
  }
}

// Uso de la clase de alto nivel
const emailService = new EmailService();
const smsService = new SMSService();

const notificationSender1 = new NotificationSender(emailService);
notificationSender1.sendNotification("Hello via Email"); // "Sending email with message: Hello via Email"

const notificationSender2 = new NotificationSender(smsService);
notificationSender2.sendNotification("Hello via SMS");   // "Sending SMS with message: Hello via SMS"
