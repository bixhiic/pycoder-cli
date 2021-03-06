import click


dec_dict = {' ': '127', '!': '033', '"': '034', '#': '035', '$': '036', '%': '037', '&': '038', "'": '039', '(': '040', ')': '041', '*': '042', '+': '043', ',': '044', '-': '045', '.': '046', '/': '047', '0': '048', '1': '049', '2': '050', '3': '051', '4': '052', '5': '053', '6': '054', '7': '055', '8': '056', '9': '057', ':': '058', ';': '059', '<': '060', '=': '061', '>': '062', '?': '063', '@': '064', 'A': '065', 'B': '066', 'C': '067', 'D': '068', 'E': '069', 'F': '070', 'G': '071', 'H': '072', 'I': '073', 'J': '074', 'K': '075', 'L': '076', 'M': '077', 'N': '078', 'O': '079', 'P': '080', 'Q': '081', 'R': '082', 'S': '083', 'T': '084', 'U': '085', 'V': '086', 'W': '087', 'X': '088', 'Y': '089', 'Z': '090', '[': '091', '\\': '092', ']': '093', '^': '094', '_': '095', '`': '096', 'a': '097', 'b': '098', 'c': '099', 'd': '100', 'e': '101', 'f': '102', 'g': '103', 'h': '104', 'i': '105', 'j': '106', 'k': '107', 'l': '108', 'm': '109', 'n': '110', 'o': '111', 'p': '112', 'q': '113', 'r': '114', 's': '115', 't': '116', 'u': '117', 'v': '118', 'w': '119', 'x': '120', 'y': '121', 'z': '122', '{': '123', '|': '124', '}': '125', '~': '126'}
oct_dict = {' ': '177', '!': '041', '"': '042', '#': '043', '$': '044', '%': '045', '&': '046', "'": '047', '(': '050', ')': '051', '*': '052', '+': '053', ',': '054', '-': '055', '.': '056', '/': '057', '0': '060', '1': '061', '2': '062', '3': '063', '4': '064', '5': '065', '6': '066', '7': '067', '8': '070', '9': '071', ':': '072', ';': '073', '<': '074', '=': '075', '>': '076', '?': '077', '@': '100', 'A': '101', 'B': '102', 'C': '103', 'D': '104', 'E': '105', 'F': '106', 'G': '107', 'H': '110', 'I': '111', 'J': '112', 'K': '113', 'L': '114', 'M': '115', 'N': '116', 'O': '117', 'P': '120', 'Q': '121', 'R': '122', 'S': '123', 'T': '124', 'U': '125', 'V': '126', 'W': '127', 'X': '130', 'Y': '131', 'Z': '132', '[': '133', '\\': '134', ']': '135', '^': '136', '_': '137', '`': '140', 'a': '141', 'b': '142', 'c': '143', 'd': '144', 'e': '145', 'f': '146', 'g': '147', 'h': '150', 'i': '151', 'j': '152', 'k': '153', 'l': '154', 'm': '155', 'n': '156', 'o': '157', 'p': '160', 'q': '161', 'r': '162', 's': '163', 't': '164', 'u': '165', 'v': '166', 'w': '167', 'x': '170', 'y': '171', 'z': '172', '{': '173', '|': '174', '}': '175', '~': '176'}
hex_dict = {' ': '7F', '!': '21', '"': '22', '#': '23', '$': '24', '%': '25', '&': '26', "'": '27', '(': '28', ')': '29', '*': '2A', '+': '2B', ',': '2C', '-': '2D', '.': '2E', '/': '2F', '0': '30', '1': '31', '2': '32', '3': '33', '4': '34', '5': '35', '6': '36', '7': '37', '8': '38', '9': '39', ':': '3A', ';': '3B', '<': '3C', '=': '3D', '>': '3E', '?': '3F', '@': '40', 'A': '41', 'B': '42', 'C': '43', 'D': '44', 'E': '45', 'F': '46', 'G': '47', 'H': '48', 'I': '49', 'J': '4A', 'K': '4B', 'L': '4C', 'M': '4D', 'N': '4E', 'O': '4F', 'P': '50', 'Q': '51', 'R': '52', 'S': '53', 'T': '54', 'U': '55', 'V': '56', 'W': '57', 'X': '58', 'Y': '59', 'Z': '5A', '[': '5B', '\\': '5C', ']': '5D', '^': '5E', '_': '5F', '`': '60', 'a': '61', 'b': '62', 'c': '63', 'd': '64', 'e': '65', 'f': '66', 'g': '67', 'h': '68', 'i': '69', 'j': '6A', 'k': '6B', 'l': '6C', 'm': '6D', 'n': '6E', 'o': '6F', 'p': '70', 'q': '71', 'r': '72', 's': '73', 't': '74', 'u': '75', 'v': '76', 'w': '77', 'x': '78', 'y': '79', 'z': '7A', '{': '7B', '|': '7C', '}': '7D', '~': '7E'}
bin_dict = {' ': '01111111', '!': '00100001', '"': '00100010', '#': '00100011', '$': '00100100', '%': '00100101', '&': '00100110', "'": '00100111', '(': '00101000', ')': '00101001', '*': '00101010', '+': '00101011', ',': '00101100', '-': '00101101', '.': '00101110', '/': '00101111', '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011', '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111', '8': '00111000', '9': '00111001', ':': '00111010', ';': '00111011', '<': '00111100', '=': '00111101', '>': '00111110', '?': '00111111', '@': '01000000', 'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000', 'Y': '01011001', 'Z': '01011010', '[': '01011011', '\\': '01011100', ']': '01011101', '^': '01011110', '_': '01011111', '`': '01100000', 'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110', 'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100', 'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000', 'y': '01111001', 'z': '01111010', '{': '01111011', '|': '01111100', '}': '01111101', '~': '01111110'}




