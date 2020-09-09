#Use to create local host
#import SimpleHTTPServer
import socketserver
import http.server                        
from http import *

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    ".js": "application/javascript",
});

httpd = socketserver.TCPServer(("", PORT), Handler)

print ("Serving at port", PORT)
print(Handler.extensions_map[".js"])
httpd.serve_forever()