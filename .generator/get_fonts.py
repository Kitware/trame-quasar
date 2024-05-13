# search "./.download/fonts_with_urls.css" for remote assets and download them
# produce a new file with "./generator/fonts.css" local paths instead of remote
# this script should run on the top-level directory of the project

import re
from pathlib import Path
from urllib.request import urlretrieve
from urllib.parse import urlparse

ROOT = Path(__file__).parent.parent.absolute()

pattern = re.compile("http[^)]*")  # capture from http until a parenthesis ')'
with open(ROOT / ".download/fonts_with_urls.css", "r") as fonts:
    lines = fonts.read()
    new_lines = lines
    for url in pattern.finditer(lines):
        parsed_url = urlparse(url[0]).path
        destination = Path(parsed_url).name
        urlretrieve(url[0], str(ROOT / ".generator" / destination))
        new_lines = re.sub(url[0], f'"{destination}"', new_lines)

    with open(ROOT / ".generator/fonts.css", "w") as out:
        out.write(new_lines)
