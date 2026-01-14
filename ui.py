from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Digits, Static, Placeholder
from textual.containers import HorizontalGroup, VerticalScroll
from textual.screen import Screen

import yendata

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class ColumnsContainer(Placeholder):
    

class ConvertScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id='Footer')

class conversionApp(App):
    
    BINDINGS = [
        #("d", "toggle_dark", "Toggle Dark Mode" )
        #("t", "toggle_direction", "Toggle USD-JPY / JPY_USD")
        #("c", "clear_screen", "Clear the Screen")
    ]

    def on_mount(self) -> ComposeResult:
        self.push_screen(ConvertScreen())



if __name__ == "__main__":
    app = conversionApp()
#    initialRequest() # Have the app run the API upon boot
    app.run()