import subprocess
import platform

class PyAppProgramBuilder:
    def __init__(self, PyAppCommand: str):
        self.PyAppCommand = PyAppCommand

    def Build(self):
        if platform.system().lower() == "windows":
            Command = ['PyApp', self.PyAppCommand]
        else:
            Command = ['./PyApp', self.PyAppCommand]

        try:
            subprocess.run(Command, check=True)
        except subprocess.CalledProcessError:
            print('Error: Either Your Command Was Incorrect Or PyApp Is Not Installed.')
        except FileNotFoundError:
            print('Error: PyApp Executable Not Found. Please Ensure It Is Installed And Available In The PATH.')

