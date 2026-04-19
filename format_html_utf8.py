from html.parser import HTMLParser
from pathlib import Path

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.indent = 0
        self.lines = []
        self.inline = {'a','span','strong','em','b','i','u','small','sup','sub','br','img','meta','link','input'}

    def _add(self, s):
        self.lines.append('  ' * self.indent + s)

    def handle_decl(self, decl):
        self._add(f'<!{decl}>')

    def handle_comment(self, data):
        self._add(f'<!--{data}-->')

    def handle_starttag(self, tag, attrs):
        attrs_str = ''.join(f' {k}="{v}"' if v is not None else f' {k}' for k, v in attrs)
        is_void = tag in ('br','img','meta','link','input')
        self._add(f'<{tag}{attrs_str}{" /" if is_void else ""}>')
        if tag not in self.inline and not is_void:
            self.indent += 1

    def handle_endtag(self, tag):
        if tag not in self.inline and tag not in ('br','img','meta','link','input'):
            self.indent -= 1
            self._add(f'</{tag}>')

    def handle_data(self, data):
        text = data.strip()
        if text:
            for line in text.splitlines():
                line = line.strip()
                if line:
                    self._add(line)

path = Path('index.html')
html = path.read_text('utf-8')
parser = P()
parser.feed(html)
Path('index_formatted.html').write_text('\n'.join(parser.lines), 'utf-8')
print('WROTE')
