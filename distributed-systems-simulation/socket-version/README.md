# 🔌 Barbearia Distribuída — Versão com Sockets

## 📌 Descrição

Esta é a versão base do projeto, implementada utilizando **sockets TCP** com arquitetura cliente-servidor.

* 💈 Barbeiro → Servidor
* 👨‍🦱 Clientes → Processos independentes

A comunicação ocorre diretamente via rede (`localhost`).

---

## ⚙️ Pré-requisitos

* Python 3.8 ou superior
* Terminal (CMD, PowerShell, Bash)

---

## 📁 Estrutura

```
socket-version/
│
├── barbeiro.py
├── cliente.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ▶️ Passo a passo para execução

### 🔹 1. Acessar a pasta

```
cd socket-version
```

---

### 🔹 2. (Opcional) Criar ambiente virtual

```
python -m venv venv
```

Ativar:

* Windows:

```
venv\Scripts\activate
```

* Linux/Mac:

```
source venv/bin/activate
```

---

### 🔹 3. Rodar o servidor (barbeiro)

```
python barbeiro.py
```

Saída esperada:

```
🚀 Barbearia aberta em 127.0.0.1:5000
😴 Barbeiro dormindo...
```

---

### 🔹 4. Rodar os clientes

Abra **outro terminal**:

```
python cliente.py
```

👉 Você pode abrir vários terminais para simular múltiplos clientes.

---

## 🧪 Testando cenários

* Rodar poucos clientes → barbeiro atende normalmente
* Rodar muitos clientes → fila enche
* Excedente → clientes recebem "CHEIA"

---

## ⚠️ Problemas comuns

* ❌ Porta já em uso → altere no `config.py`
* ❌ Esqueceu de rodar o servidor antes
* ❌ Firewall bloqueando conexão

---

## 🧠 Explicação técnica

* Uso de `socket` para comunicação TCP
* `threading` para múltiplos clientes
* `Lock` para evitar condições de corrida
* Fila FIFO para atendimento

---

## 🎯 Quando usar essa versão

* Entender conceitos básicos
* Demonstrar comunicação direta
* Base para evoluções futuras

---
