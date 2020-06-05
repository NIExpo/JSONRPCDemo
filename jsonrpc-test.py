
import socket
import time
import sys
import json

def read(s, length=2048):
   data = []
   chunk = s.recv(length)
   return chunk

def query_server(server_connection, query_payload, max_response_length = 2048):

   try:
      #CONVERT JSON QUERY TO STR
      PAYLOAD_STR = json.dumps(query_payload)

      #SEND JSON QUERY
      server_connection.send(len(PAYLOAD_STR).to_bytes(4, byteorder = 'big')) #Send Length
      server_connection.send(PAYLOAD_STR.encode()) #Send data

      #GET RESPONSE
      length_data = s.recv(4)
      #print("Message Length :",length_data)
      data = read(s, max_response_length)
      #print("Message Received:", data)

      #CONVERT RESPONSE STR to JSON
      query_response = json.loads(data)

      return query_response
   
   except Exception as e:
      print('Error in function query_server :',e)
      raise


#TCP_IP = '192.168.1.7'
TCP_IP = 'NI-cRIO-9045-01D3CFD5'
TCP_PORT = 6340

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)
s.connect((TCP_IP, TCP_PORT))
time.sleep(1)

#QUERY ECHO MESSAGE
echo_payload = {
      "method": "echo",
      "params": [1,2],
      "jsonrpc": "2.0",
      "id": 10,
      }
rx_data = query_server(s, echo_payload)
print("Result :",rx_data['result'])


#QUERY RANDOM_GENERATOR

#QUERY ANALOG INPUT
ai_payload = {
       "method": "getVoltagesamples",
       "params": {"channel": "Mod2/ai0","samples": 10},
       "jsonrpc": "2.0",
       "id": 10,
    }
rx_data = query_server(s,ai_payload)
print("Result :",rx_data['result'])



