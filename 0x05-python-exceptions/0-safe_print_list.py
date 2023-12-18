#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    track = 0
    while x > 0:
        try:
            print("{}".format(my_list[track]), end = "")
            track += 1
            x -= 1
        except (IndexError):
            pass
        except Exception:
            print("Get all exceptions!")
        finally:
            print("")
    return track
