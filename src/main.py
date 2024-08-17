import sys
from services.service import FilterService
from parsers.parser import TextToComponentParser
from loaders.loader import TextFileLoader
import pathlib

def main(archive_filename):
    """Driver function"""
    try:
        try:
            archive_dir = pathlib.Path(__file__).parent.resolve()
            archive_path = archive_dir.joinpath(archive_filename)
            extract_dir = archive_dir.joinpath("extracted")
        except FileNotFoundError:
            sys.exit("Archive file not found")

        # Call the loader to create a mapping between filename and its content.
        loader = TextFileLoader(str(archive_path), str(extract_dir))
        content_dict = loader.load_data()

        if not content_dict:
            sys.exit("Failed to load content")
        
        # Pass the content dictionary to the parser, to create a list of Components.
        parser = TextToComponentParser(content_dict)
        service = FilterService(parser.parse_data())

        return service.serve_client(filter=(5,-20))
    except:
        sys.exit("FATAL error occured")



if __name__ == "__main__":
    main(archive_filename="Task example files.7z")
