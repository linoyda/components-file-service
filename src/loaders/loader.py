from abc import ABC, abstractmethod
import py7zr
import os

class ILoader(ABC):
    @abstractmethod
    def load_data(self, extract_dir):
        pass

    @abstractmethod
    def __unzip(self, extract_dir):
        pass

class TextFileLoader(ILoader):
    """Extract text from a .7z of .txt files. Return a list of components, containing """
    def __init__(self, path):
        self.archive_path = path

    def __unzip(self, extract_dir):
        try:
            with py7zr.SevenZipFile(self.archive_path, mode='r') as archive:
                archive.extractall(path=extract_dir)
        except:
            print("Exception while unzipping archive: " + self.archive_path)


    def load_data(self, extract_dir):
        """Unzip to a specific directory and return a dict of all file content per filename (component file)"""

        self.__unzip(extract_dir)
        
        content_dict = {}
        # Iterate over all files in the extracted directory
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                try:
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        
                        # Read and concatenate the content of each .txt file
                        with open(file_path, 'r') as f:
                            content_dict[file] = f.read()
                except:
                    print("failed loading content from file: " + file)
                    
        return content_dict