# Editorial and update guidelines

[English](CONTRIBUTING.md) | [简体中文](CONTRIBUTING.zh-CN.md) | [Home](README.md)

## Scope and evidence

Cover public research on robot learning and embodied AI, emphasizing VLA, world/action models, reinforcement learning and adaptation, memory, skill accumulation, manipulation, and real-robot transfer. Navigation or multi-robot work belongs when it directly informs these areas. There is no fixed daily quota.

Each substantive entry should include the exact title, versionless arXiv ID and reviewed version, announcement batch, first-submission/revision dates, new/revised/supplemental status, review depth, contribution, author-reported evidence, limitations, and public paper/project/code links. Do not silently upgrade abstract-only review to full-text verification. Distinguish simulation, replay/offline trajectory evaluation, and real closed-loop deployment.

For revisions, compare the relevant versions and identify a verifiable substantive change. Do not present old metrics as new or infer that unchanged abstracts prove unchanged methods. Record incomplete comparisons and unresolved access gaps. Keep code release claims separate from project websites, placeholder buttons, empty repositories, and reproducible implementations.

## Bilingual layout

- `README.md` is the English landing page; `README.zh-CN.md` is its Chinese counterpart.
- `daily/YYYY-MM-DD.md` and `daily/YYYY-MM-DD.zh-CN.md` preserve full dated editions, including scope notes and caveats.
- `topics/` contains bilingual navigation summaries linking to the full archives.
- `data/papers.json` contains one record per versionless arXiv ID, public summaries, topic tags, and dated history.

Maintain equivalent factual content in both languages and reciprocal links. Keep paper titles and benchmark/model names recognizable. Each paper entry has the stable anchor `arxiv-ID`.

## Updating safely

1. Read the current default-branch files before editing. Reconcile concurrent changes; never overwrite unrelated contributions.
2. Add new dated entries and both language versions. Preserve previous archive content. Corrections should be explicit; later revisions get a new dated history entry.
3. Update the canonical catalog and edition counts. A review completed later for an earlier announcement batch must retain both dates and supplemental status.
4. Run `python scripts/build_indexes.py` and `python scripts/check_content.py` from the repository root.
5. Review the diff for bilingual parity, private information, metric denominators, code-status claims, and working relative links. Commit only the intended public files, then verify the remote commit and contents.

Do not include personal notes, private research plans, private document/conversation links, credentials, or personalized statements about an individual's research. Public research summaries should be objective and source-attributed, without inferring anyone's endorsement.

Live arXiv category pages change over time. Preserve reviewed version links and archive dates rather than treating today's listing as a historical snapshot. A delayed announcement, a routine non-announcement day, and an announced batch with no relevant papers are different states; do not fabricate a paper-filled or empty edition before checking the actual batch.

No credentials or GitHub Actions are required by this repository. The standard-library scripts only rebuild local navigation and validate content; they do not fetch sources or publish changes.
