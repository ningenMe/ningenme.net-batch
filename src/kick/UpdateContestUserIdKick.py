#coding: UTF-8
import sys
import pathlib
path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
sys.path.append(str(path.parent)+'/../scenario')
import Log
import UpdateContestUserIdScenario

def kick(site="atcoder"):
    Log.info(str(path.name) + ": start")
    UpdateContestUserIdScenario.main(site)
    Log.info(str(path.name) + ": end\n")

if __name__ == "__main__":
    kick()