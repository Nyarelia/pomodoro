from distutils.core import setup
import py2exe
import glob

data_files = [('images', glob.glob('images/tomato.png'))]

includes = ["tkinter"]

packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']

setup(
    data_files= data_files,
    options={"py2exe": {"compressed": 2,
                        "optimize": 2,
                        "includes": includes,
                        "packages": packages,
                        "dll_excludes": dll_excludes,
                        "bundle_files": 1,
                        "dist_dir": "dist",
                        "xref": False,
                        "skip_archive": False,
                        "ascii": False,
                        "custom_boot_script": '',
                        }
             },
    windows=['main.py']
)
