def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello there!", "How are you?", "What's up?"]
sent_messages = []

show_messages(messages)
send_messages(messages[:], sent_messages)

print("\nOriginal messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)
