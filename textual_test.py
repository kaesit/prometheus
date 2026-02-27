from textual.app import App
from textual.widgets import Button

class MyApp(App):
    def compose(self):
        yield Button("Click Me")

if __name__ == "__main__":
        MyApp().run()