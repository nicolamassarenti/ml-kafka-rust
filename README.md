# ml-kafka-rust 🚀

_**Note: This is a work in progress. The API is not stable and may change.**_

**An end-to-end example of a streaming pipeline with Kafka, Rust, and AI.**

# In a nutshell

This repository contains an MVP of a streaming architecture that demonstrates how to build an end-to-end system for 
ingesting data from a streaming data source, performing real-time/near-real-time inference, monitoring data flow, and visualizing the data 📊.

The architecture is composed of the following components:
<img src="https://user-images.githubusercontent.com/38035878/202036459-7ff8731e-6eb4-4bad-9c72-e35a38a71591.png" />

* **Data generator**: a Kafka producer that generates data and sends it to a Kafka topic.
* **Kafka**: a distributed streaming platform that stores and processes streams of records.
* **ETL**: a Kafka consumer that reads data from a Kafka topic, performs some transformations, and sends the data to another Kafka topic.
* **Inference server**: an inference server that exposes an AI model
* **Data warehouse**: a database that stores the raw and transformed data.
* **Metrics database**: a database that collects metrics
* **Backend**: a backend that exposes an API to query the data warehouse and the metrics database.
* **Frontend**: a frontend that visualizes the data.

## Authors
* Nicola Massarenti
