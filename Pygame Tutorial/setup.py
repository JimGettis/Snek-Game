import cx_Freeze
import os

os.environ['TCL_LIBRARY'] ="C:/Users/Jim Gettis/AppData/Local/Programs/Python/Python36-32//tcl//tcl8.6"
os.environ['TK_LIBRARY'] ="C:/Users/Jim Gettis/AppData/Local/Programs/Python/Python36-32//tcl//tk8.6"
executables = [cx_Freeze.Executable("snek.py")]

cx_Freeze.setup(
    name = "Snek Game",
    options = {'build_exe': {"packages" : ["pygame","time", "random"],
                             "include_files" : ["C:/Users/Jim Gettis/Desktop/Dad/Beginner Projects/Pygame Tutorial/scripts/UltraColor.py",
                                                "C:/Users/Jim Gettis/Desktop/Dad/Beginner Projects/Pygame Tutorial/graphics/snakehead.png",
                                                "C:/Users/Jim Gettis/Desktop/Dad/Beginner Projects/Pygame Tutorial/graphics/apple.png"]}},

    description = "Snek Game",
    executables = executables
    )