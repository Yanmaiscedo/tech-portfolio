# 💈 Barbearia Distribuída — Projeto Completo

## 📌 Visão Geral

Este repositório apresenta diferentes implementações do clássico problema de concorrência conhecido como **Barbeiro Dorminhoco**, aplicando conceitos fundamentais de **Sistemas Distribuídos**.

O projeto foi desenvolvido em três versões, cada uma evoluindo em complexidade e arquitetura:

* 🔌 Comunicação direta com sockets
* 🐳 Containerização com Docker
* 📡 Mensageria assíncrona com Kafka

---

## 🧠 Objetivo

Demonstrar, na prática, diferentes abordagens para comunicação entre processos distribuídos, explorando:

* Comunicação síncrona vs assíncrona
* Acoplamento entre componentes
* Escalabilidade
* Concorrência e sincronização

---

## 🏗️ Estrutura do Repositório

```bash
barbearia-distribuida/
│
├── socket-version/     # Versão base com TCP sockets
│   └── README.md
│
├── docker-version/     # Versão containerizada
│   └── README.md
│
├── kafka-version/      # Versão com mensageria
│   └── README.md
│
└── README.md           # Este arquivo (visão geral)
```

---

## 🔗 Versões do Projeto

### 🔌 Versão 1 — Sockets (Base)

Implementação clássica utilizando **arquitetura cliente-servidor** com sockets TCP.

📌 Características:

* Comunicação direta entre cliente e servidor
* Baixo nível de abstração
* Controle manual de concorrência

  👉 [Acessar projeto](./socket-version/README.md)

---

### 🐳 Versão 2 — Docker (Ambiente Distribuído)

Evolução da versão com sockets, agora executando em containers utilizando Docker.

📌 Características:

* Simulação de múltiplas máquinas
* Isolamento de processos
* Rede virtual entre serviços

  👉 [Acessar projeto](./docker-version/README.md)

---

### 📡 Versão 3 — Kafka (Mensageria Assíncrona)

Implementação utilizando Apache Kafka como broker de mensagens.

📌 Características:

* Comunicação assíncrona (event-driven)
* Baixo acoplamento entre componentes
* Alta escalabilidade

  👉 [Acessar projeto](./kafka-version/README.md)

---

## ⚖️ Comparação entre as versões

| Critério           | Sockets | Docker        | Kafka      |
| ------------------ | ------- | ------------- | ---------- |
| Comunicação        | Direta  | Direta        | Assíncrona |
| Acoplamento        | Alto    | Médio         | Baixo      |
| Escalabilidade     | Baixa   | Média         | Alta       |
| Complexidade       | Baixa   | Média         | Alta       |
| Nível profissional | Básico  | Intermediário | Avançado   |

---

## 🧩 Problema Modelado

O sistema simula uma barbearia com:

* 💈 1 barbeiro
* 🪑 3 cadeiras de espera
* 👨‍🦱 Clientes chegando de forma concorrente

Regras:

* Se não há clientes → barbeiro dorme
* Se chega cliente → barbeiro acorda
* Se há vagas → cliente espera
* Se está cheio → cliente vai embora

---

## 🚀 Como começar

1. Escolha uma versão para executar
2. Acesse o diretório correspondente
3. Siga as instruções do README específico

---

## 🧠 Conceitos Aplicados

* Sistemas distribuídos
* Concorrência e sincronização
* Comunicação entre processos
* Arquitetura cliente-servidor
* Event-driven architecture

---

## 🎯 Sugestão de Apresentação

Se este projeto for apresentado:

1. Comece pela versão **Sockets** (fundamentos)
2. Evolua para **Docker** (ambiente distribuído)
3. Finalize com **Kafka** (arquitetura moderna)

👉 Isso mostra evolução de conhecimento (professores adoram isso)

---

## 🚀 Possíveis Extensões

* Múltiplos barbeiros (load balancing)
* Interface web em tempo real
* Deploy em nuvem
* Monitoramento de eventos