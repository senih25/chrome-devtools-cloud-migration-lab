from __future__ import annotations

import argparse
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


SECURITY_HEADERS = {
    "Content-Security-Policy": (
        "default-src 'self'; "
        "base-uri 'self'; "
        "connect-src 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none'; "
        "img-src 'self' data:; "
        "object-src 'none'; "
        "script-src 'self'; "
        "style-src 'self'"
    ),
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "no-referrer-when-downgrade",
    "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
}


class SecurityHeadersHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        for header, value in SECURITY_HEADERS.items():
            self.send_header(header, value)
        super().end_headers()


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve Module 10 demo locally.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8090)
    args = parser.parse_args()

    os.chdir(Path(__file__).resolve().parent)
    server = ThreadingHTTPServer((args.host, args.port), SecurityHeadersHandler)
    print(f"Serving Module 10 demo at http://{args.host}:{args.port}/")
    server.serve_forever()


if __name__ == "__main__":
    main()
