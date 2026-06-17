from services.prompt import build_prompt
from services.groq_client import ask_groq
from models.message_model import save_message, get_messages


def handle_chat(user_id, first_name, mode, lang, messages):
    system_prompt = build_prompt(mode, first_name, lang)
    response = ask_groq(system_prompt, messages)

    # on sauvegarde le dernier echange (question + reponse)
    if messages:
        save_message(user_id, "user", messages[-1]["content"])
    save_message(user_id, "assistant", response)
    return response


def get_history(user_id):
    return get_messages(user_id)
