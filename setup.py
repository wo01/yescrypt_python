from distutils.core import setup, Extension

yescrypt_module = Extension('yescrypt',
                            sources = ['yescrypt.c'],
                            extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'yescrypt',
       version = '1.0',
       description = 'Bindings for yescrypt proof of work',
       ext_modules = [yescrypt_module])
