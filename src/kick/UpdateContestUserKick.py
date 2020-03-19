#coding: UTF-8
import sys
import os

sys.path.append(os.path.dirname(__file__)+'/../lib')
sys.path.append(os.path.dirname(__file__)+'/../service')
import Log
import UpdateContestUserService

def kick():
    Log.info(os.path.basename(__file__) + ": start")
    UpdateContestUserService.main("atcoder")
    Log.info(os.path.basename(__file__) + ": end\n")

if __name__ == "__main__":
    kick()