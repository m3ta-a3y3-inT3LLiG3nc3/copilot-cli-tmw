# M3TA-OS Knowledge Vault & Intelligence Core

Welcome to the centralized Knowledge Vault for **M3TA-OS** and **Copilot CLI**. This vault stores structured catalogs of AI tools, production-grade agentic workflows, prompt libraries, and architectural blueprints for team-wide use and autonomous agent execution.

---

## 📂 Vault Structure

```
knowledge-vault/
├── M3TA_OS_Intelligence_Empire_Blueprint.md   # Architectural blueprint for autonomous agents & automations
├── README.md                                  # This documentation
└── maitis-ai/                                 # Reverse-engineered Maitis AI catalog & workflows
    ├── tools.json                             # 763 curated AI tools across 26 categories
    ├── tools.csv                              # CSV format for spreadsheets & databases
    ├── workflows.json                         # 24 production workflows with prompt blocks & tools
    ├── logos.json                             # 665 pre-baked tool brand favicons
    ├── summary.json                           # Category breakdown and pricing stats
    ├── query.py                               # Fast CLI search engine for terminal & agents
    ├── maitis_architecture_blueprint.md       # Technical reverse-engineering report
    └── maitis_platform.html                   # Self-contained interactive web app
```

---

## ⚡ Fast CLI Search Engine (`query.py`)

You can query the entire 763-tool catalog and all 24 workflows directly from the terminal or from any agent script:

```bash
# Search by keyword, use case, or category
python3 knowledge-vault/maitis-ai/query.py "video generation"
python3 knowledge-vault/maitis-ai/query.py "coding"
python3 knowledge-vault/maitis-ai/query.py "sales agent"
```

Sample output displays matching workflows with their prompt summaries, followed by categorized tools with direct URLs and pricing models.

---

## 📊 Catalog Overview

- **Total AI Tools:** 763
- **Primary Categories:** 26 (including AI Agents & Automation, Coding, Video Generation, No-Code Builders, SEO, Chatbots)
- **Workflows:** 24 video-verified step-by-step guides with ready-to-run copyable prompts
- **Pricing Breakdown:**
  - Freemium: 472 tools (61.9%)
  - Paid: 248 tools (32.5%)
  - Free: 41 tools (5.4%)

---

## 🛠️ Usage with GitHub Copilot CLI

When building projects with GitHub Copilot CLI, you or Copilot can reference these files to select optimal AI tools or scaffold workflows:
- Reference `knowledge-vault/maitis-ai/tools.json` to look up available APIs, CLI tools, or libraries.
- Reference `knowledge-vault/maitis-ai/workflows.json` to adapt prompt engineering templates for your tasks.
- Open `knowledge-vault/maitis-ai/maitis_platform.html` in any browser to use the interactive directory and Document-to-Topic admin converter.
