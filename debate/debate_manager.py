# debate/debate_manager.py

from llm_clients.gpt_client import call_gpt
from llm_clients.llama_client import call_llama
from debate.judge import evaluate_debate

def run_debate(topic, num_rounds):
    transcript = []

    pro_msgs = [{"role": "system", "content": "You're GPT-4.1. Argue in favor of the topic. Keep replies short and chat-style. Respond only when prompted."}]
    con_msgs = [{"role": "system", "content": "You're LLaMA-4. Argue against the topic. Keep replies short and chat-style. Respond only when prompted."}]

    # GPT starts
    pro_msgs.append({"role": "user", "content": f"Debate topic: {topic}\nStart with your opinion. Max 2 sentences."})
    pro_response = call_gpt(pro_msgs)
    transcript.append({"role": "GPT-4.1 (PRO)", "content": pro_response})
    pro_msgs.append({"role": "assistant", "content": pro_response})

    for round_num in range(num_rounds):
        # LLaMA replies
        con_msgs.append({"role": "user", "content": f"GPT-4.1 said:\n\"{pro_response}\"\nGive a short rebuttal (1-2 lines)."})
        con_response = call_llama(con_msgs)
        transcript.append({"role": "LLaMA-4 (CON)", "content": con_response})
        con_msgs.append({"role": "assistant", "content": con_response})

        # GPT replies
        pro_msgs.append({"role": "user", "content": f"LLaMA-4 said:\n\"{con_response}\"\nReply back shortly (1-2 lines)."})
        pro_response = call_gpt(pro_msgs)
        transcript.append({"role": "GPT-4.1 (PRO)", "content": pro_response})
        pro_msgs.append({"role": "assistant", "content": pro_response})

    # Final judgment
    judgment = evaluate_debate(transcript, topic)
    return transcript, judgment
