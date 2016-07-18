from cx_Freeze import setup, Executable

executables = [
        Executable("Namechooser.py", icon="pi.ico")
]
buildOptions = dict(
        create_shared_zip = True)

includefiles = ["Namelist.py"]
includes = []
excludes = []
packages = []

setup(
        name = "NameChooser",
        version = "0.1",
        description = "A program to draw names from a box",
        options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
        executables = executables)
