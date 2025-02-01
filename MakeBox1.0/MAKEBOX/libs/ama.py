def set_print(text, color):
    colors = {
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "BLUE": "\033[34m",
        "YELLOW": "\033[33m",
        "PURPLE": "\033[35m",
        "AQUA": "\033[36m",
        "NONE": "\033[0m"
    }

    color_code = colors.get(color.upper(), colors["NONE"])
    print(f"{color_code}{text}{colors['NONE']}")
