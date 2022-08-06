import whois
import typer

app = typer.Typer()

@app.command()

def domain(name: str):
    results = whois.whois(name)
    print(f"{name} is registered by {results.name} - {results.org}")


if __name__ == "__main__":
    app() 