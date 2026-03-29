from pathlib import Path
for path in sorted(Path("diagrams/source").glob("*.xml")):
    print(path.name)
