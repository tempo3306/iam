#coding=utf-8
from distutils.core import sebtup
import py2exe
import glob
#
libRootPath = r'D:\ProgramStudy\python278'

data_files = ["E:\python_p\logo.ico",
              (r'mpl-data', glob.glob(libRootPath+r'\Lib\site-packages\matplotlib\mpl-data\*.*')),
              (r'mpl-data', [libRootPath+r'\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
              (r'mpl-data\images', glob.glob(libRootPath+r'\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
              (r'mpl-data\fonts', glob.glob(libRootPath+r'\Lib\site-packages\matplotlib\mpl-data\fonts\*.*'))]

setup(
    windows=[
        {
            "script":'study_main.py',
            "icon_resources":[(1, "logo.ico")]
        }],
    options = {
        'py2exe':
                   {
                       'dll_excludes':['MSVCP90.dll', 'numpy-atlas.dll'],
                        "includes": ["matplotlib.backends", "matplotlib.figure", "pylab", "numpy", "matplotlib.backends.backend_tkagg"],
                        'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo', '_cocoaagg', '_fltkagg', '_gtk', '_gtkcairo', ]
                   }
    },
    data_files=data_files
)
