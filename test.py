import marko

name = "test"

with open(f"{name}.md", "r") as f:
    md = f.read()

doc = marko.parse(md)
renderer = marko.HTMLRenderer()
html = renderer.render(doc)

with open(f"{name}.html", "w") as f:
    f.write(html)


