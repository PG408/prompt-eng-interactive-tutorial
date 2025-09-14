# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 提供在此代码库中工作的指导。

## 项目概述

此代码库包含 Anthropic 的提示工程交互式教程 - 一个全面的教育课程，旨在教授 Claude AI 的最佳提示工程技术。教程包含 9 个章节加一个附录，以交互式 Jupyter notebook 形式呈现，包含实践练习。

## 代码库结构

代码库有两个主要实现：

### 1. Anthropic 1P（直接 API）
位于 `Anthropic 1P/` - 使用 Anthropic 直接 API
- 教程 notebooks：从 `00_Tutorial_How-To.ipynb` 到 `10.3_Appendix_Search & Retrieval.ipynb`
- 辅助工具：`hints.py` - 包含练习的提示文本和解决方案模板
- 所有 notebooks 直接使用 Anthropic Python 客户端

### 2. AmazonBedrock（AWS 集成）
位于 `AmazonBedrock/` - 通过 AWS Bedrock 使用 Claude
- 相同编号的 notebooks，但适配了 Bedrock API 调用
- 子目录：
  - `anthropic/` - 用于 Bedrock 的 Anthropic SDK 示例
  - `boto3/` - 用于 Bedrock 的纯 boto3 示例
  - `utils/` - 共享工具函数
  - `cloudformation/` - AWS 基础设施模板
- 依赖项：`requirements.txt` 包含 boto3、awscli 和 anthropic 包

## 开发环境设置

### Anthropic 1P 版本：
```bash
cd "Anthropic 1P"
pip install anthropic
# 在 IPython store 中设置 API_KEY 和 MODEL_NAME 变量
```

### Bedrock 版本：
```bash
cd AmazonBedrock  
pip install -r requirements.txt
# 配置 AWS 凭证和区域
```

## 教程结构

每个章节遵循以下模式：
1. **课程** - 核心概念和示例
2. **练习** - 带自动评分的实践练习
3. **示例游乐场** - 自由实验区域

### 章节进度：
- **初级（1-3）**：基本结构、清晰度、角色分配
- **中级（4-7）**：数据分离、输出格式化、逐步思考、示例使用
- **高级（8-9）**：防止幻觉、复杂行业用例
- **附录（10.x）**：高级技术如链式提示、工具使用、搜索检索

## 代码模式

### Notebook 单元格结构
- `get_completion()` 辅助函数标准化 API 调用
- 练习单元格包含使用正则表达式模式的自动评分函数
- 提示系统引用 `hints.py` 进行引导学习
- 课程内容和练习区域清晰分离

### API 集成模式
- **Anthropic 1P**：直接使用 `anthropic.Anthropic()` 客户端
- **Bedrock**：使用 `boto3` 客户端或带 Bedrock 后端的 Anthropic SDK
- 一致的参数：`model`、`max_tokens=2000`、`temperature=0.0`
- 系统提示与用户/助手消息数组分开处理

### 练习评分
- 使用 `grade_exercise()` 函数中的正则表达式模式进行自动验证
- 复杂练习的解决方案存储在 `hints.py` 中
- 模式匹配查找响应中的特定关键词或结构

## 文件编辑指南

### 修改 Notebooks 时：
- 保持单元格结构和 ID 以维持练习流程
- 保持一致的 `get_completion()` 函数签名
- 保持评分函数完整 - 它们验证练习完成情况
- 如果更改内容，更新两个 API 版本

### 使用提示时：
- 按照现有命名约定向 `hints.py` 添加新提示
- 包含提示文本和完整解决方案示例
- 对多行提示使用三引号字符串

## 常用操作

### 运行教程：
1. 从 `00_Tutorial_How-To.ipynb` 开始获取设置说明
2. 按编号顺序逐章进行
3. 在进入下一章之前完成练习
4. 需要时通过 `from hints import exercise_X_Y_hint` 使用提示

### 测试练习：
- 每个练习都有通过 `grade_exercise()` 函数内置的评分
- 按说明修改 `PROMPT` 或 `SYSTEM_PROMPT` 变量
- 运行单元格查看 Claude 的响应和验证结果

### API 配置：
- 在 IPython 变量存储中存储 API 密钥和模型名称
- 在 Bedrock 版本中使用环境变量配置 AWS 凭证
- 在开始教程前用简单提示测试 API 连接

## 学习目标

此教程教授：
- 正确的提示结构和格式化
- 与 Claude 清晰直接沟通的技术
- 基于角色的提示策略
- 数据/指令分离方法
- 输出格式化和响应指导
- 逐步推理方法
- 使用示例的少样本学习
- 防止幻觉策略
- 真实世界应用的复杂提示构建
- 高级技术如提示链和工具集成