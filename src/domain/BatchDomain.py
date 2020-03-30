import sys
import pathlib

path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
import Log
import Database

class BatchDomain:
    def updateUserListPageNum(self,site,userListPageNum):
        database = Database.Datebase()
        query = "REPLACE INTO batch VALUES ('all_%s_user_list_page','%d');" % (site,userListPageNum)
        database.update(query)
        return
