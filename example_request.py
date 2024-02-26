import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print(f"Sending request for data from xml file.....")
socket.send_string('example.xml')

example_data = socket.recv()

print(f"xml data received.")
example_data_formatted = example_data.decode('utf-8')
print(example_data_formatted)
