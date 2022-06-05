##  Pycoder Cli Version


### How to install (Linux)

```
git clone https://github.com/bixhiic/pycoder-cli.git
cd pycoder-cli
python3 -m venv env
source env/bin/activate
pip install --editable .

pycodercli --help
```

### How it works

This script reads a file to convert it into a code plain text from/to the chosen format (decimal, octal, hexadecimal, binary).

Example: suppose you have a file called ‘myscript.py’ in your project.

You can use -e myscript.py to encode and -f dec for decimal format. 

if you want to decode the text, you must use -d file and -f dec, using the format that file has  to convert to original version.


## License
[MIT](https://choosealicense.com/licenses/mit/)