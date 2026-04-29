# AI-Driven Spatial Omics & Gene Regulatory Network Agent
这是一个基于多 Agent 协同架构的生物信息学自动化分析工作流，专为解决复杂组学数据（如空间转录组学 Stereo-seq）的工程化瓶颈而设计。

## 🎯 核心能力
- **长链推理任务拆解**：自动将生物学指令（如构建单样本网络 SCAN）转化为计算 Pipeline。
- **Pipeline 代码生成**：自动化生成并执行跨语言（R/Python）的生信清洗与分析代码。
- **自适应 Debug 机制**：自动捕捉 `igraph` 等复杂底层运算中的内存溢出并进行算法调优。

## ⚙️ 架构说明
项目包含三个核心大模型 Agent：
1. `Logic_Agent`: 负责科研链路规划与统计学方法匹配。
2. `Coder_Agent`: 负责高维矩阵运算与批处理脚本生成。
3. `Debug_Agent`: 负责日志监控与代码自修复。

*(Note: Currently migrating to MiMo API for enhanced long-context handling of biological literature.)*
