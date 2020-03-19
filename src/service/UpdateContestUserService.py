import GetAtcoderUserService as atcoder

def main(site="atcoder"):
    user_info = []
    # get user info
    if site == "atcoder":
        user_info = atcoder.main()
    # update user info    
