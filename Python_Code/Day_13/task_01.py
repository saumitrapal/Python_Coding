# Add other packages
import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokeman Name", ['Pickachu', 'squirtle', 'charmander'], "l")
table.add_column("Type", ['Electric', 'Water', 'Fire'], "l")

print(table)