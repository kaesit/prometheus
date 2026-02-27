from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static, ListView, ListItem
from textual.reactive import reactive
from textual import events
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
import random


from textual.widgets import ListView, ListItem, Label

class ToolsPanel(ListView):

    def on_mount(self) -> None:
        self.append(ListItem(Label("📊 Generate Random Data")))
        self.append(ListItem(Label("📈 Show Statistics")))
        self.append(ListItem(Label("🔥 Simulate Process")))
        self.append(ListItem(Label("🧹 Clear Results")))

class VisualizationPanel(Static):
    def show_chart(self):
        table = Table(title="Random Data Visualization")
        table.add_column("Index")
        table.add_column("Value")

        for i in range(10):
            table.add_row(str(i), str(random.randint(1, 100)))

        self.update(Panel(table, border_style="cyan"))

    def show_stats(self):
        values = [random.randint(1, 100) for _ in range(20)]
        avg = sum(values) / len(values)

        content = f"""
Min: {min(values)}
Max: {max(values)}
Avg: {avg:.2f}
"""
        self.update(Panel(Align.center(content), title="Statistics", border_style="green"))

    def show_process(self):
        progress = ""
        for i in range(1, 11):
            progress += f"Step {i}/10 completed\n"

        self.update(Panel(progress, title="Process Simulation", border_style="magenta"))


class ResultsPanel(Static):
    def log(self, message: str):
        self.update(Panel(message, title="Results Log", border_style="yellow"))


class DashboardApp(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    #main {
        layout: horizontal;
        height: 1fr;
    }

    #tools {
        width: 25%;
        border: solid green;
    }

    #visualization {
        width: 50%;
        border: solid cyan;
    }

    #results {
        width: 25%;
        border: solid yellow;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="main"):
            yield ToolsPanel(id="tools")
            yield VisualizationPanel(id="visualization")
            yield ResultsPanel(id="results")
        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        tool_name = event.item.query_one(Label).renderable

        visualization = self.query_one("#visualization", VisualizationPanel)
        results = self.query_one("#results", ResultsPanel)

        if "Generate Random Data" in tool_name:
            visualization.show_chart()
            results.log("Random data generated.")

        elif "Show Statistics" in tool_name:
            visualization.show_stats()
            results.log("Statistics calculated.")

        elif "Simulate Process" in tool_name:
            visualization.show_process()
            results.log("Process simulation completed.")

        elif "Clear Results" in tool_name:
            visualization.update("Cleared.")
            results.log("Results cleared.")

if __name__ == "__main__":
    DashboardApp().run()