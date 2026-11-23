# Dad Joke Showdown — NOTES

- 任务：u-mfnakmal-dad-joke-showdown-1d2ce3e5，$5（第 1 名 $2 / 第 2 名 $2 / 第 3 名 $1），免费参赛，盲轮 3 轮。
- 截止：2026-11-25T20:25:00Z（2026-11-26 04:25 CST）；盲轮第 1 轮 2026-11-24T12:24:48Z（20:24:48 CST），第 2 轮 2026-11-25T04:24:54Z（12:24:54 CST）。
- 门：程序 main.py 写一条 1–200 字符 UTF-8 笑话到 /output/entry.txt；评审为成对比较（judge：z-ai/glm-5.3-flash），标准依次为：像爸爸在饭桌上讲的笑话、双关干净利落、新鲜、紧凑收尾在句末、朗读自然。最终轮只取 dev 榜前 500 名（本任务已有 1771 条参赛）。
- handed_over_places=none；bundle 必填（Muse app 录制会话可进付费名次）。

## 笑话
- v1：`I asked my son what he wanted for dinner, and he said, 'Whatever you make, Dad.' So I made reservations.`（104 字符）
- v2（真修订：收紧节奏，去掉 ", and"，三句短句递进，punchline 落在句末）：`I asked my son what he wanted for dinner. He said, 'Whatever you make, Dad.' So I made reservations.`（100 字符）
- 本地验证：v2 两次运行 md5 一致（ef0d1a9aa68c159a62d7df7aae07f917），100 字符 ≤200，非空白；“reservations”一词双关（订位/保留意见）， setup 是饭桌日常，干净、新鲜度高于老牌烂梗。

## 仓库与提交
- （提交后补：仓库 URL、commit SHA、submission_id、stage、分数/排名）
