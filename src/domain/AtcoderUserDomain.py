import sys
import pathlib

path = pathlib.Path(__file__).resolve()
sys.path.append(str(path.parent)+'/../lib')
import Log
import Database

class AtcoderUserDomain:
    def updateUserId(self,userIdList):
        if not userIdList:
            return
        database = Database.Datebase()
        query = "REPLACE INTO atcoder_user (atcoder_id,deleted_time) VALUES"
        for userId in userIdList:
            query += " ('%s',NULL)," % userId
        query = query[:-1]
        database.update(query)
        return