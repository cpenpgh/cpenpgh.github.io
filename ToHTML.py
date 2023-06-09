import json

# Read the JSON data from a file
with open("data.json", "r") as f:
    data = json.load(f)

# Create an HTML table
table = """
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
<th>Occupation</th>
</tr>
</thead>
<tbody>
"""

# Iterate through the data and create a row for each person
for person in data:
    table += """
    <tr>
    <td>{name}</td>
    <td>{age}</td>
    <td>{occupation}</td>
    </tr>
    """.format(**person)

table += """
</tbody>
</table>
"""

# Write the HTML table to a file
with open("output.html", "w") as f:
    f.write(table)