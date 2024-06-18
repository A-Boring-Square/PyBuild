import os
import shutil
import subprocess
from pathlib import Path
from typing import List

class GuiProgramBuilder:
    def __init__(self, MainFilePath: str, DirsToPackage: List[str], SingleFile: bool, ExtraDirsToInclude: List[str]):
        self.MainFilePath = MainFilePath
        self.DirsToPackage = DirsToPackage
        self.SingleFile = SingleFile
        self.ExtraDirsToInclude = ExtraDirsToInclude
        self.BuildDir = Path("Build")

    def Build(self):
        """
        Build the GUI program using PyInstaller.
        """
        self._Clean()
        self._PrepareBuildDir()
        try:
            AddData = self._GatherAddData()
            Command = ['pyinstaller', '--onefile' if self.SingleFile else '--onedir', '--distpath', str(self.BuildDir)]
            
            if AddData:
                Command.extend(['--add-data', AddData])
                
            Command.append(self.MainFilePath)
            
            subprocess.run(Command, check=True)
            print(f"Successfully built {self.MainFilePath} as a {'single file' if self.SingleFile else 'directory'} GUI program.")
        except subprocess.CalledProcessError as e:
            print(f"Error during build: {e}")

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

    def _PrepareBuildDir(self):
        """
        Prepare the build directory by copying extra directories.
        """
        self.BuildDir.mkdir(exist_ok=True)
        for Directory in self.ExtraDirsToInclude:
            Dest = self.BuildDir / Path(Directory).name
            shutil.copytree(Directory, Dest)

    def _Clean(self):
        """
        Clean the build directory.
        """
        if self.BuildDir.exists() and self.BuildDir.is_dir():
            shutil.rmtree(self.BuildDir)

class TerminalAppBuilder:
    def __init__(self, MainFilePath: str, DirsToPackage: List[str], SingleFile: bool, ExtraDirsToInclude: List[str]):
        self.MainFilePath = MainFilePath
        self.DirsToPackage = DirsToPackage
        self.SingleFile = SingleFile
        self.ExtraDirsToInclude = ExtraDirsToInclude
        self.BuildDir = Path("Build")

    def Build(self):
        """
        Build the terminal application using PyInstaller.
        """
        self._Clean()
        self._PrepareBuildDir()
        try:
            AddData = self._GatherAddData()
            Command = ['pyinstaller', '--onefile' if self.SingleFile else '--onedir', '--distpath', str(self.BuildDir)]
            
            if AddData:
                Command.extend(['--add-data', AddData])
                
            Command.append(self.MainFilePath)
            
            subprocess.run(Command, check=True)
            print(f"Successfully built {self.MainFilePath} as a {'single file' if self.SingleFile else 'directory'} terminal application.")
        except subprocess.CalledProcessError as e:
            print(f"Error during build: {e}")

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

    def _PrepareBuildDir(self):
        """
        Prepare the build directory by copying extra directories.
        """
        self.BuildDir.mkdir(exist_ok=True)
        for Directory in self.ExtraDirsToInclude:
            Dest = self.BuildDir / Path(Directory).name
            shutil.copytree(Directory, Dest)

    def _Clean(self):
        """
        Clean the build directory.
        """
        if self.BuildDir.exists() and self.BuildDir.is_dir():
            shutil.rmtree(self.BuildDir)
