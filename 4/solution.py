from bs4 import BeautifulSoup
import re

html = """
<html>
<head>
    <title>My first web page</title>
</head>
<body>
<h1>My first web page</h1>
<h2>What this is tutorial</h2>
<p>A simple page put together using HTML. <em>I said a simple page.</em>.</p>
<ul>
    <li>To learn HTML</li>
    <li>
        To show off
        <ol>
            <li>To my boss</li>
            <li>To my friends</li>
            <li>To my cat</li>
            <li>To the little talking duck in my brain</li>
        </ol>
    </li>
    <li>Because I have fallen in love with my computer.</li>
</ul>
<h3>Where to find the tutorial</h3>
<p><a href="http://www.aaa.com"><img src=http://www.aaa.com/badge1.gif></a></p>
<h4>Some random table</h4>
<table>
    <tr class="tutorial1">
        <td>Row 1, cell 1</td>
        <td>Row 1, cell 2<img src=http://www.bbb.com/badge2.gif></td>
        <td>Row 1, cell 3</td>
    </tr>
    <tr class="tutorial2">
        <td>Row 2, cell 1</td>
        <td>Row 2, cell 2</td>
        <td>Row 2, cell 3<img src=http://www.ccc.com/badge3.gif></td>
    </tr>
</table>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Print the text of the <title> element by navigating the HTML tags
print("a. " + soup.title.get_text())

# Print the text of the second <li> element inside the <ol> below "To show off"
# by navigating the HTML tags
print("b. " + soup.ol.find_all('li')[1].get_text())

# Print all <td> elements in the first <tr> row of the table by navigating the
# HTML tags
td_list = soup.tr.find_all('td')
print("c. ", end="")
for item in td_list:
    print(item)

# Print the text of the <h2> element that contains the word "tutorial" by
# navigating the HTML tags and using a RegEx
print("d. " + soup.find('h2', string=re.compile(r"tutorial")).get_text())

# Print all text nodes that contain the word HTML by using a RegEx
contains_html = soup.find_all(string = re.compile(r"HTML"))
print("e. ", end="")
for item in contains_html:
    print(item)

# Print all <td> elements in the second <tr> row of the table by navigating the
# HTML tags
td_list = soup.table.find_all('tr')[1].find_all('td')
print("f. ", end="")
for item in td_list:
    print(item)

# Print all <img> tags contained within the <table> element by navigating the
# HTML tags
img_list = soup.table.find_all('img')
print("g. ", end="")
for item in img_list:
    print(item)