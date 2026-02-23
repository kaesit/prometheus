from rich.console import Console
from rich.progress import track
from rich.table import Table
import time
def main():
    console  = Console()
    
    console.print("Hello from Prometheus!")
    console.print("Hello from Prometheus", style="bold")
    console.print("Hello from Prometheus", style="bold underline")
    console.print("Hello from Prometheus", style="bold underline green")
    
    console.print("Hello from Prometheus", style="bold underline blue on red")
    
    console.print("[bold]Hello [cyan]from[/] Prometheus[/]")
    for i in track(range(10), description="Processing..."):
        print(f"working {i}")
        time.sleep(0.5)
    table = Table(title="Star Wars Movies")
    table.add_column("Released", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Released", style="green")
    
    table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,100,678")
    table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$352,100,678")
    table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,519,889")
    console.print(table)
    
    table2 = Table(title="Dune Movies")
    table2.add_column("Released", style="cyan")
    table2.add_column("Title", style="magenta")
    table2.add_column("Released", style="green")
    
    table2.add_row("Dec 20, 2022", "Dune Part 1", "$952,100,678")
    table2.add_row("May 25, 2024", "Dune Part 2", "$1,352,100,678")
    console.print(table2)
    
    
    


if __name__ == "__main__":
    main()
