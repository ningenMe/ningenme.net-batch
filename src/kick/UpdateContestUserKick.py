#coding: UTF-8
import sys
import pathlib
path = pathlib.Path(__file__)
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../service')
import Log
import UpdateContestUserService

def kick():
    Log.info(str(path.name) + ": start")
    UpdateContestUserService.main("atcoder")
    Log.info(str(path.name) + ": end\n")

if __name__ == "__main__":
    kick()