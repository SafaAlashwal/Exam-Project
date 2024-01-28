import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import frappe

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        data = json.loads(post_data)

        name = data["name"]
        email = data["email"]

        # ≈÷«›… «·»Ì«‰«  ≈·Ï Frappe ERPNext
        doc = frappe.get_doc({
            "doctype": "CustomDocType",
            "name1": name,
            "email": email
        })
        doc.insert()

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting server...")
    httpd.serve_forever()

if __name__ == "__main__":
    frappe.init()
    run()