# Proyecto de Prueba para Alten-SmartCities-Telefónica: ContextBroker con Importación desde CSV

Este proyecto levanta una instancia de **ContextBroker** utilizando `docker-compose` y realiza la publicación de entidades en el ContextBrocker mediante un script en Python que lee dichos datos de un archivo CSV

---

## Requisitos Previos

### Herramientas necesarias:
1. **Docker** y **Docker Compose**.
2. **Python3.7 o mayor** 
3. **Dependencias de Python**:
   ```bash
   pip install requests pandas
   ```

---

## Desplegar el ContextBroker

1. **Clonar el repositorio FIWARE Orion**:
   ```bash
   git clone https://github.com/telefonicaid/fiware-orion.git
   ```

2. **Levantar el entorno con Docker Compose**:
   ```bash
   cd fiware-orion/docker
   sudo docker-compose up -d

   Response:
   docker_mongo_1 is up-to-date
   docker_orion_1 is up-to-date
   ```

3. **Verificar que el ContextBroker esté en funcionamiento - Versión activa**:
   ```bash
   curl -X GET http://localhost:1026/version

   Response:
   {
   "orion" : {
      "version" : "4.1.0-next",
      "uptime" : "0 d, 0 h, 35 m, 55 s",
      "git_hash" : "fec7146609326f30f86eb33f12ddae05765eac1e",
      "compile_time" : "Fri Nov 8 09:16:31 UTC 2024",
      "compiled_by" : "root",
      "compiled_in" : "buildkitsandbox",
      "release_date" : "Fri Nov 8 09:16:31 UTC 2024",
      "machine" : "x86_64",
      "doc" : "https://fiware-orion.rtfd.io/"
   }
   ```

---

## Formato del Archivo CSV

El archivo CSV contiene:
- **entityId**: Identificador de la entidad
- **entityType**: Tipo de la entidad
- Atributos adicionales con formato `nombre<tipo>`. temperature < Float >, humidity < Integer >

---

## Uso del Script

### Descripción

El script lee un archivo CSV especificado como argumento, procesa los datos, convierte en el formato requerido por el API y publica cada entidad en el ContextBroker.

### Ejecutar el Script

1. Para ejecutar el script indicando la ruta del archivo CSV:
   ```bash
   python3 script.py entities.csv
   ```

2. Para verifica las entidades creadas en el ContextBroker:
   ```bash
   curl -X GET http://localhost:1026/v2/entities
   ```

3. Response:
   ```bash
   /home/juan/prueba Alten/fiware-orion/pruebasFinalesEjercicio.jpg
   ```

---

## Nuevos archivos incluidos de la prueba
```plaintext
.
├── docker-compose.yml - Despliega la instancia
├── script.py - Procesa y publica los datos del archivo csv
├── entities.csv - Archivo csv que contiene las entidades
├── pruebasFinalesEjercicio.jpg - Comprobaciones en formato jpg
└── README.md 
```
