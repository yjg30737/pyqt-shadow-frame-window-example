from setuptools import setup, find_packages

setup(
    name='pyqt-shadow-frame-window-example',
    version='0.0.31',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt shadow(+rounded) frame window example',
    url='https://github.com/yjg30737/pyqt-shadow-frame-window-example.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-frameless-window>=0.0.1'
    ]
)