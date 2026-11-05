from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlsplit, unquote
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        range_header = self.headers.get("Range")
        path = Path(self.translate_path(self.path))
        if not range_header or not path.is_file():
            return super().do_GET()

        size = path.stat().st_size
        match = re.fullmatch(r"bytes=(\d*)-(\d*)", range_header.strip())
        start, end = 0, size - 1
        if match and size:
            first, last = match.groups()
            if first:
                start = int(first)
                end = min(int(last), size - 1) if last else size - 1
                valid = start < size and end >= start
            elif last and int(last) > 0:
                start = max(0, size - int(last))
                valid = True
            else:
                valid = False
        else:
            valid = False

        if not valid:
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        length = end - start + 1
        with path.open("rb") as source:
            source.seek(start)
            self.send_response(206)
            self.send_header("Content-Type", self.guess_type(str(path)))
            self.send_header("Content-Length", str(length))
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
            self.end_headers()
            remaining = length
            while remaining:
                chunk = source.read(min(64 * 1024, remaining))
                if not chunk:
                    break
                self.wfile.write(chunk)
                remaining -= len(chunk)


    def translate_path(self, request_target):
        parsed = urlsplit(request_target)
        relative = unquote(parsed.path).lstrip("/")
        base = (ROOT / relative).resolve()

        try:
            base.relative_to(ROOT)
        except ValueError:
            return str(ROOT / "__not_found__")

        # Framer's published route for this page is /demos/city-2. Keep the
        # offline filename available while serving the canonical route too.
        if parsed.path.rstrip("/") == "/demos/city-2":
            return str(ROOT / "www.missingpieceinvites.com/demos/city-2-local.html")

        if parsed.query:
            queried = Path(str(base) + "?" + parsed.query).resolve()
            try:
                queried.relative_to(ROOT)
                if queried.is_file():
                    return str(queried)
            except ValueError:
                pass

        return str(base)

Handler.protocol_version = "HTTP/1.1"
ThreadingHTTPServer.request_queue_size = 128
server = ThreadingHTTPServer(("127.0.0.1", 8000), Handler)

print("City 2 local server running!", flush=True)
print("http://127.0.0.1:8000/www.missingpieceinvites.com/demos/city-2-local.html", flush=True)

server.serve_forever()
