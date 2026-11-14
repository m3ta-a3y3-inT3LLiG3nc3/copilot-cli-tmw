#!/usr/bin/env python3
"""
M3TA-OS Knowledge Vault Query Engine
Fast semantic / keyword retrieval across 763 AI tools and 24 master workflows.
"""
import sys, json, os

VAULT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    with open(os.path.join(VAULT_DIR, "tools.json"), "r") as f:
        tools = json.load(f)
    with open(os.path.join(VAULT_DIR, "workflows.json"), "r") as f:
        workflows = json.load(f)
    return tools, workflows

def search_tools(query, limit=10):
    tools, _ = load_data()
    q = query.lower()
    results = []
    for t in tools:
        score = 0
        name = t.get("name", "").lower()
        cat = t.get("category", "").lower()
        tag = t.get("tag", "").lower()
        desc = t.get("description", "").lower()
        kw = t.get("keywords", "").lower()

        if q in name: score += 10
        if q in cat: score += 5
        if q in tag: score += 4
        if q in kw: score += 3
        if q in desc: score += 1

        if score > 0:
            results.append((score, t))
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:limit]]

def search_workflows(query, limit=5):
    _, workflows = load_data()
    q = query.lower()
    results = []
    for w in workflows:
        score = 0
        title = w.get("title", "").lower()
        cat = w.get("category", "").lower()
        summary = w.get("summary", "").lower()
        if q in title: score += 10
        if q in cat: score += 5
        if q in summary: score += 3
        if score > 0:
            results.append((score, w))
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:limit]]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: query.py <search-terms>")
        sys.exit(1)
    q = " ".join(sys.argv[1:])
    print(f"\n🔍 Searching M3TA-OS Knowledge Vault for: '{q}'\n" + "="*50)
    
    w_matches = search_workflows(q)
    if w_matches:
        print(f"\n📚 WORKFLOWS FOUND ({len(w_matches)}):")
        for w in w_matches:
            print(f"  • [{w['category']}] {w['title']}")
            print(f"    Summary: {w['summary'][:120]}...")
            
    t_matches = search_tools(q)
    if t_matches:
        print(f"\n⚡ TOOLS FOUND ({len(t_matches)}):")
        for t in t_matches:
            print(f"  • {t['name']} ({t.get('pricing', 'N/A')}) — {t.get('tag', '')}")
            print(f"    Category: {t.get('category')} | URL: {t.get('url')}")
    
    if not w_matches and not t_matches:
        print("No matches found in vault.")
