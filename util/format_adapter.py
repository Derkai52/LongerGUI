VALID_SEPARATORS = (",", ";", " ", ":", "|", "!", "/", "-", "+", "=", "%", "(", ")", "_")

# Hex转换器
def format_hex_bytes(src):
    text = ""
    for s in str(src).split("0x"):
        if s != "":
            s = s.zfill(2)
            text += (s + " ")
    return text

# Ascii码验证器
def check_ascii_character(chars) -> bool:
    for c in chars:
        if ord(c) > 255:
            return False
    return True