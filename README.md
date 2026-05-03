# Gemini Executive Branch Monitoring Extension

A Gemini CLI extension for monitoring executive branch, politics, law, and government-related trends.

This extension packages two custom Gemini CLI slash commands:

- `/sourceCheck`
- `/report`

Together, they support a workflow for identifying trending political or government topics, checking the sources behind those trends, and generating short monitoring reports.

The extension was designed for journalism, civic monitoring, public affairs, and research workflows where the goal is to describe what is being discussed, identify what information is available, and produce clear, source-driven outputs.

---

## What this extension does

This extension helps with two main tasks:

1. **Source checking**
   - Reviews trending topics or user-provided links.
   - Identifies the sources driving the trend.
   - Checks whether the available information is clear, incomplete, duplicated, or noisy.
   - Produces a short summary of what was checked and what remains uncertain.

2. **Report generation**
   - Uses checked sources or available monitoring data.
   - Generates a concise monitoring report.
   - Explains what is trending, why it matters, and what information supports the analysis.
   - Includes a short methodology note.

---

## Included custom commands

### `/sourceCheck`

Runs the source checking workflow.

Use this command when you want Gemini CLI to review a topic, trend, article, or set of sources before writing a report.

#### Example uses

/sourceCheck revisar tendencias de política y gobierno de hoy
/sourceCheck revisar esta nota y verificar qué fuentes la están impulsando
/sourceCheck revisar los temas de Law and Government en Google Trends para hoy

## What the command does

The /sourceCheck command instructs Gemini CLI to:

1. Read the project context.
2. Follow the workflow in sourcesCheckSkill/SKILL.md.
3. Review the source checking guide and related files.
4. Identify relevant sources, links, posts, or trend data.
5. Separate verified information from uncertainty.
6. Save or update outputs only when the workflow instructs it to do so.
7. Summarize what was checked.

### Related files
sourcesCheckSkill/
|- SKILL.md
|- hooks.md
|- data_schema.md
|- scripts/

### Expected output

The command should produce a brief source checking summary that includes:

Topic or trend reviewed
Sources checked
Main findings
Missing information
Possible noise or irrelevant results
Recommended next step

Example output structure:

## Source check summary

**Topic reviewed:** [topic]

**Sources checked:**
- [source 1]
- [source 2]
- [source 3]

**Main finding:**
[Short summary of what the available sources show.]

**Uncertainty or gaps:**
[What could not be confirmed or what needs more review.]

**Recommended next step:**
[Whether to generate a report, search again, or refine the topic.]

## /report
### Generates a monitoring report.

Use this command after running /sourceCheck, or when you already have enough source material to generate a short monitoring report.

### Example uses
/report generar reporte de tendencias políticas de hoy
/report crear un one-pager con las tres tendencias principales
/report generar reporte sobre temas de política, gobierno y leyes en Google Trends

### What the command does

The /report command instructs Gemini CLI to:

1. Read the project context.
2. Follow the reporting workflow in reportSkill/SKILL.md.
3. Review available source checking outputs if needed.
4. Use the latest available data unless the user provides a date or topic.
5. Generate a concise monitoring report.
6. Include a short methodology note.
7. Clearly flag missing data, weak sources, or uncertainty.

### Related files
reportSkill/
|- SKILL.md
|- hooks.md
|- report_guide.md
|- scripts/
Expected output

The command should produce a monitoring report with a structure similar to:

# Executive Branch Monitoring Report

## 1. Main trend

[Short explanation of the trend.]

## 2. Why it matters

[Why the trend is relevant for political, civic, or public affairs monitoring.]

## 3. Sources driving the conversation

- [Source 1]
- [Source 2]
- [Source 3]

## 4. Trend behavior

[Brief explanation of how the topic behaved over time, if trend data is available.]

## 5. Notes and caveats

[What is incomplete, uncertain, noisy, or still needs verification.]

## Methodology note

This report was prepared by reviewing trending topics, filtering irrelevant or duplicated results, and summarizing the sources that appeared to be driving attention during the review period.
Recommended workflow

The preferred workflow is to run a source check first:

/sourceCheck [topic, date, trend, or source set]

Then generate the report:

/report [specific report request]

For example:

/sourceCheck revisar las tendencias de política y gobierno de hoy

Then:

/report generar un reporte corto con las tres tendencias principales

## Repository structure
gemini-executive-branch-monitoring/
|- gemini-extension.json
|- GEMINI.md
|- README.md
|- commands/
|  |- sourceCheck.toml
|  |- report.toml
|- PROJECT.md
|- sourcesCheckSkill/
|  |- SKILL.md
|  |- hooks.md
|  |- data_schema.md
|  |- scripts/
|- reportSkill/
   |- SKILL.md
   |- hooks.md
   |- report_guide.md
   |- scripts/

## Installation

Install this extension from GitHub using Gemini CLI:

gemini extensions install https://github.com/ramonzamora89/gemini-executive-branch-monitoring

After installing, restart Gemini CLI.

Then check that the extension is available:

/extensions list
Local development

To test this extension locally before publishing it to GitHub, go to the extension folder:

cd /path/to/gemini-executive-branch-monitoring

Then link it locally:

gemini extensions link .

Restart Gemini CLI and test the commands:

/sourceCheck test
/report test

If the commands do not appear, reload commands inside Gemini CLI:

/commands reload

## Extension manifest

This extension uses a gemini-extension.json file:

{
  "name": "gemini-executive-branch-monitoring",
  "version": "0.1.0",
  "description": "Gemini CLI extension for executive branch monitoring, source checking, and report generation.",
  "contextFileName": "GEMINI.md"
}

The GEMINI.md file provides general context and behavior instructions for the extension.

## Optional companion plugin

This workflow was developed alongside journalism-oriented skills and templates, including materials from the Center for Cooperative Media.

Those external materials are not bundled in this repository.

If a plugins/journalism-skills/ folder exists in the active workspace, Gemini may use it for:

Journalism writing guidance
HTML templates
PDF workflows
AI-writing cleanup
One-pager and report formatting

The companion plugin is available here:

https://github.com/jamditis/claude-skills-journalism/tree/master

If that folder is not available, this extension should continue using only its own commands and skills.

## Generated outputs

This extension may generate files such as:

outputs/
|- executive_branch_report_YYYY-MM-DD.md
|- executive_branch_one_pager.html
|- executive_branch_one_pager.pdf
|- latest_posts.csv
|- latest_posts.json
|- posts_archive.csv

Generated outputs should normally not be committed to GitHub.

Recommended .gitignore:

outputs/
*.pdf
*.html
*.csv
*.json
!gemini-extension.json
.env
.DS_Store
node_modules/

## Security note

Before installing any Gemini CLI extension, review its files.

This extension currently includes:

Custom slash commands
Project context files
Skill instructions
Optional scripts

If scripts are added or modified, inspect them before running the workflow.

Do not commit API keys, credentials, browser cookies, or private monitoring data to this repository.

Suggested usage principles

When using this extension, Gemini CLI should:

Be source-driven.
Separate verified facts from interpretation.
Describe what is being said without assuming who is right.
Identify uncertainty clearly.
Avoid overclaiming.
Prefer concise monitoring language.
Include methodology notes when generating reports.
Flag incomplete, duplicated, or noisy information.
Version

## Current version:

0.1.0

## License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Acknowledgment

This README file was written with the help of ChatGPT.