#!/usr/bin/env python
"""sketch_answers_server.py - serve a folder of sketches; save each sketch's answers beside it.

    py -3 sketch_answers_server.py --dir <folder with the sketch .html files> [--port 8815]

A sketch with the feedback block (functional-ui-sketch, "Feedback on every card") GETs and POSTs
`/answers/<sketch file name>`; the answers live in `<folder>/<sketch name>.answers.json`:
    {saved, sketch, answers: {<card id>: {choice: "yes"|"no"|"change", note}}, counts: {cards, answered}}
Rewritten atomically on every change; the agent reads that file, never asks the owner to export.
Opened without this server (file://), the sketch keeps answers in the browser and offers a download.
Stop it by its command line (sketch_answers_server.py) when the answers are in.
"""
import argparse
import json
import mimetypes
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--port", type=int, default=8815)
    a = ap.parse_args()
    root = os.path.abspath(a.dir)

    class H(BaseHTTPRequestHandler):
        def log_message(self, *x):
            pass

        def send(self, code, body, ctype="application/json"):
            b = body if isinstance(body, bytes) else json.dumps(body).encode()
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(b)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(b)

        def answers_file(self, name):
            name = os.path.basename(name)                      # a sketch in this folder, nothing else
            if not name.endswith(".html") or not os.path.isfile(os.path.join(root, name)):
                return None
            return os.path.join(root, name[:-5] + ".answers.json")

        def do_GET(self):
            path = unquote(self.path.split("?")[0])
            if path.startswith("/answers/"):
                f = self.answers_file(path[len("/answers/"):])
                if not f:
                    return self.send(404, {"error": "no such sketch"})
                return self.send(200, json.load(open(f, encoding="utf-8")) if os.path.exists(f) else {"answers": {}})
            f = os.path.normpath(os.path.join(root, path.lstrip("/") or "index.html"))
            if not f.startswith(root) or not os.path.isfile(f):
                listing = "".join('<li><a href="/%s">%s</a></li>' % (n, n) for n in sorted(os.listdir(root)) if n.endswith(".html"))
                return self.send(200 if path == "/" else 404, ("<ul>%s</ul>" % listing).encode(), "text/html; charset=utf-8")
            self.send(200, open(f, "rb").read(), mimetypes.guess_type(f)[0] or "application/octet-stream")

        def do_POST(self):
            path = unquote(self.path.split("?")[0])
            f = self.answers_file(path[len("/answers/"):]) if path.startswith("/answers/") else None
            if not f:
                return self.send(404, {"error": "no such sketch"})
            data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            data["saved"] = time.strftime("%Y-%m-%d %H:%M:%S")
            tmp = f + ".tmp"
            json.dump(data, open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
            os.replace(tmp, f)                                 # never a half-written answers file
            self.send(200, {"saved": data["saved"]})

    print("sketches:", root, "-> http://127.0.0.1:%d/" % a.port, flush=True)
    ThreadingHTTPServer(("127.0.0.1", a.port), H).serve_forever()


if __name__ == "__main__":
    main()