@click.command()
@click.option('-d', type=click.File(mode='r', encoding='ascii'), help="Decode file text from chosen format")
@click.option('-e', type=click.File(mode='r', encoding='ascii'), help="Encode file text to chosen format")
@click.option('-f', type=click.Choice(choices=['dec', 'oct', 'hex', 'bin']), help="Choose a format")
@click.option('-g', type=click.Choice(choices=['yes', 'no']), help="Create file or just prompt it")
def cli( d, e, f, g):
    '''This script help u to encode or decode text files in 
    differents formats.

    Available formats
    
    [->] Decimal
    
    [->] Octal 
    
    [->] Hexadecimal 
    
    [->] Binary
    '''
    

    if e and f:
        data = e.read().replace('\n', '~')
        content = crypt(data, f)
        generate(g=g, content=content)

    elif d and f:
            data = d.read()
            code = decrypt(data=data, format=f)
            content = code.replace('~', '\n')
            generate(g=g, content=content)

        



def crypt(data, format):
    '''Crypt data to selected format'''
    
    chain = ''
    result = []
    
    if format == 'dec':
        for i in data:
            value = dec_dict.get(i)
            result.append(str(value))

    elif format == 'oct':
        for i in data:
            value = oct_dict.get(i)
            result.append(str(value))

    elif format == 'hex':
        for i in data:
            value = hex_dict.get(i)
            result.append(str(value))
    
    elif format == 'bin':
        for i in data:
            value = bin_dict.get(i)
            result.append(str(value))
                                        
    return chain.join(result)




def decrypt(data, format):
    '''Convert text to chosen format '''
    
    text = list(data)
    num = ""
    content = ""

    if format == 'dec':
        for i in text:
            num += i
            if len(num) > 2:
                for k,v in dec_dict.items():
                    if num == v:
                        content += k
                        num = ""             
    elif format == 'oct':
        for i in text:
            num += i
            if len(num) > 2:
                for k,v in oct_dict.items():
                    if num == v:
                        content += k
                        num = ""
    elif format == 'hex':
        for i in text:
            num += i
            if len(num) > 1:
                for k,v in hex_dict.items():
                    if num == v:
                        content += k
                        num = ""                    
    elif format == 'bin':
        for i in text:
            num += i
            if len(num) > 7:
                for k,v in bin_dict.items():
                    if num == v:
                        content += k
                        num = ""

    
    if len(content) == 0:
        return "Something is wrong.. maybe you should check the format!"                    

    return content




def generate(g, content):
    if g == 'yes':
        filename = input('\nFilename: ')
        with open(file=filename, mode='w') as fl:
            fl.write(content)
            fl.close()
            print(f'\n[Done] File {filename} created!\n')

    elif g == 'no':
        print(f'\n\n{content}\n\n')
        
