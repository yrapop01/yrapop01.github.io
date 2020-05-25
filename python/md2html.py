import sys

HIGHSTART = '```python\n'
HIGHEND = '```\n'

def replpair(what, by_start, by_end, s):
    inside = False

    for c in s:
        if c == what:
            yield by_end if inside else by_start
            inside = not inside
        else:
            yield c

def pre(lines):
    gathered = ''

    for line in lines:
        if gathered:
            if line.endswith(HIGHEND):
                yield gathered + line[:-len(HIGHEND)] + '</code></pre>\n'
                gathered = ''
            else:
                gathered += line
            continue

        if line.startswith(HIGHSTART):
            gathered = '<pre><code class="python">' + line[len(HIGHSTART):]
            continue

        yield line

def inline(line):
    line = ''.join(replpair('*', '<em>', '</em>', line))
    line = ''.join(replpair('`', '<code>', '</code>', line))
    #line = line.replace(' < ', ' &lt; ').replace(' > ', '&gt;')
    return line

def headers(lines):
    for line in lines:
        if line.startswith('### '):
            yield '<h3>' + inline(line[4:-1]) + '</h3>\n'
        elif line.startswith('## '):
            yield '<h2>' + inline(line[3:-1]) + '</h2>\n'
        elif line.startswith('# '):
            yield '<h1>' + inline(line[2:-1]) + '</h1>\n'
        else:
            yield line

def paragraphs(lines):
    gather = ''

    for line in lines:
        if line.startswith('<'):
            if gather and not gather.isspace():
                yield '<p>' + inline(gather).strip() + '</p>\n\n'
            gather = ''
            yield line
            continue

        if line == '\n' and gather.endswith('\n'):
            if not gather.isspace():
                yield '<p>' + inline(gather).strip() + '</p>\n\n'
            gather = ''
            continue
            
        gather += line

    if gather:
        yield gather

def main(inp):
    lines = paragraphs(headers(pre(inp)))
    
    for line in lines:
        print(line, end='')
    print()


if __name__ == "__main__":
    main(sys.stdin)
