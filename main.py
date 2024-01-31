import argparse
import time

def parse_message(message):
    # Implement your parsing logic here
    # For example, return True if the message contains a certain keyword
    return "keyword" in message

def monitor_chat_log(file_path):
    with open(file_path, "r") as file:
        # Go to the end of the file
        file.seek(0,2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly to avoid busy waiting
                continue
            if parse_message(line):
                print(line.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor a chat log and print certain messages.")
    parser.add_argument("file_path", type=str, help="Path to the chat log file")
    args = parser.parse_args()

    monitor_chat_log(args.file_path)