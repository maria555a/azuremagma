import re
import codecs

def delete_html_tags(html_text, ready_text='cleaned.txt'):
    with codecs.open(html_text, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r"<.*?>", '', html)

    lines = cleaned_text.splitlines()
    filled_lines = [line.strip() for line in lines if line.strip() != '']
    result = '\n'.join(filled_lines)

    with codecs.open(ready_text, 'w', 'utf-8') as output:
        output.write(result)

    print(f"Save cleaned text in '{ready_text}'")
    print(result)

example_text = """
<html>
  <head>
    <title>Приклад HTML</title>
  </head>
  <body>
    <h1>Заголовок сторінки</h1>
    <p>Це <b>жирний</b> текст, а це <i>курсив</i>.</p>
    <p>Ось список:</p>
    <ul>
      <li>Пункт 1</li>
      <li>Пункт 2</li>
    </ul>
  </body>
</html>
"""

with codecs.open('example.html', 'w', 'utf-8') as f:
    f.write(example_text)

delete_html_tags('example.html')
