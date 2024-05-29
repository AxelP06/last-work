import yaml
import typer

app = typer.Typer()

orders = {}

def print_orders():
    orders_str = "Aktuella beställningar:\n"
    if orders:
        for name in orders:
            orders_str += f"{name}s beställningar:\n"
            for cookie_type, quantity in orders[name].items():
                orders_str += f"  {cookie_type}: {quantity} st\n"
    else:
        orders_str += "Inga beställningar än.\n"
    typer.echo(orders_str)
    return orders_str


def update_orders(name: str, cookie_type: str, quantity: int):
    if name not in orders:
        orders[name] = {}
    if cookie_type in orders[name]:
        orders[name][cookie_type] += quantity
    else:
        orders[name][cookie_type] = quantity


def save_orders_to_yaml(filename: str):
    with open(filename, 'w') as file:
        yaml.dump(orders, file, allow_unicode=True)
    typer.echo(f"Orders saved to {filename}")


@app.command()
def add_order(name: str, cookie_type: str, quantity: int):
    """
    Add a new order for a specific cookie type and quantity.
    """
    if cookie_type not in ["Chokladbollar", "Kolabollar", "Dammsugare", "Godis"]:
        typer.echo("Felaktig kaksort, försök igen.")
        raise typer.Exit()
    update_orders(name, cookie_type, quantity)
    typer.echo(f"{name} har lagt till en beställning för {quantity} {cookie_type} kakburkar.")


@app.command()
def show_orders():
    """
    Show all current orders.
    """
    print_orders()


@app.command()
def save_orders(filename: str = "orders.yaml"):
    """
    Save all orders to a YAML file.
    """
    save_orders_to_yaml(filename)


if __name__ == "__main__":
    app()
