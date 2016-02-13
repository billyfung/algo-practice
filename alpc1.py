# input signed integer in the 14­bit range [­8192..+8191]
# convert integer into text encoding, then convert back


def encode_integer(input_int):
    if input_int >= 8192 or input_int <= -8192:
        raise Exception("Invalid input, number not in range")
    else:
        # convert to different range, unsigned 14 bit
        input_int += 8192
        # 7 upper bits
        upper = hex(input_int >> 7)[2:]
        # 7 lower bits
        lower = hex(input_int & 0x7f)[2:]
        if lower == '0':
            lower = '00'
        # format strings and return
        return upper + lower


def decode_bytes(byte):
    # grab first 2 bytes
    high = byte[0:2]
    # grab last 2 bytes
    low = byte[0:2]
    return (int(high,16) <<7 | int(low,16)) - 8192


encode_list = [6111, 340, -2628, -255, 7550]
decode_list = ['0A0A', '0029', '3F0F', '4400', '5E7F']

for entry in encode_list:
    print(encode_integer(entry))

for byte in decode_list:
    print(decode_bytes(byte))