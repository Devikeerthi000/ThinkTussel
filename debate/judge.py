# debate/judge.py

from llm_clients.gpt_client import call_gpt

def evaluate_debate(transcript, topic):
    eval_prompt = [
        {"role": "system", "content": "You are a fair debate judge. Evaluate both arguments carefully."},
        {"role": "user", "content": f"Debate topic: {topic}\n\nHere is the full transcript:\n\n" +
         "\n\n".join([f"{msg['role']}: {msg['content']}" for msg in transcript]) +
         "\n\nPlease declare a clear winner (GPT-4.1 or LLaMA-4) and give reasons based on the strength, clarity, and evidence of their arguments."}
    ]

    judgment = call_gpt(eval_prompt)
    return judgment
