import os
import subprocess
from pathlib import Path
from typing import List

class DjangoAppBuilder:
    def __init__(self, MainFilePath: str, DirsToPackage: List[str], SingleFile: bool):
        self.MainFilePath = MainFilePath
        self.DirsToPackage = DirsToPackage
        self.SingleFile = SingleFile

    def build(self):
        """
        Build the Django application using PyInstaller.
        """
        try:
            AddData = self._GatherAddData()
            Command = ['pyinstaller', '--onefile' if self.SingleFile else '--onedir', '--add-data', AddData, self.MainFilePath]
            subprocess.run(Command, check=True)
            print(f"Successfully Built {self.MainFilePath} As A Django Application.")
        except subprocess.CalledProcessError as e:
            print(f"Error During Build: {e}")

    def _GatherAddData(self):
        """
        Gather the directories and their files to be included in the PyInstaller build.
        """
        AddDataList = []
        for Directory in self.DirsToPackage:
            for Root, _, Files in os.walk(Directory):
                for File in Files:
                    FilePath = Path(Root) / File
                    RelativePath = FilePath.relative_to(Directory)
                    AddDataList.append(f"{FilePath}{os.pathsep}{RelativePath.parent}")

        return ';'.join(AddDataList)