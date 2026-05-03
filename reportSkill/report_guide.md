# Report Guide

## Purpose

This file defines the structure, style, analytical rules, and validation standards for one-page monitoring reports created by `reportSkill`.

Use this file when Gemini CLI needs to:

- Generate a one-page PDF report.
- Structure the monitoring report.
- Identify main topics.
- Select relevant data points.
- Write concise monitoring summaries.
- Apply the monitoring-focused Smart Brevity style.
- Validate the report before saving it.

---

## Report type

The default report is a one-pager.

It should summarize the latest public social media publications collected by `sourcesCheckSkill`.

The report should focus on:

1. What was published.
2. What topics appeared.
3. Which accounts and platforms were active.
4. What relevant data points stand out.
5. Which publications are representative.
6. What limitations affect the reading of the data.

This is a monitoring report, not a news article.

---

## Input files

Default input:

```text
outputs/latest_posts.csv