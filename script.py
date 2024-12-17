import requests
import csv
import sys

# Configuración necesaria previa del ContextBroker
CONTEXT_BROKER_URL = "http://localhost:1026/v2/entities"
HEADERS = {"Content-Type": "application/json"}

# Para leer el archivo entities.CSV y aplicar un formato compatible con lo esperado por el API de ContextBroker
def read_csv_to_entities(file_path):
    entities = []
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # Bucle, anidado de sengundo nivel, que mira las columnas de cada fila
        for row in csv_reader:
            entity = {
                "id": row["entityId"],
                "type": row["entityType"],
                "attributes": {}
            }
            for column_name, column_value in row.items():
                if column_name not in ["entityId", "entityType"]:
                    attribute_name, attribute_type = column_name.split("<")
                    attribute_type = attribute_type.rstrip(">")
                    entity["attributes"][attribute_name] = {
                        "value": column_value,
                        "type": attribute_type
                    }
            # Incluye cada entity
            entities.append(entity)
    # Devuelve las entities
    return entities

# Para publicar las entidades en el ContextBroker
def send_entity_to_context_broker(entity):
    payload = {
        "id": entity["id"],
        "type": entity["type"],
    }
    for attribute_name, attribute_data in entity["attributes"].items():
        payload[attribute_name] = attribute_data
    try:
        response = requests.post(CONTEXT_BROKER_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        print(f"Éxito: Entidad {entity['id']} publicada correctamente.")
    except requests.exceptions.RequestException as error:
        print(f"Error: No se pudo publicar la entidad {entity['id']}. Detalles: {error}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <ruta_al_csv>")
        sys.exit(1)   
    csv_file_path = sys.argv[1]
    try:
        # Extrae los entities del csv
        entities = read_csv_to_entities(csv_file_path)
        # Bucle Iterator para cada entity de los entities
        for entity in entities:
            send_entity_to_context_broker(entity)
    # Excepciones
    except FileNotFoundError:
        print(f"Error: El archivo {csv_file_path} no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")
