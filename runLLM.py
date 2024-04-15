from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")



def get_strategy(message_txt):
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message_txt,
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        comment, code = messages.data[0].content[0].text.value.split('```')[:2]
        if "python" in code:
            code = code.split("python")[1]
        return comment, code
    else:
        print(run.status)
        return None, None


def write_strategy(code, comment):
    with open("./assistant_files/GeneratedStrategy.py", "w") as f:
        f.write(code)

    with open("./assistant_files/GeneratedStrategy.txt", "w") as f:
        f.write(comment)



