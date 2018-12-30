from cx_Freeze import setup, Executable
import requests.certs

build_exe_options = {"include_files":[(requests.certs.where(),'cacert.pem')]}
setup(name='FFExplorerURL',
      options = {"build_exe": {"packages":["idna","requests","bs4"]}},
      version='0.1',
      description='FFExplorer',
      executables = [Executable("Script.py")])