#!/usr/bin/env python3
"""Validate the public catalog, bilingual archives, relative links, and obvious leaks."""
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parents[1]
TOPICS = {'vla','world-models','memory-skills','rl-adaptation','manipulation-transfer','evaluation'}

def main():
    errors=[]
    data=json.loads((ROOT/'data/papers.json').read_text())
    papers=data['papers']; ids=[p['id'] for p in papers]
    if len(set(ids)) != len(ids): errors.append('Duplicate canonical arXiv IDs')
    counts={d:Counter() for d in data['editions']}
    for p in papers:
        if not re.fullmatch(r'\d{4}\.\d{4,5}',p['id']): errors.append(f"Invalid ID: {p['id']}")
        if not set(p['topics']).issubset(TOPICS) or not p['topics']:errors.append(f"Invalid topics: {p['id']}")
        seen=set()
        for h in p['history']:
            key=(h['date'],h['version'])
            if key in seen:errors.append(f"Duplicate history: {p['id']} {key}")
            seen.add(key)
            s=h['status'];counts[h['date']]['new' if s=='new' else 'supplemental' if 'supplemental' in s else 'revised']+=1
            for suffix in ('.md','.zh-CN.md'):
                f=ROOT/'daily'/(h['date']+suffix)
                if not f.exists():errors.append(f'Missing {f.relative_to(ROOT)}');continue
                t=f.read_text()
                if t.count(f'id="arxiv-{p["id"]}"')!=1:errors.append(f"Missing/duplicate anchor: {f.name} {p['id']}")
                if p['title'] not in t:errors.append(f"Missing exact title: {f.name} {p['id']}")
    for d,c in counts.items():
        for k in ('new','revised','supplemental'):
            if c[k]!=data['editions'][d].get(k,0):errors.append(f'Count mismatch: {d} {k}')
    blocked=[r'docs\.google\.com',r'chatgpt\.com/c/',r'codex://',r'与你的方向',r'你的研究',r'\bJev\b',r'\bgh[pousr]_[A-Za-z0-9]{20,}',r'-----BEGIN .*PRIVATE KEY-----']
    md=list(ROOT.rglob('*.md'))
    for f in md:
        t=f.read_text()
        for pattern in blocked:
            if re.search(pattern,t,re.I):errors.append(f'Potential private content: {f.relative_to(ROOT)} ({pattern})')
        for target in re.findall(r'\]\(([^\s)]+)',t):
            if target.startswith(('https://','http://','mailto:')):continue
            part,_,anchor=target.partition('#');dest=(f.parent/unquote(part)).resolve() if part else f
            if not dest.is_file():errors.append(f'Broken relative link: {f.relative_to(ROOT)} -> {target}');continue
            if anchor and f'id="{unquote(anchor)}"' not in dest.read_text():errors.append(f'Unknown anchor: {f.relative_to(ROOT)} -> {target}')
        if f.name.endswith('.zh-CN.md'):
            pair=f.with_name(f.name.replace('.zh-CN.md','.md'))
            if not pair.exists():errors.append(f'Missing English pair: {f.name}')
            else:
                a=set(re.findall(r'id="arxiv-([^"]+)"',t));b=set(re.findall(r'id="arxiv-([^"]+)"',pair.read_text()))
                if a!=b:errors.append(f'Bilingual anchor mismatch: {f.name}')
    raw=(ROOT/'data/papers.json').read_text()
    for pattern in blocked:
        if re.search(pattern,raw,re.I):errors.append(f'Potential private catalog content: {pattern}')
    if errors:raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(papers)} unique papers, {sum(map(lambda p: len(p["history"]), papers))} dated entries, {len(data["editions"])} editions, {len(md)} Markdown files; catalog, bilingual anchors, relative links, and privacy-pattern checks.')
    print('Scope: static checks only. External HTTP availability and research findings are not revalidated by this script.')
if __name__=='__main__':main()
