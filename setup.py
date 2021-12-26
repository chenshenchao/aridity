import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", 'pyglet'],
    "excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="aridity",
    version="0.4",
    description="yet a roguelike game.",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "app.py",
            base=base,
            icon='aridity.ico',
            target_name='aridity',
        ),
        Executable(
            "edit.py",
            base=base,
            icon='aridity/design/edit.ico',
        ),
    ]
)
