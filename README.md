# XML File Microservice

A microservice that returns the data in an XML file

## About

This microservice takes in a request for the filename of a specific XML file and then reads the contents of that file.
The contents of that XML file are then sent back to the requesting program. This microservice uses ZeroMQ to facilitate
the request and response for data.

![UML Sequence Diagram](https://github.com/tevin-voong/XML-Microservice/blob/main/Microservice%20UML%20Diagram.png)

## Setup

Install [ZeroMQ](https://zeromq.org/languages/python/)

## How to request and receive data

Include below code in requesting program

```python
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

Requesting program can request for the specific XML file by using the example code provided below
```python
socket.send_string('example.xml')
```

Make request from main program and then run microservice.py. The contents of the XML file specified will be returned to the program sending the request.