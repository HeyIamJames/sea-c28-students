"""This programs removes whitespace from a file."""

print "filename" sys.argv 

map(clean_lines = [])
with open("transfer-out/" + file, "r") as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]

with open("transfer-out/"+file, "w") as f:
    f.writelines('\n'.join(clean_lines))