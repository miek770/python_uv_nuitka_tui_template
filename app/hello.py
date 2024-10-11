import rich_click as click


@click.command()
@click.argument("name")
def main(name: str):
    print(f"Hello {name}!")


if __name__ == "__main__":
    main()
