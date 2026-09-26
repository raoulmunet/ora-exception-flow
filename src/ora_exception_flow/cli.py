from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import parse_handlers,render_mermaid

def main(argv=None):
    p=argparse.ArgumentParser(description="Visualize PL/SQL exception handlers.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json","mermaid"),default="text")
    a=p.parse_args(argv)
    handlers=parse_handlers(Path(a.source).read_text(encoding="utf-8"))
    if a.format=="json": print(json.dumps([h.to_dict() for h in handlers],indent=2))
    elif a.format=="mermaid": print(render_mermaid(handlers))
    else:
        for h in handlers:
            print(f"{' OR '.join(h.exceptions)} -> handler -> {'RAISE' if h.reraises else 'handled'}")
    return 0
if __name__=="__main__": raise SystemExit(main())
