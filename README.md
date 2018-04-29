# bit and byte ops

import bit_manip

# char to array of 1s and 0s
bit_manip.char_to_bitstring(char)

# decimal value of half-byte to array of 1s and 0s
bit_manip.nibble_to_bitstring(nibble)

# decimal value of byte to array of 1s and 0s
bit_manip.hex_byte_to_bitstring(byte)

# decimal value of uint_32 to array of 1s and 0s
bit_manip.hex_word_to_bitstring(word)

# array of 4 chars to array of 1s and 0s
bit_manip.str_word_to_bitstring(word)

# array of 1s and 0s to array of 4 chars
bit_manip.bitstring_to_str_word(bitstring)

# array of 1s and 0s to array of 4 hex byted
bit_manip.bitstring_to_hex_word(bitstring)

# array of 4 hex bytes to array of 4 ASCII chars
bit_manip.hex_word_to_str_word(hex_word)

# array of 4 ASCII chars to array of 4 hex bytes
bit_manip.str_word_to_hex_word(str_word)
 
# returns numeric value of half-byte
bit_manip.bitstring_to_hex_nibble(bitstring)

# returns numeric value of byte
bit_manip.bitstring_to_hex_byte(bitstring)

# returns ASCII char
bit_manip.bitstring_to_char(bitstring)

