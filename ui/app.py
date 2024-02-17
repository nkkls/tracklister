from textual import on

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, ContentSwitcher

from ui.screens.home import HomeScreen
from ui.screens.create import CreateScreen
from ui.screens.modify import ModifyScreen
from ui.screens.settings import SettingsScreen

from ui.widgets.Header import Header
from ui.messages import SetScreen

class MainScreen(Screen):
    async def on_mount(self) -> None:
        self.title = "spot2grind"

    async def on_show(self) -> None:
        self.title = "spot2grind"

    def compose(self) -> ComposeResult:
        yield Header()
        with ContentSwitcher(initial="home"):
            yield HomeScreen(id="home")
            yield CreateScreen(id="create")
            yield ModifyScreen(id="modify")
            yield SettingsScreen(id="settings")

    @on(SetScreen)
    def screenChanged(self, event) -> str:
        self.query_one(ContentSwitcher).current = event.screen

class spot2grind(App):
    CSS_PATH = "css/result.tcss"
    SCREENS = {
        "main": MainScreen()
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, watch_css=True)

    async def on_mount(self) -> None:
        self.push_screen("main")
