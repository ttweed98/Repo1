import difflib

file01 = "httpd.conf.bak"  # Corrected file name to match your original intention
file02 = "httpd.conf"

# Read file1 contents
with open(file01, 'r') as f1:
    file1_contents = f1.readlines()  # Read all lines into a list

# Read file2 contents
with open(file02, 'r') as f2:
    file2_contents = f2.readlines()  # Read all lines into a list

# Create an HTML diff
differences = difflib.HtmlDiff(wrapcolumn=79).make_file(file1_contents, file2_contents, fromdesc=file01, todesc=file02)

# Write the diff to an HTML file
with open(f'{file01}_{file02}_compared.html', 'w') as html_file:
    html_file.write(differences)
