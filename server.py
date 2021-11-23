import http.server
import os
import bpy

from threading import Thread, current_thread
from functools import partial

def ServeDirectoryWithHTTP(directory='.'):
    hostname = 'localhost'
    port = 8000
    directory = os.path.abspath(directory)
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=directory)
    httpd = http.server.HTTPServer((hostname, port), handler, False)
    httpd.allow_reuse_address = True

    httpd.server_bind()
    httpd.server_activate()

    def serve_forever(httpd):
        with httpd:
            httpd.serve_forever()

    thread = Thread(target=serve_forever, args=(httpd, ))
    thread.setDaemon(True)
    thread.start()

app_root = os.path.dirname(bpy.context.space_data.text.filepath)
ServeDirectoryWithHTTP(app_root)
