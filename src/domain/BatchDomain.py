import sys
import pathlib

path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
import Log
import Database

class BatchDomain:
    def updateAllUserListPageNum(self,site,userListPageNum):
        database = Database.Datebase()
        query = "REPLACE INTO batch VALUES ('all_%s_user_list_page','%d');" % (site,userListPageNum)
        database.update(query)
        return

    def getCurrentUserListPageNum(self,site): 
        database = Database.Datebase()
        query = "SELECT * FROM batch WHERE name = 'current_%s_user_list_page'" % site
        res = database.select(query)
        if not res :
            Log.error(str(path.parent) + " failed\n")
            sys.exit(0)
        name,info = res[0] 
        return int(info)

    def updateCurrentUserListPageNum(self,site,userListPageNum):
        database = Database.Datebase()
        query = "REPLACE INTO batch VALUES ('current_%s_user_list_page','%d');" % (site,userListPageNum)
        database.update(query)
        return
