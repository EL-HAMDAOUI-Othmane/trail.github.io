import http.server
import socketserver
import webbrowser
import os
from threading import Timer

# Define the port number
PORT = 8000

# Define the directory to serve files from (the current directory)
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Function to open the web page after a short delay
def open_browser():
    webbrowser.open(f'http://localhost:{PORT}/first.html')

# Run the server
if __name__ == "__main__":
    # Start the server
    handler = CustomHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    # Open the web browser after a short delay
    Timer(1, open_browser).start()

    print(f"Serving files from {DIRECTORY} at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()
