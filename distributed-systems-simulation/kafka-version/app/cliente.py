from kafka import KafkaProducer, KafkaConsumer
import json
import time
import uuid
from kafka_config import *

cliente_id = str(uuid.uuid4())

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode()
)

consumer = KafkaConsumer(
    TOPIC_RESULTADO,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=lambda x: json.loads(x.decode()),
    group_id=cliente_id,
    auto_offset_reset='earliest'
)

# envia pedido
producer.send(TOPIC_FILA, cliente_id)
print(f"👤 Cliente {cliente_id} entrou")

# espera resposta
for msg in consumer:
    data = msg.value

    if data["cliente_id"] == cliente_id:
        if data["status"] == "CHEIA":
            print("❌ Fui embora (lotado)")
        else:
            print("💇 Fui atendido")
        break