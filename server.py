#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
from datetime import datetime
from urllib.parse import urlparse, parse_qs

PORT = 64088

class ComparisonHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save-comparison':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                # Create comparisons directory if it doesn't exist
                if not os.path.exists('comparisons'):
                    os.makedirs('comparisons')
                
                # Save the comparison data to a file
                filename = f"comparisons/{data['id']}.json"
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=2)
                
                # Update the registry
                registry_file = 'comparison_registry.json'
                registry = []
                
                # Load existing registry if it exists
                if os.path.exists(registry_file):
                    try:
                        with open(registry_file, 'r') as f:
                            registry = json.load(f)
                    except:
                        registry = []
                
                # Add new entry
                registry_entry = {
                    "datetime": data['datetime'],
                    "title": data['title'],
                    "id": data['id']
                }
                
                # Add description if provided
                if 'description' in data:
                    registry_entry['description'] = data['description']
                
                # Check if entry already exists
                existing = False
                for i, entry in enumerate(registry):
                    if entry['id'] == data['id']:
                        registry[i] = registry_entry
                        existing = True
                        break
                
                if not existing:
                    registry.append(registry_entry)
                
                # Sort by datetime descending
                registry.sort(key=lambda x: x['datetime'], reverse=True)
                
                # Save updated registry
                with open(registry_file, 'w') as f:
                    json.dump(registry, f, indent=2)
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "id": data['id']}).encode())
                
            except Exception as e:
                # Send error response
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

with socketserver.TCPServer(("", PORT), ComparisonHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    httpd.serve_forever()