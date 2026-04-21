# 📡 Barbearia Distribuída — Versão com Kafka

## 📌 Descrição

Esta versão utiliza Apache Kafka para comunicação assíncrona baseada em eventos.

* 👨‍🦱 Clientes → produtores (producers)
* 💈 Barbeiro → consumidor (consumer)
* 📡 Kafka → intermediador de mensagens

---

## ⚙️ Pré-requisitos

* Docker
* Docker Compose

---

## 📁 Estrutura

```
kafka-version/
│
├── app/
│   ├── barbeiro.py
│   ├── cliente.py
│   ├── kafka_config.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ▶️ Passo a passo para execução

### 🔹 1. Acessar a pasta

```
cd kafka-version
```

---

### 🔹 2. Subir o ambiente completo

```
docker-compose up --build --scale cliente=5
```

👉 Isso sobe:

* Zookeeper
* Kafka
* Barbeiro
* Clientes

---

## ⏳ Observação importante

Kafka leva alguns segundos para iniciar.

Se der erro na primeira vez:

```
docker-compose restart
```

---

## 🧪 O que você verá

* Clientes enviando mensagens
* Kafka recebendo eventos
* Barbeiro consumindo e processando
* Respostas sendo enviadas

---

## 🔄 Parar o sistema

```
CTRL + C
docker-compose down
```

---

## ⚠️ Problemas comuns

* ❌ Kafka não inicializou ainda
* ❌ Erro de conexão → aguarde alguns segundos
* ❌ Containers não sobem → rebuild:

```
docker-compose down
docker-compose up --build
```

---

## 🧠 Explicação técnica

* Comunicação assíncrona (event-driven)
* Baixo acoplamento entre serviços
* Alta escalabilidade

---

## 🎯 Diferencial dessa versão

* Arquitetura moderna
* Usada em sistemas reais
* Alta performance e escalabilidade

---

## 🆚 Comparação com sockets

| Característica | Sockets | Kafka      |
| -------------- | ------- | ---------- |
| Comunicação    | Direta  | Assíncrona |
| Acoplamento    | Alto    | Baixo      |
| Escalabilidade | Baixa   | Alta       |

---

## 🚀 Quando usar essa versão

* Projetos reais de alta escala
* Sistemas orientados a eventos
* Processamento distribuído

---
