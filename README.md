# Elsight_Assignment

Hellow Elsight team!

Here is some explanation about the assignment. 

*This repository consist of 2 scripts. one is for client side and the other is for server side.
*To run the scripts you will have to supply some command line arguments. some of them are mandatory and some are optional.

*client side arguments:

  address - a mandatory - Represents the adderss to send a ping for. the format should be {IP:port}.
  for example: 127.0.0.1:5000. it sholud be the first argument
  
  message (-m or --message) - optional - A message to send with the ping. if no message was given, a default message will be used.
  
  protocol (-p or --protocol) - optional - The protocol to use for the ping. should be one of the following:
  "UDP" , "udp" ,"TCP" ,"tcp".
  if no protocol was given we will use UDP.
  
  size (-s or --size) - optional - The buffer size for TCP connection. should be grater than 0.
  if no size was spicefied we will set the size to 1024.
  
  timeout (-t or --timeout) - optional - The timeout for TCP connection. should be be grater than 0.
  if no timeout was spicefied we will set the timeout to 10.
  
  
*server side arguments:

  port - a mandatory - represents the port to bind to socket to.
  
  protocol (-p or --protocol) - optional - The protocol to use for the ping should be one of the following:
  "UDP" , "udp" ,"TCP" ,"tcp".
  if no protocol was given we will use UDP.
  
  size (-s or --size) - optional - The buffer size for TCP connection. should be grater than 0.
  if no size was spicefied we will set the size to 1024.
  
  timeout (-t or --timeout) - optional - The timeout for TCP connection should be be grater than 0.
  if no timeout was spicefied we will set the timeout to 10.



  example: 
  
  python server_side_ping.py 5000 -p tcp
  
  python client_side_ping.py 127.0.0.1:5000 -m "Hellow world!"  --protocol tcp -s 2048 -t 120
