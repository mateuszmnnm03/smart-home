# Distributed Smart Home Platform

Polyglot distributed IoT platform built with **Java**, **Python**, and **ZeroC Ice**.  
The project simulates a smart home environment where multiple devices can be remotely controlled through RPC communication using strongly typed Slice interfaces.

## Features

- Distributed client-server architecture
- Java-based concurrent server
- Python client application
- ZeroC Ice RPC communication
- Slice IDL contracts for cross-language interoperability
- Thread-safe servant management
- Dynamic object routing using Ice Object Adapters
- Location-transparent remote method invocation
- Smart home device simulation

## Technologies

- Java
- Python
- ZeroC Ice
- Slice IDL
- RPC
- Docker

---

# Project Structure

```text
smart-home/
│
├── client.py
│
├── slice/
│   └── home.ice
│
├── src/
│   └── sr/
│       └── ice/
│           └── server/
│               ├── AbstractDevice.java
│               ├── CameraI.java
│               ├── CleanerI.java
│               ├── GroundHeaterI.java
│               ├── HeaterI.java
│               ├── RadiatorI.java
│               └── Server.java
│
├── Dockerfile
├── docker-compose.yml
│
└── README.md
```

---

# Architecture

The system consists of:

## Java Server

The server exposes smart home devices as remote Ice objects.

Implemented devices include:

- Camera
- Cleaner
- Ground Heater
- Heater
- Radiator

The server:
- registers servants inside Ice Object Adapters,
- handles concurrent requests,
- manages remote object identities,
- exposes strongly typed interfaces generated from Slice definitions.

## Python Client

The Python client connects to the Ice server using typed proxies and allows remote interaction with smart home devices.

The client demonstrates:
- remote method invocation,
- safe proxy casting,
- distributed communication between different programming languages.

---

# Communication Flow

```text
Python Client
      │
      │  RPC Calls
      ▼
ZeroC Ice Middleware
      │
      ▼
Java Ice Server
      │
      ▼
Smart Home Devices
```

---

# Requirements

## Java
- JDK 17+ (or compatible version)

## Python
- Python 3.10+

## ZeroC Ice
Install Ice for both Java and Python.

Official documentation:

- https://zeroc.com/ice
- https://zeroc.com/downloads/ice

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/mateuszmnnm03/smart-home.git
cd smart-home
```

---

## 2. Generate Slice bindings

### Java

```bash
slice2java slice/home.ice
```

### Python

```bash
slice2py slice/home.ice
```

---

# Running the Server

## Compile Java sources

```bash
javac src/sr/ice/server/*.java
```

## Start the server

```bash
java sr.ice.server.Server
```

The server initializes Ice communicators, creates object adapters, and registers smart device servants.

---

# Running the Client

```bash
python client.py
```

The client connects to the remote Ice server and allows interaction with available smart home devices.

---

# Docker

The project also supports Docker deployment.

## Build and run

```bash
docker compose up --build
```

---

# Example Functionality

Possible operations include:

- enabling/disabling heaters,
- reading camera state,
- controlling cleaning devices,
- changing temperature settings,
- querying remote device status.

---

# Distributed Systems Concepts Demonstrated

- RPC-based distributed architecture
- Interface Definition Language (Slice)
- Typed remote proxies
- Object identities
- Object adapters
- Concurrent request handling
- Polyglot interoperability
- Location transparency
- Client-server communication

---

# Learning Goals

This project was created to explore practical distributed systems concepts, including:
- middleware-based communication,
- cross-language interoperability,
- concurrent server design,
- remote object management,
- scalable IoT-oriented architectures.
