---
name: sourcesCheckSkill
description: Extracts, updates, and archives the latest public posts from Guatemalan executive branch social media accounts. Use when the user asks to run /sourceCheck, check latest executive branch communications, update latest_posts.csv, update posts_archive.csv, or collect posts before creating a monitoring report.
allowed-tools:
  - shell
  - read_file
  - write_file
  - edit_file
---

# Sources Check Skill

## Skill note

This `SKILL.md` file was originally structured with support from ChatGPT and fully implemented using **Gemini CLI**.

---

## Purpose

Use this skill to extract the latest public posts from monitored Guatemalan executive branch accounts.

### Workflow Integration
- **Command:** `/sourceCheck`
- **Configuration:** `.gemini/commands/sourceCheck.toml`
- **Implementation:** `executiveBranchMonitoring/sourcesCheckSkill/scripts/run_extraction.py`

---

## Command name

Invoked through:

```text
/sourceCheck
```

---

*Final implementation by Gemini CLI on May 2, 2026.*