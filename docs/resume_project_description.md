# Resume Project Description

## 中文简历版

### 岗位数据分析与可视化 Dashboard

基于 Python / pandas / Streamlit 开发岗位数据分析与可视化项目，支持读取岗位 CSV 数据，完成字段校验、岗位筛选、城市统计、技能频次统计、薪资分析和高薪岗位排序，并自动生成 CSV 结果、文本总结和 PNG 图表。项目进一步使用 Streamlit 构建交互式网页 Dashboard，支持 CSV 上传、关键指标展示、统计表格、柱状图展示和侧边栏筛选，实现从命令行脚本到可交互数据分析工具的完整项目流程。

**技术栈：** Python、pandas、matplotlib、Streamlit、argparse、pathlib、Git、GitHub

**项目亮点：**

* 使用 pandas 完成岗位数据清洗、筛选、分组统计和技能字段拆分分析
* 使用 argparse 支持命令行输入输出参数，提高脚本复用性
* 使用 pathlib 管理项目路径，避免脚本依赖当前运行目录
* 使用 matplotlib 自动生成技能频次、城市平均薪资和高薪岗位图表
* 使用 Streamlit 构建交互式网页 Dashboard，支持 CSV 上传和筛选
* 将分析逻辑封装在 `analyze_jobs.py` 中，`app.py` 仅负责网页展示，避免重复代码
* 使用 Git 分支完成图表功能、README 展示、函数化重构和 Streamlit 页面开发

## 简历精简版

开发岗位数据分析与可视化 Dashboard，使用 pandas 完成岗位数据清洗、筛选、技能频次统计、城市薪资分析和高薪岗位排序，使用 matplotlib 自动生成图表，并基于 Streamlit 构建支持 CSV 上传、指标展示、图表展示和侧边栏筛选的交互式网页工具。项目采用 Git 分支管理开发流程，并将分析逻辑与网页展示逻辑拆分，提高代码复用性和项目可维护性。

## 面试讲述版

这个项目最开始是一个 pandas 岗位数据分析脚本，后来我逐步把它整理成一个完整的小型数据分析项目。前期主要实现 CSV 读取、字段校验、岗位筛选、技能统计、城市薪资分析和图表输出；中期加入 argparse、pathlib 和 Git 分支管理，让脚本更接近真实项目结构；后期使用 Streamlit 做成网页 Dashboard，支持上传 CSV、筛选城市和技能关键词，并动态展示指标、表格和图表。

这个项目对我来说主要练习了三件事：第一是 pandas 数据处理能力，第二是 Git / GitHub 项目化管理能力，第三是把命令行脚本升级成交互式网页工具的能力。后续我也计划把这套结构迁移到建筑能耗模拟结果分析中，用来处理 EnergyPlus / Honeybee 输出数据。
