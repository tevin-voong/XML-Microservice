import zmq
from bs4 import BeautifulSoup

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

xml_request = socket.recv()

print("Request received. Sending specific xml file data back.")
xml_filename = xml_request.decode('utf-8')

with open('%s' % xml_filename, 'r') as example:
    example_data = example.read()

xml_data = BeautifulSoup(example_data, "xml")
socket.send_string(xml_data.prettify())
