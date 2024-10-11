from textual.app import App
from textual.widgets import Input, Button, Header, Footer, Static
from textual.containers import Container


class HelloApp(App):

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        yield Header()
        yield Footer()
        yield Container(
            Input(placeholder="Enter your name", id="name_input"),
            Button(label="Submit", id="submit_button"),
            Static(id="greeting_output"),
        )

    def on_button_pressed(self, event: Button.Pressed):
        name_input = self.query_one("#name_input", Input)
        greeting_output = self.query_one("#greeting_output", Static)
        name = name_input.value.strip()
        if name:
            greeting_output.update(f"Hello {name}!")
        else:
            greeting_output.update("Please enter a valid name.")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_quit(self):
        self.exit()


if __name__ == "__main__":
    HelloApp().run()
