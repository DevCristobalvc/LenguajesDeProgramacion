# O - Open/Closed Principle (Principio Abierto/Cerrado)
# Este principio sugiere que las clases deben estar abiertas a la extensión pero cerradas a la modificación.

# Formatos de Exportación

// Clase base que está abierta a la extensión mediante herencia
abstract class Exporter {
  abstract export(data: string): string;
}

// Clase que extiende el comportamiento sin modificar la clase base
class PDFExporter extends Exporter {
  export(data: string): string {
    return `Exporting data as PDF: ${data}`;
  }
}

// Otra clase que también extiende la funcionalidad
class CSVExporter extends Exporter {
  export(data: string): string {
    return `Exporting data as CSV: ${data}`;
  }
}

// Se pueden agregar nuevos exportadores sin modificar las clases existentes
const pdfExporter = new PDFExporter();
const csvExporter = new CSVExporter();

console.log(pdfExporter.export("My data"));
console.log(csvExporter.export("My data"));
