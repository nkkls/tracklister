from textual.message import Message

class SetScreen(Message):
    def __init__(self, event) -> None:
        super().__init__()
        self.screen = event
