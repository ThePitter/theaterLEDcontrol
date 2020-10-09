from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path[1:]
        if path == "/":
            path = "/index"
        if path.find(".") == -1:
            path += ".html"
        try:
            f = open(path, "r")
            self.send_response(200)
            # self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(f.read(), "utf-8")) #work on getting it to load
        except:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
        print(self.path)


def startServer():
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


if __name__ == "__main__":        
    startServer()