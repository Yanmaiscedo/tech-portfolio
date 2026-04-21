# 🐳 Barbearia Distribuída — Versão com Docker

## 📌 Descrição

Esta versão utiliza Docker para simular um ambiente distribuído com múltiplos containers.

* 💈 Barbeiro → container servidor
* 👨‍🦱 Clientes → múltiplos containers

---

## ⚙️ Pré-requisitos

* Docker instalado
* Docker Compose

Verificar instalação:

```
docker --version
docker-compose --version
```

---

## 📁 Estrutura

```
docker-version/
│
├── app/
│   ├── barbeiro.py
│   ├── cliente.py
│   ├── config.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ▶️ Passo a passo para execução

### 🔹 1. Acessar a pasta

```
cd docker-version
```

---

### 🔹 2. Build dos containers

```
docker-compose build
```

---

### 🔹 3. Subir o sistema

```
docker-compose up --scale cliente=5
```

👉 Isso cria:

* 1 barbeiro
* 5 clientes simultâneos

---

## 🧪 O que você verá

* Containers iniciando
* Clientes conectando automaticamente
* Fila sendo gerenciada
* Atendimento acontecendo

---

## 🔄 Parar o sistema

```
CTRL + C
docker-compose down
```

---

## ⚠️ Problemas comuns

* ❌ Docker não iniciado
* ❌ Porta 5000 ocupada
* ❌ Erro de build → limpar cache:

```
docker-compose down --rmi all
docker-compose build
```

---

## 🧠 Explicação técnica

* Containers simulam máquinas distintas
* Rede Docker permite comunicação via nome do serviço
* Escalabilidade com `--scale`

---

## 🎯 Diferencial dessa versão

* Ambiente distribuído real
* Isolamento de processos
* Mais próximo de produção

---
