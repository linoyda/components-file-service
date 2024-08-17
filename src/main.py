from services.service import SearchService
from parsers.parser import TextToComponentParser
from loaders.loader import TextFileLoader
from services.component import Component
import pathlib

def main(archive_filename):
    """Driver function"""

    try:
        archive_path = pathlib.Path(__file__).parent.resolve().joinpath(archive_filename)
    except FileNotFoundError:
        print("archive path was not found")

    loader = TextFileLoader(archive_path)
    parser = TextToComponentParser()
    service = SearchService()

    # Call the loader to create a mapping between filename and its content.



if __name__ == "__main__":
    main(archive_filename="Task example files.7z")
