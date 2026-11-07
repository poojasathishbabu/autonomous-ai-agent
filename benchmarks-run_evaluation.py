from src_evaluation_harness import eval_factuality, eval_latency
if __name__=="__main__":
    print(f"Factuality: {eval_factuality('revenue is 1240000','1240000')}")
    print("Run Garak: garak --model_name test --probes promptinject,dan --generators openai")
