# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="hexagonos minecraft", 
 version="1.0", 
 description="este programa genera una secuencia del numero de bloques que se deben poner por fila para generar un lado", 
 author="falacod", 
 url="https://github.com/falacod/minecraft_util", 
 license="GNU General Public License v3.0", 
 scripts=["hexagonos.py"], 
 console=[{"script":"hexagonos.py"}], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)