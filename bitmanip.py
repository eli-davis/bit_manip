# bit_manip

###########################################################################
# bitstring, words (string and hex), bytes (char and hex)

# def char_to_bitstring

def nibble_to_bitstring(nibble):
    bitstring = ""
    for i in [8, 4, 2, 1]:
        if nibble >= i:
            bitstring += "1"
            nibble -= i
        else:
            bitstring += "0"
    return bitstring

def hex_byte_to_bitstring(byte):
    bitstring = ""
    for i in [128, 64, 32, 16, 8, 4, 2, 1]:
        if byte >= i:
            bitstring += "1"
            byte -= i
        else:
            bitstring += "0"
    return bitstring

def hex_word_to_bitstring(word):
    bitstring = ""
    byte = [0, 0, 0, 0]
    byte[0] = (word >> 24) & 0xFF
    byte[1] = (word >> 16) & 0xFF
    byte[2] = (word >> 8) & 0xFF
    byte[3] = word & 0xFF
    # for i in [0, 1, 2, 3]:
    #    print ("0x{:X}").format(byte[i])
    for i in [0, 1, 2, 3]:
        bitstring += hex_byte_to_bitstring(byte[i])
    return bitstring

def str_word_to_bitstring(word):
    bitstring = ""
    # for i in [0, 1, 2, 3]:
    #    print ("0x{:X}").format(byte[i])
    for i in [0, 1, 2, 3]:
        bitstring += hex_byte_to_bitstring(ord(word[i]))
    return bitstring

def bitstring_to_str_word(bitstring):
    word = ""
    bitstring1 = bitstring[0:8]
    bitstring2 = bitstring[8:16]
    bitstring3 = bitstring[16:24]
    bitstring4 = bitstring[24:32]
    word += bitstring_to_char(bitstring1)
    word += bitstring_to_char(bitstring2)
    word += bitstring_to_char(bitstring3)
    word += bitstring_to_char(bitstring4)
    return word

def bitstring_to_hex_word(bitstring):
    bitstring0 = bitstring[0:8]
    bitstring1 = bitstring[8:16]
    bitstring2 = bitstring[16:24]
    bitstring3 = bitstring[24:32]
    byte0 = bitstring_to_hex_byte(bitstring0)
    byte1 = bitstring_to_hex_byte(bitstring1)
    byte2 = bitstring_to_hex_byte(bitstring2)
    byte3 = bitstring_to_hex_byte(bitstring3)
    byte = [0, 0, 0, 0]
    byte[0] = (byte0 << 24)
    byte[1] = (byte1 << 16)
    byte[2] = (byte2 << 8)
    byte[3] = byte3
    hex_word = byte[0] | byte[1] | byte[2] | byte[3]
    return hex_word

def hex_word_to_str_word(hex_word):
    bitstring = hex_word_to_bitstring(hex_word)
    str_word = bitstring_to_str_word(bitstring)
    return str_word

def str_word_to_hex_word(str_word):
    bitstring = str_word_to_bitstring(str_word)
    hex_word = bitstring_to_hex_word(bitstring)
    return hex_word

def bitstring_to_hex_nibble(bitstring):
    value = 0
    exponent = 0
    while len(bitstring) > 0:
        if bitstring[-1] == "1":
            value += 2 ** exponent
        exponent += 1
        bitstring = bitstring[:-1]
    return value

def bitstring_to_hex_byte(bitstring):
    new_char = bitstring_to_char(bitstring)
    new_byte = ord(new_char)
    return new_byte

def bitstring_to_char(bitstring):
    value = 0
    exponent = 0
    while len(bitstring) > 0:
        if bitstring[-1] == "1":
            value += 2 ** exponent
        exponent += 1
        bitstring = bitstring[:-1]
    byte = chr(value)
    return byte

############################################################################
