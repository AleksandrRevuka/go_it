def token_parser(s: str):
    lexemes = ''
    if s:
        for symbol in s:
            if symbol.isdigit():
                lexemes += symbol
            elif symbol in '+-*/':
                lexemes += " " + symbol + ' '
                
            elif symbol in '(':
                lexemes += symbol + ' '
                
            elif symbol in ')':
                lexemes += " " + symbol
              
        return lexemes.split(' ')
    return []
    
print(token_parser('(2+ 3) *4 - 5 * 3'))