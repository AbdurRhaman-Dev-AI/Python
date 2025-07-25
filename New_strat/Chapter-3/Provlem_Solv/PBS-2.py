#___In heare we write a code using some replace funion

letter  = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

print(letter.replace('<|NAME|>', 'Marin').replace('<|DATE|>', '1st January 2026'))