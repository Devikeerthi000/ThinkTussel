def build_prompt(topic, stance):
    return f"Present a strong argument {'in favor of' if stance == 'pro' else 'against'} the following topic:\n\n{topic}"
