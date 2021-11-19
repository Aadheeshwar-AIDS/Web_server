from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>Aadheeshwar.A</h1>
<h2>21001368</h2>
<h3>Artificial Intelligence and Data Science</h3>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',786)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()