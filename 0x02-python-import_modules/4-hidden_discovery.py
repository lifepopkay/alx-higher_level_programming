#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hd

    all_names = dir(hd)

    for names in all_names:
        """ this will find the first two letter in
        each name """
        if name[:2] != '__':
            print(name)
