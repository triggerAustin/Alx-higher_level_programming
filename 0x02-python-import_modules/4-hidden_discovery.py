#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden_contents = dir(hidden_4)
    for names in hidden_contents:
        if names[:2] == "__":
            continue
        else:
            print(names)
