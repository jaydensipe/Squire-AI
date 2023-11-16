from ui.main_window import MainWindow
from components.brain import Brain
import threading

squire = Brain(
    name="Squire",
    personality="""
    Your name is Squire and you are my assistant. As my assistant, your primary responsibility is to complete tasks I ask of you. However, I also value your input and insights. While I expect you to prioritize my requests, I want you to feel comfortable speaking your mind and offering suggestions or feedback when you think it could benefit our work together.

    {history}
    Human: {human_input}
    Assistant:
    """,
)


def __startup_squire() -> None:
    squire.awaken()


def __startup_ui() -> None:
    global ui

    ui = MainWindow()
    ui.mainloop()


def submit_chatbot_request():
    request = ui.entry.get()
    ui.entry.delete(0, "end")

    squire.interpret_and_reflect(request)

def receive_chatbot_message(message: str):
    ui.textbox.insert("end", message)


@staticmethod
def start_threads() -> None:
    bot_thread = threading.Thread(target=__startup_squire, args=())
    ui_thread = threading.Thread(target=__startup_ui, args=())

    bot_thread.start()
    ui_thread.start()
