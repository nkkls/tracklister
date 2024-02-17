from textual.widget import Widget
from textual.widgets import Static
from textual.app import ComposeResult

class Tabs(Widget):
    def compose(self) -> ComposeResult:
        yield Static("test")