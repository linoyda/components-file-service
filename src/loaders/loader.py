from abc import ABC, abstractmethod
import sys
import py7zr
import os

class ILoader(ABC):
    @abstractmethod
    def load_data(self):
        pass


class TextFileLoader(ILoader):
    """Extract text from a .7z of .txt files. Return a list of components, containing """
    def __init__(self, path, extract_dir):
        self.archive_path = path
        self.extract_dir = extract_dir

    def __unzip(self):
        try:
            with py7zr.SevenZipFile(self.archive_path, mode='r') as archive:
                archive.extractall(path=self.extract_dir)
        except:
            print("Exception while unzipping archive: " + self.archive_path)


    def load_data(self):
        """Unzip to a specific directory and return a dict of all file content per filename (component file)"""
        
        if not os.path.exists(self.archive_path):
            sys.exit("Archive file does not exist")
        
        # unzip only if necessary
        if not os.path.exists(self.extract_dir):
            self.__unzip()
        
        content_dict = {}
        # Iterate over all files in the extracted directory
        for root, dirs, files in os.walk(self.extract_dir):
            for file in files:
                try:
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        
                        # Read and concatenate the content of each .txt file
                        with open(file_path, 'r') as f:
                            content_dict[os.path.splitext(file)[0]] = f.read()
                except:
                    print("failed loading content from file: " + file)

        return content_dict