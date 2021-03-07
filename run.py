import sys

from rom import ROM

if __name__ == "__main__":
    params = sys.argv[1:]

    try:
        rom = ROM(params[0])
    except Exception:
        print("Unable to open NDS File")

    try:
        save_location = params[1] if len(params) > 1 else "icon.png"
        rom.load_image(save_location)
    except Exception:
        print("Unable to extract icon")
    finally:
        rom.close()
