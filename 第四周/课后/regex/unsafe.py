import subprocess

subprocess.Popen("dir", shell=True)
subprocess.Popen("dir", cwd=".", shell = True)
subprocess.Popen(
    "dir",
    shell=True,
)