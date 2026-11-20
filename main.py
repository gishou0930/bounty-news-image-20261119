"""Write the fixed 19 November 2026 news illustration without network access."""

from pathlib import Path
from shutil import copyfile


def main():
    image = Path(__file__).resolve().with_name("news.png")
    output = Path("/output/entry.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    copyfile(image, output)


if __name__ == "__main__":
    main()
