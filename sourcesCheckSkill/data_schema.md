# Data Schema and Archive Rules

## Purpose

This file defines the dataset structure, output file behavior, deduplication rules, archive logic, and validation checks for `sourcesCheckSkill`.

---

## Dataset Schema

The following columns are mandatory for `outputs/latest_posts.csv` and `outputs/posts_archive.csv`:

| Column | Type | Description |
| :--- | :--- | :--- |
| `post_id` | String | Unique identifier (platform-native ID or a hash of content+date). |
| `account` | String | The handle or name of the account (e.g., `@GuatemalaGob`). |
| `platform` | String | The social media platform (X, Facebook, TikTok, Instagram). |
| `date` | String | ISO 8601 timestamp (`YYYY-MM-DD HH:MM:SS`). |
| `content` | String | The full text content of the post. |
| `url` | String | Direct link to the publication. |
| `topics` | String | Comma-separated list of identified themes or tags. |
| `sentiment` | String | Analytical sentiment (Positive, Neutral, Negative). |
| `is_announcement` | Boolean | `True` if the post contains an official policy announcement. |

---

## Archive Rules

1. **Deduplication:** Before appending to `posts_archive.csv`, check if `post_id` already exists.
2. **Persistence:** `latest_posts.csv` is overwritten on each `/sourceCheck` run.
3. **Storage:** `posts_archive.csv` grows indefinitely to support historical analysis.
4. **JSON Export:** `latest_posts.json` should mirror the CSV for easy web integration.

---

## Validation Checks

- Ensure `date` is valid and not in the future.
- `url` must start with `http` or `https`.
- `content` must not be empty.