"""Write the 19 November edition from its bundled image."""

from pathlib import Path


if __name__ == "__main__":
    edition = Path(__file__).resolve().with_name("world-brief.jpg").read_bytes()
    target = Path("/output/entry.png")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(edition)
