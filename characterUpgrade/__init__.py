"""
The most Pythonic way to import a module from another folder is to place an empty file named __init__.py. into that folder and use the relative path with the dot notation.
For example, a module in the parent folder would be imported with from .. import module. The __init__.py file signals to Python that the folder should be treated as package.
"""