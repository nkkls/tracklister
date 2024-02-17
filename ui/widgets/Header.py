from textual.widget import Widget
from textual.widgets import Static, Button
from textual.containers import Horizontal
from textual.app import ComposeResult

from ui.messages import SetScreen

class Header(Widget):
    def on_button_pressed(self, event):
        self.post_message(SetScreen(event.button.id))

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("home", id="home")
            yield Button("create", id="create")
            yield Button("modify", id="modify")
            yield Button("settings", id="settings")
            yield Static("spot2grind v0.0.1 ")