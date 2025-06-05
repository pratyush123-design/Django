fo = open("foo.txt", "wb")
print("Name of the file:", fo.name)

ret = fo.isatty()
print("Return value:", ret)

fo.close()
import sys
print("is stdin a terminal?",sys.stdin.isatty())
