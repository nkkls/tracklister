from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

class HomeScreen(Widget):
    async def on_mount(self) -> None:
        self.title = "spot2grind"

    async def on_show(self) -> None:
        self.title = "spot2grind"

    def compose(self) -> ComposeResult:
        yield Static("home screen")