import sys
sys.path.append("\\\\colossus\\User_Folders\\matthew.rowland\\Public\\Python\\lib")
from linq import From
import fileinfo

def main():

    lines = fileinfo.read_all_lines("demo.txt")
    for line in From(lines).where(lambda x: x[:2] == "01").select(lambda x: x[13:]):
        print(line)

main()
