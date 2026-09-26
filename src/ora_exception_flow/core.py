from __future__ import annotations
from dataclasses import dataclass, asdict
import re

@dataclass(frozen=True)
class Handler:
    exceptions: list[str]
    reraises: bool
    body: str
    def to_dict(self): return asdict(self)

def parse_handlers(plsql: str) -> list[Handler]:
    m=re.search(r"\bEXCEPTION\b(.*?)(?:\bEND\b\s*;|\Z)",plsql,re.I|re.S)
    if not m: return []
    section=m.group(1)
    matches=list(re.finditer(r"\bWHEN\s+(.+?)\s+THEN\b",section,re.I|re.S))
    handlers=[]
    for i,h in enumerate(matches):
        body=section[h.end(): matches[i+1].start() if i+1<len(matches) else len(section)]
        names=[x.strip().upper() for x in re.split(r"\s+OR\s+",h.group(1),flags=re.I)]
        reraises=bool(re.search(r"\bRAISE\s*;",body,re.I))
        handlers.append(Handler(names,reraises,body.strip()))
    return handlers

def render_mermaid(handlers:list[Handler])->str:
    lines=["flowchart LR"]
    for i,h in enumerate(handlers):
        label=" OR ".join(h.exceptions)
        result="RAISE" if h.reraises else "HANDLED"
        lines += [f'    E{i}["{label}"] --> H{i}["handler"]', f'    H{i} --> R{i}["{result}"]']
    if not handlers: lines.append('    N0["No EXCEPTION handlers detected"]')
    return "\n".join(lines)
