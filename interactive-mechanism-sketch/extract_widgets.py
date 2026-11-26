"""extract_widgets.py <session.jsonl> <out_dir> [title_prefix ...] — pull every widget the chat rendered out of a
Claude Code session transcript, BYTE-FOR-BYTE, as `<title>.widget.html` files. A widget is a
`mcp__visualize__show_widget` tool call; its `widget_code` input is what the host rendered. Give title prefixes to
keep only some (for example `first_sketch second_sketch`); give none to take them all. Pair with
`widget_to_standalone.py` to make a page that opens in any browser, then serve it (never `file://`).

Run with `python -I` (the transcript is data, not code). The transcript's path is printed by the session on
request (`~/.claude/projects/<project>/<session-id>.jsonl`)."""
import json
import sys
from pathlib import Path


def main() -> None:
    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    prefixes = tuple(sys.argv[3:])
    out.mkdir(parents=True, exist_ok=True)
    found: dict[str, str] = {}
    with src.open(encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = rec.get("message") or {}
            content = msg.get("content")
            if not isinstance(content, list):
                continue
            for part in content:
                if part.get("type") != "tool_use" or part.get("name") != "mcp__visualize__show_widget":
                    continue
                inp = part.get("input") or {}
                title = inp.get("title", "")
                if prefixes and not title.startswith(prefixes):
                    continue
                found[title] = inp.get("widget_code", "")
    for title, code in found.items():
        (out / f"{title}.widget.html").write_text(code, encoding="utf-8", newline="")
        print(title, len(code))
    if not found:
        print("no widgets matched", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
