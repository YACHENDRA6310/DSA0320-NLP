import re
dialog_acts = {
    "greeting": r"\b(hi|hello|hey)\b",
    "farewell": r"\b(goodbye|bye|see you)\b",
    "question": r"\b(what|who|where|when|why|how)\b",
    "statement": r"\b(is|are|was|were|am)\b",
    "thanks": r"\b(thank you|thanks)\b"
}
def classify_dialog_act(statement):
    for act, pattern in dialog_acts.items():
        if re.search(pattern, statement, re.IGNORECASE):
            return act
    return "unknown"
def recognize_dialog_acts(conversation):
    acts = []
    for line in conversation:
        act = classify_dialog_act(line)
        acts.append((line, act))
    return acts
conversation = [
    "Hello! How are you?",
    "I am fine, thank you.",
    "What about you?",
    "Goodbye!",
    "See you later!",
    "Thanks for the chat!"
]
recognized_acts = recognize_dialog_acts(conversation)
for line, act in recognized_acts:
    print(f"Dialog: '{line}' - Act: '{act}'")
