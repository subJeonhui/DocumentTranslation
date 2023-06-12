from enum import Enum


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class FileExt(StrEnum):
    HTML = 'html'
    MARKDOWN = 'md'
    Another = ''

    @staticmethod
    def toExt(extStr):
        extStr = extStr.lower()
        if extStr == FileExt.HTML.value.lower():
            return FileExt.HTML
        elif extStr == FileExt.MARKDOWN.value.lower():
            return FileExt.MARKDOWN
        else:
            return FileExt.Another

    @staticmethod
    def validation(ext):
        if ext == FileExt.HTML:
            return True
        elif ext == FileExt.MARKDOWN:
            return True
        else:
            return False


class Component:
    """
    Composite Pattern
    """

    def tree(self):
        pass

    def show_tree(self, lv, option):
        pass


class File(Component):
    """
    Leaf
    """

    def __init__(self, name, path):
        self.name = name
        self.path = path
        extStr = name.split('/')[-1].split('.')[-1]
        self.ext = FileExt.toExt(extStr)

    def tree(self):
        return self

    def show_tree(self, lv, option=False):
        if not option and not FileExt.validation(self.ext): return ''
        lvt = '\t' * lv
        if not FileExt.validation(self.ext):
            return f"{lvt} ▷ {self.name}\n"
        else:
            return f"{lvt} ➤ {self.name}\n"

    def fullPath(self):
        return f"{self.path}/{self.name}"


class Directory(Component):
    """
    Composite
    """

    def __init__(self, path):
        self.path = path
        self.components = []

    def tree(self):
        return [c.tree() for c in self.components]

    def add(self, component: Component):
        self.components.append(component)

    def show_tree(self, lv=0, option=False):
        lvt = '\t' * lv
        dirName = self.path.split('/')
        s = f"{lvt} ❖ /{dirName[-1]}\n"
        for c in self.components:
            s += f"{c.show_tree(lv + 1, option=option)}"
        return s
