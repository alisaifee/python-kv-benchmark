tmpl=open("README.tmpl").read()
tmpl=tmpl.replace("{TABLE}", open("results/table.txt").read())
open("README.md", "w").write(tmpl)
