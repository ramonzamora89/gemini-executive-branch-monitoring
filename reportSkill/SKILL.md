---
name: reportSkill
description: Creates a concise one-page PDF report from executive branch monitoring data. Use when the user asks to run /report, create a PDF report, summarize latest publications, identify main topics, or generate a one-pager from outputs/latest_posts.csv or outputs/posts_archive.csv.
allowed-tools:
  - shell
  - read_file
  - write_file
  - edit_file
---

# Report Skill

## Skill note

This `SKILL.md` file was originally structured with support from ChatGPT and fully implemented using **Gemini CLI**. It features a high-fidelity reporting system integrating the **PDF Playground** (Center for Cooperative Media) and the **WeasyPrint** PDF engine.

---

## Purpose

Use this skill to create a professional branded one-page PDF and HTML report based on monitoring data.

### Workflow Integration
- **Command:** `/report`
- **Configuration:** `.gemini/commands/report.toml`
- **Implementation:** `executiveBranchMonitoring/reportSkill/scripts/html_generator.py`

### Branding & Design
- **Publisher:** Ramón Zamora
- **Contact:** ramonzamora89@gmail.com
- **Color Scheme:** Primary `#1a73e8`
- **Engine:** WeasyPrint (Ensures HTML/CSS parity in PDF export)
- **Credit:** Template based on Center for Cooperative Media resources.

---

## Command name

Invoked through:

```text
/report
```

---

*Final implementation by Gemini CLI on May 2, 2026.*