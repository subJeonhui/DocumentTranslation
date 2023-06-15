import re


class Loader:
    def load(self):
        pass


class HTMLLoader(Loader):
    def __init__(self, path: str):
        self.path = path

    def load(self):
        f = open(self.path, 'r')
        html = f.read()
        f.close()
        html = html.split('</head>')
        head = html[0] + '</head>'
        html[1] = html[1].replace('&nbsp;', ' ').replace('&amp;', '&')
        body = []
        status = True
        for line in re.split('<', html[1]):
            if len(line.strip()) > 0:
                body.append((False, "<"))

            if len(line) >= 5 and line[:5] in ['scrip', 'style']:
                status = False

            data = line.split('>')

            if status and len(data) >= 2 and len(data[1].strip()) != 0:
                body.append((False, data[0]))
                body.append((False, '>'))
                body.append((True, data[1]))
            else:
                body.append((False, line))

            if len(line) >= 6 and line[:6] in ['/scrip', '/style']:
                status = True

        return [(False, head)] + body


class MarkDownLoader(Loader):
    def __init__(self, path):
        self.path = path

    def load(self):
        f = open(self.path, 'r')
        md = f.readlines()
        f.close()

        body = []
        for line in md:
            if line[0] != '|' and len(line.strip()) >= 5 and line[0] != '!':
                body.append((False, line + '  \n' + ('>' if line[0] != '-' else '- >')))
                translate_line = re.sub(r'[*#\[\]\-]+|(\(.+\))', '', line.strip()).strip()
                body.append((True, translate_line))
                body.append((False, '  \n\n'))
            else:
                body.append((False, line))

        return body

