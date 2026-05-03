# Guatemalan Executive Branch Monitoring Project

## Project note

This project file was created and structured with support from ChatGPT and significantly updated/implemented using **Gemini CLI**. It is a specialized workspace for journalistic monitoring, integrating automated data extraction with high-fidelity professional reporting.

---

## Project purpose

This project monitors the public communications of the Guatemalan executive branch across official government and presidential social media accounts.

The goal is to identify the latest topics, narratives, announcements, priorities, and framing used by the executive branch in its public-facing communication.

---

## Tool Setup & Custom Commands

This project uses the Gemini CLI custom command registry (`.gemini/commands/`) to provide short-hand access to the monitoring workflow.

### Custom Commands

- **`/sourceCheck`**: Runs the extraction engine to fetch the latest social media posts.
- **`/report`**: Generates a professional branded one-page PDF and HTML monitoring report using the WeasyPrint engine.

---

## Plugins & Extended Skills

This project integrates the **[Claude Skills for Journalism](https://github.com/jamditis/claude-skills-journalism)** plugin system (developed by Joe Amditis).

### AI Writing Detox
- **Mandate:** Eliminate AI signature words (delve, realm, landscape, robust) and patterns to maintain reader trust.
- **Implementation:** Follow the guidelines in `executiveBranchMonitoring/plugins/journalism-skills/ai-writing-detox/SKILL.md` for all summaries and news outputs.

### PDF Playground (Professional Reporting)
- **Branding:** Customized for **Ramón Zamora** (@ramonzamora89).
- **Templates:** Uses high-quality HTML templates from `executiveBranchMonitoring/plugins/journalism-skills/pdf-playground/templates/`.
- **Primary Color:** `#1a73e8` (Substack/Google Blue).
- **High-Fidelity PDF:** Powered by the **WeasyPrint** engine to ensure CSS/formatting parity between HTML and PDF outputs.

---

## Accounts to monitor

### Government of Guatemala
- X/Twitter: https://x.com/GuatemalaGob
- Facebook: https://www.facebook.com/guatemalagob
- TikTok: https://www.tiktok.com/@guatemalagob
- Instagram: https://www.instagram.com/guatemalagob/

### President Bernardo Arévalo
- X/Twitter: https://x.com/BArevalodeLeon
- Facebook: https://www.facebook.com/Dr.BernardoArevalodeLeon
- TikTok: https://www.tiktok.com/@bernardoarevalogt
- Instagram: https://www.instagram.com/bernardoarevalogt/

---

## Output files

The project maintains:

```text
executiveBranchMonitoring/outputs/latest_posts.csv
executiveBranchMonitoring/outputs/posts_archive.csv
executiveBranchMonitoring/outputs/latest_posts.json
executiveBranchMonitoring/outputs/executive_branch_one_pager.html
executiveBranchMonitoring/outputs/executive_branch_one_pager.pdf
```

---

*Last updated and implemented by Gemini CLI on May 2, 2026.*