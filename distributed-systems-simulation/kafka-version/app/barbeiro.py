from kafka import KafkaConsumer, KafkaProducer
import json
import time
from kafka_config import *

consumer = KafkaConsumer(
    TOPIC_FILA,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=lambda x: json.loads(x.decode())
)

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode()
)

fila = []
CADEIRAS = 3

print("💈 Barbeiro pronto...")

for msg in consumer:
    cliente = msg.value
    print(f"👤 Cliente chegou: {cliente}")

    if len(fila) < CADEIRAS:
        fila.append(cliente)

        print(f"🪑 Cliente aguardando ({len(fila)})")

        # atender imediatamente (simples)
        atual = fila.pop(0)

        print(f"💈 Atendendo {atual}")
        time.sleep(3)

        producer.send(TOPIC_RESULTADO, {
            "cliente_id": atual,
            "status": "CORTADO"
        })

        print("📢 PRÓXIMO")

    else:
        print("❌ Barbearia cheia")

        producer.send(TOPIC_RESULTADO, {
            "cliente_id": cliente,
            "status": "CHEIA"
        })