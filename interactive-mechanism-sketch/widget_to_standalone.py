"""widget_to_standalone.py <widget.html> <out.html> <title> — wrap a chat-rendered widget (an HTML fragment that
relies on the chat host's CSS variables, SVG text classes and pre-styled controls) into a standalone page that
opens in any browser, light or dark. The widget code is embedded BYTE-FOR-BYTE; only a host shim is added."""
import sys
from pathlib import Path

SHIM = """<style>
:root{--text-primary:#1f1e1d;--text-secondary:#5f5e5a;--text-muted:#888780;--border:rgba(31,30,29,.15);
--border-strong:rgba(31,30,29,.3);--surface-1:#f5f4ef;--surface-2:#fff;--radius:8px;--p:#1f1e1d;--s:#5f5e5a;
--t:#888780;--b:rgba(31,30,29,.15);--bg2:#f5f4ef;--text-accent:#185FA5;--text-danger:#A32D2D;
--font-sans:system-ui,-apple-system,"Segoe UI",sans-serif;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--text-primary:#ecebe6;--text-secondary:#b4b2a9;--text-muted:#888780;
--border:rgba(236,235,230,.15);--border-strong:rgba(236,235,230,.3);--surface-1:#262624;--surface-2:#1f1e1d;
--p:#ecebe6;--s:#b4b2a9;--t:#888780;--b:rgba(236,235,230,.15);--bg2:#262624}}
body{margin:0;padding:24px;background:var(--surface-2);color:var(--text-primary);font:16px/1.6 var(--font-sans)}
main{max-width:680px;margin:0 auto}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
button{font:inherit;font-size:13px;color:var(--text-primary);background:transparent;border:.5px solid var(--border-strong);
border-radius:var(--radius);padding:6px 12px;cursor:pointer}
button:hover{background:var(--surface-1)}
input[type=range]{width:100%}
svg .t,svg .ts,svg .th{fill:var(--text-primary);font-family:var(--font-sans)}
svg .t{font-size:14px}svg .th{font-size:14px;font-weight:500}svg .ts{font-size:12px;fill:var(--text-secondary)}
svg .arr{stroke:var(--t);stroke-width:1.5;fill:none}
svg .leader{stroke:var(--t);stroke-width:.5;stroke-dasharray:3 3;fill:none}
</style>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">"""


def main():
    src, out, title = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    widget = src.read_text(encoding="utf-8")
    page = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        f"<title>{title}</title>\n{SHIM}\n</head>\n<body>\n<main>\n{widget}\n</main>\n</body>\n</html>\n"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"{out} ({len(page)} bytes, widget {len(widget)} bytes embedded unchanged)")


if __name__ == "__main__":
    main()
