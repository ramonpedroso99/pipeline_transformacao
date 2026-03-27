# 🚀 Pipeline ETL com Python

Este projeto consiste no desenvolvimento de um pipeline ETL (**Extract, Transform, Load**) utilizando Python, com o objetivo de simular um fluxo real de processamento de dados em ambiente corporativo.

---

## 📌 Sobre o projeto

A aplicação realiza a extração de dados fictícios a partir de um arquivo CSV, contendo informações de atendimentos.  

Em seguida, os dados passam por uma etapa de transformação, onde são aplicadas regras de negócio, como filtragem de registros válidos e cálculo de métricas (tempo de atendimento).

Por fim, os dados tratados são carregados em um banco de dados PostgreSQL, garantindo sua persistência de forma estruturada e preparada para análises futuras.

---

## 🔄 Fluxo do Pipeline

```bash
CSV → Extract → Transform → Load → PostgreSQL
