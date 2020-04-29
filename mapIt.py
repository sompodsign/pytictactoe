# mapIt.py - launches a map in the browser using an address from the clipboard

import pyperclip, webbrowser, sys

if len(sys.argv) > 1:
    # Get address from clipboard
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)






# 870 Valencia St, San Francisco, CA 94110