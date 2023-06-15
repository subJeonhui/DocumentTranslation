import os
from FileManagement.FileType import *
from FileManagement.FileLoader import *
from pathlib import Path
import datetime


class FileManager:

    def __init__(self, basePath="./files"):
        self.root = None
        self.fileLoader = None
        self.select = None
        self.basePath = basePath

        dir_set = {}

        for root, dirs, files in os.walk(basePath):
            directory = dir_set[root] if root in dir_set else Directory(root)
            if root == basePath:
                self.root = directory

            for dirName in dirs:
                dirPath = f"{root}/{dirName}"
                dir_set[dirPath] = Directory(dirPath)
                directory.add(dir_set[dirPath])

            for fileName in files:
                directory.add(File(fileName, root))

    def selectFile(self, file: File):
        self.select = file
        self.__setLoader()

    def selectFilePath(self, filePath: str):
        path = '/'.join(filePath.split('/')[:-1])
        name = filePath.split('/')[-1]
        self.select = File(name, path)
        self.__setLoader()

    """
    ================================================================
    
    Strategy Pattern
    Runtime 중 알고리즘을 선택
    사용자가 선택한 파일에 따라 다른 Loader을 선택
    
    ================================================================
    """
    def __setLoader(self):
        if self.select.ext == FileExt.HTML:
            self.fileLoader = HTMLLoader(self.select.fullPath())
        elif self.select.ext == FileExt.MARKDOWN:
            self.fileLoader = MarkDownLoader(self.select.fullPath())

    def load(self):
        return self.fileLoader.load()

    def save(self, path, text):
        if self.select is None:
            return None
        if path is None:
            new_path = self.select.fullPath().split("/")
            new_path[-1] = "translated-" + new_path[-1]
            path = "/".join(new_path)
        print(path)
        file = Path(path)
        file.parent.mkdir(exist_ok=True, parents=True)
        file.write_text(text)
        return path

    def logging(self, path, count):
        if self.select is None:
            return None
        log = f"|{datetime.datetime.now().date()}|{self.select.fullPath()}|{count}|\n"
        with open(path, 'a') as f:
            f.write(log)

    def read_log(self, path):
        with open(path, 'r') as f:
            logs = f.readlines()
            return logs

    def read_log_with_date(self, path, date=None):
        logs = self.read_log(path)
        if date is None:
            date = str(datetime.datetime.now().date())
        date_log = []
        for log in logs:
            log = list(map(lambda x: x.strip(),filter(lambda x: len(x.strip()) > 0, log.split('|'))))
            if log[0] == date:
                date_log.append(log)
        return date_log

