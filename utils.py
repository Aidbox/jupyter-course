def pprint(d):
    from json import dump
    import sys

    dump(d, sys.stdout, indent=2)
