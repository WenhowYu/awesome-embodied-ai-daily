#!/usr/bin/env python3
"""Rebuild bilingual navigation from public data/papers.json (standard library only)."""
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TOPICS = {
    'vla': ('Vision-language-action models', '视觉—语言—动作模型'),
    'world-models': ('World models and world-action models', '世界模型与世界动作模型'),
    'memory-skills': ('Memory, skills, and continual learning', '记忆、技能与持续学习'),
    'rl-adaptation': ('Reinforcement learning and adaptation', '强化学习与适应'),
    'manipulation-transfer': ('Manipulation and real-robot transfer', '操作与真实机器人迁移'),
    'evaluation': ('Evaluation, robustness, and safety', '评测、鲁棒性与安全'),
}
def main():
    data = json.loads((ROOT / 'data/papers.json').read_text())
    papers = sorted(data['papers'], key=lambda p: (p['latest_covered'], p['id']), reverse=True)
    editions = data['editions']
    dates = sorted(editions, reverse=True)
    latest = dates[0]
    n = len(papers)
    count = sum(len(p['history']) for p in papers)
    for lang in ('en', 'zh'):
        zh = lang == 'zh'
        suffix = '.zh-CN.md' if zh else '.md'
        other = 'README.md' if zh else 'README.zh-CN.md'
        labels = '[English](README.md) | [简体中文](README.zh-CN.md)'
        title = '# Awesome Embodied AI Daily\n\n' if not zh else '# Awesome Embodied AI Daily · 具身智能每日论文\n\n'
        intro = ('面向公众的双语机器人学习与具身智能论文精选，关注 VLA、WAM／世界模型、强化学习与测试时适应、经验记忆、技能积累及真实机器人迁移。英文为默认语言。' if zh else 'A bilingual, public-facing reading list for robot learning and embodied AI: VLA, WAM/world models, reinforcement learning and test-time adaptation, memory, skill accumulation, and real-robot transfer. English is the default language.')
        stats = (f'最新覆盖公告：**{latest}**。共 **{n} 篇独立论文**、**{count} 条有实质内容的日期记录**、**{len(dates)} 期归档**。' if zh else f'Latest covered announcement: **{latest}**. **{n} unique papers**, **{count} substantive dated entries**, and **{len(dates)} archived editions**.')
        opening = title + labels + '\n\n' + intro + '\n\n' + stats + '\n\n'
        opening += ('收录不代表对论文或作者的背书。所有量化结果均为作者报告，非独立复现。请结合每篇归档中的限制、实验设置、版本与阅读深度理解结果。\n\n' if zh else 'Inclusion is not an endorsement of a paper or its authors. Numerical results are author-reported, not independently reproduced. Read each archive entry for limitations, experimental conditions, version, and review depth.\n\n')
        opening += ('## 浏览\n\n' if zh else '## Browse\n\n')
        opening += f"- [{'主题索引' if zh else 'Topic index'}](topics/README{suffix})\n- [{'每日完整归档' if zh else 'Full daily archives'}](daily/README{suffix})\n- [{'收录与更新规范' if zh else 'Editorial and update guidelines'}](CONTRIBUTING{suffix})\n- [{'机器可读论文目录' if zh else 'Machine-readable catalog'}](data/papers.json)\n\n"
        opening += ('## 研究主题\n\n' if zh else '## Topics\n\n')
        for slug, titles in TOPICS.items():
            total = sum(slug in p['topics'] for p in papers)
            opening += f'- [{titles[zh]}](topics/{slug}{suffix}) · {total}\n'
        opening += ('\n主题可以交叉；每篇论文在机器可读目录中按不带版本号的 arXiv ID 仅保留一个记录，所有已收录版本与日期保留在历史中。\n\n' if zh else '\nTopics overlap. The catalog has one canonical record per versionless arXiv ID, with all covered versions and dates retained in its history.\n\n')
        opening += ('## 每日归档\n\n' if zh else '## Daily archives\n\n')
        for date in dates:
            counts = editions[date]
            note = (f"{counts['new']} 篇新论文、{counts['revised']} 项修订" if zh else f"{counts['new']} new papers, {counts['revised']} revisions")
            if counts.get('supplemental'):note += (f"、{counts['supplemental']} 项前期补核" if zh else f", {counts['supplemental']} earlier-batch supplemental review")
            opening += f'- [{date}](daily/{date}{suffix}) · {note}\n'
        opening += ('\n## 如何阅读\n\n- 归档按公告批次组织；首稿提交和修订日期另外标注。10 月 21 日归档中的 PrismWAM 为 10 月 20 日批次补核。\n- 明确区分新论文、实质修订与仅元数据／格式变化，避免把旧结果当新结果。\n- 保留摘要初筛与正文核对的区别；可访问仓库不等于代码完整或可复现。\n- 所有代码／项目状态按各期记录的核验日期理解，后续可能变化。\n- 不设固定收录数量；只收录与主题相关且证据足以描述的内容。覆盖范围与缺口写在各期归档中，10 月 19 日不保证跨分类完整覆盖。\n\n论文、代码与项目的权利归原作者或相应权利人所有。引用研究请优先引用原论文。\n' if zh else '\n## How to read this list\n\n- Archives follow announcement batches; first-submission and revision dates are recorded separately. PrismWAM in the October 21 archive is a supplemental review of the October 20 batch.\n- New papers, substantive revisions, and metadata/format-only changes are distinguished so old results are not presented as new.\n- Abstract screening is distinguished from selected full-text checks. An accessible repository is not proof of complete or reproducible code.\n- Code/project status is historical as of the review recorded in each edition and may change later.\n- There is no fixed inclusion quota. Scope and gaps are recorded per edition; October 19 does not claim complete cross-category coverage.\n\nPapers, code, and projects remain the work of their respective authors and rights holders. Cite the original papers when referencing the research.\n')
        (ROOT / ('README' + suffix)).write_text(opening)
        daily = ('# 每日归档\n\n' if zh else '# Daily archives\n\n') + labels + f" | [{'首页' if zh else 'Home'}](../README{suffix})\n\n"
        daily += ('完整保留各期有实质内容的条目、实验条件与限制；后续修订不会覆盖历史记录。\n\n' if zh else 'Full dated entries preserve experimental conditions and limitations. Later revisions do not erase earlier records.\n\n')
        for date in dates:
            c=editions[date];daily += f"- [{date}]({date}{suffix}): {c['new']} {'新论文' if zh else 'new'}, {c['revised']} {'修订' if zh else 'revised'}, {c.get('supplemental',0)} {'前期补核' if zh else 'supplemental'}\n"
        (ROOT / 'daily' / ('README' + suffix)).write_text(daily)
        ti = ('# 主题索引\n\n' if zh else '# Topic index\n\n') + labels + f" | [{'首页' if zh else 'Home'}](../README{suffix})\n\n"
        ti += (f'共 {n} 篇独立论文。不同主题可重复出现同一论文；每个主题内按 arXiv ID 去重，并链接到最新归档及完整日期历史。\n\n' if zh else f'{n} unique papers. A paper may belong to several topics; each topic deduplicates by arXiv ID and links to the latest covered entry and dated history.\n\n')
        for slug,titles in TOPICS.items():
            selected=[p for p in papers if slug in p['topics']]
            ti += f'- [{titles[zh]}]({slug}{suffix}) · {len(selected)}\n'
            topic=f'# {titles[zh]}\n\n[English]({slug}.md) | [简体中文]({slug}.zh-CN.md) | [{"所有主题" if zh else "All topics"}](README{suffix})\n\n'
            topic+=(f'{len(selected)} 篇独立论文。以下为导航摘要；完整数值、实验限制与代码状态见每日归档。\n\n' if zh else f'{len(selected)} unique papers. These are navigation summaries; consult the daily entries for full metrics, caveats, and code status.\n\n')
            for p in selected:
                h=p['history'][-1]
                topic+=f"## {p['title']}\n\n- [arXiv {p['id']}](https://arxiv.org/abs/{p['id']}) · {h['version']} · [{'最新归档' if zh else 'Latest entry'}](../daily/{h['date']}{suffix}#arxiv-{p['id']})\n"
                topic+=f"- {'收录历史' if zh else 'Coverage history'}: "+' · '.join(f"[{x['date']} ({x['version']}, {x['status']})](../daily/{x['date']}{suffix}#arxiv-{p['id']})" for x in p['history'])+'\n\n'
                topic+=p['summary_zh' if zh else 'summary_en']+'\n\n'
            (ROOT/'topics'/(slug+suffix)).write_text(topic)
        (ROOT/'topics'/('README'+suffix)).write_text(ti)
if __name__ == '__main__': main()
