"""
Bio-Omics Multi-Agent Automated Pipeline
Author: Independent Researcher
Target: miRNA Regulatory Network Construction (e.g., Lung Adenocarcinoma, COPD)
"""

import argparse
import logging
import time
from core.agents import LogicAgent, CoderAgent, DebugAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_agents():
    logging.info("Initializing Agent System...")
    # 模拟未来接入 MiMo API 的高维上下文能力
    logic_agent = LogicAgent(llm_backend="MiMo-Pro", context_window="1M")
    coder_agent = CoderAgent(language_support=["R", "Python"])
    debug_agent = DebugAgent(auto_fix=True)
    return logic_agent, coder_agent, debug_agent

def run_pipeline(dataset_id, task_type):
    logic, coder, debug = initialize_agents()
    
    logging.info(f"Task Received: {task_type} for dataset {dataset_id}")
    
    # Phase 1: Task Decomposition
    sub_tasks = logic.decompose_task(task_type)
    
    # Phase 2: Execution with Auto-Debug
    for step in sub_tasks:
        code_script = coder.generate_script(step)
        success = False
        retry_count = 0
        
        while not success and retry_count < 3:
            try:
                # 模拟执行诸如 limma 差异分析或 SCAN 单样本网络构建
                coder.execute_in_sandbox(code_script)
                success = True
            except Exception as e:
                logging.warning(f"Execution failed: {str(e)}. Triggering DebugAgent...")
                code_script = debug.fix_code(code_script, error_log=str(e))
                retry_count += 1
                time.sleep(2)

    logging.info(f"Pipeline completed successfully for {dataset_id}. Outputs saved to /results.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Bio-Omics Agent Pipeline.")
    parser.add_argument("--dataset", type=str, default="GSE119269", help="Target GEO dataset ID")
    parser.add_argument("--task", type=str, default="SCAN_miRNA_Network_Construction", help="Type of analysis")
    
    args = parser.parse_args()
    run_pipeline(args.dataset, args.task)
