from dateutil import parser
from datetime import datetime, timedelta
from github import Github
from flask import Flask, jsonify,request
import github


#api tokken 
githubApiTokken="Enter your access token"
g = Github(login_or_token=githubApiTokken)
app=Flask(__name__)



def checkTokken():
    try:
        user=g.get_user()
        return(jsonify({"message":"Authorized Tokken","username":user.login}))
    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))




@app.route("/test")
def api_checkTokken():
    return checkTokken()



@app.route("/createRepo",methods=["POST"])
def api_createRepo():
    repo_name= request.args.get("name")
    repo_desc="" if (request.args.get('desc')==None) else request.args.get('desc')
    repo_private= False if(request.args.get("private")=="False")  else True
    
    try:
        user = g.get_user()
        user.create_repo(repo_name,description=repo_desc,private=repo_private)
        return (jsonify({"Username":user.login,"message":repo_name+" repo is created"}))

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))


@app.route("/repoList")
def api_repoList():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)

        res={
            "username":user.login,
            "repoList":[]
            }
        
        for repo in user.get_repos():
            res["repoList"].append(repo.name)
        
        return(jsonify(res))

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))


@app.route("/topics/list")
def api_topicsList():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        repo_name= request.args.get("repo")
        repo=user.get_repo(repo_name)
        res={
            "username":user.login,
            "repo":repo.name,
            "topics":[]
        }
        for topic in repo.get_topics():
            res["topics"].append(topic)

        return jsonify(res)
    

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))

@app.route("/topics/delete")
def api_topicsDelete():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        repo_name= request.args.get("repo")
        topics = list(request.args.get("topics").split(", "))
        repo=user.get_repo(repo_name)
        topicsList=repo.get_topics()
        for i in topics:
            if(i in topicsList):
                topicsList.remove(i)

        repo.replace_topics(topicsList)
        res={
            "username":user.login,
            "repo":repo.name,
            "topics":repo.get_topics()
        }
        return jsonify(res)

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))

@app.route("/topics/update")
def api_topicsUpdate():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        repo_name= request.args.get("repo")
        topics = list(request.args.get("topics").split(", "))
        repo=user.get_repo(repo_name)
        
        repo.replace_topics(topics)
        res={
            "username":user.login,
            "repo":repo.name,
            "topics":repo.get_topics()
        }

        return jsonify(res)

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))

@app.route("/list/contributors")
def api_listContributors():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        repo_name= request.args.get("repo")
        repo=user.get_repo(repo_name)
        
        res={
            "username":user.login,
            "repo":repo.name,
            "contributors":[i.login for i in repo.get_contributors()]
        }

        return jsonify(res)

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))


@app.route("/list/stargazers")
def api_listStargazers():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        repo_name= request.args.get("repo")
        repo=user.get_repo(repo_name)
        
        res={
            "username":user.login,
            "repo":repo.name,
            "stargazers":[i.login for i in repo.get_stargazers()]
        }

        return jsonify(res)

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))


@app.route("/repoListSpecial")
def api_repoListSpecial():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)

        res={
            "username":user.login,
            "repoList":[]
            }
        
        for repo in user.get_repos():
            if (repo.forks_count >5 and repo.stargazers_count>5):
                temp={"reponame":repo.name,"stars":repo.stargazers_count,"forks":repo.forks_count}
                res["repoList"].append(temp)
                
        return(jsonify(res))

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))

@app.route("/list/stargazers/special")
def api_listStargazersSpecial():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        templist={}
        stargazersList=[]
        for repo in user.get_repos():
            for st in repo.get_stargazers():
                if (st.login not in templist):
                    templist[st.login]=1
                else:
                    templist[st.login]+=1
        for i in templist:
            if(templist[i]>2):
                stargazersList.append(i)

        res={
            "username":user.login,
            "stargazers list":stargazersList
        }
        return jsonify(res)
        
    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))


@app.route("/list/stargazers/special2")
def api_listStargazersSpecial2():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        templist={}
        stargazersList=[]
        for repo in user.get_repos():
            for st in repo.get_stargazers():
                if (st.login not in templist):
                    templist[st.login]=1
                else:
                    templist[st.login]+=1
        for i in templist:
            if(templist[i]==2):
                stargazersList.append(i)

        res={
            "username":user.login,
            "stargazers list":stargazersList
        }
        return jsonify(res)

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))


@app.route("/list/commits")
def api_listcommits():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        repoList=[]
        for repo in user.get_repos():
            if(repo.size==0):
                continue
            count=0
            for commit in repo.get_commits():
                temp= list(commit.stats.last_modified.split(" "))
                tempDate=temp[1]+" "+temp[2]+" "+temp[3]
                commitDate=parser.parse(tempDate)
                past = datetime.now() - timedelta(days=10)
                
                if(commitDate>past):
                    count+=1
                    if(count>5):
                        repoList.append(repo.name)
                        break
                else:
                    break

        res={
            "username":user.login,
            "repoList":repoList
        }
        return jsonify(res)

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred"+str(e)}))

@app.route("/list/commits/owner")
def api_listcommitsOwner():
    username=request.args.get("username")
    try:
        user=g.get_user() if(username==None) else g.get_user(username)
        repoList=[]
        for repo in user.get_repos():
            if(repo.size==0):
                continue
            count=0
            for commit in repo.get_commits():
                temp= list(commit.stats.last_modified.split(" "))
                tempDate=temp[1]+" "+temp[2]+" "+temp[3]
                commitDate=parser.parse(tempDate)
                past = datetime.now() - timedelta(days=10)
                
                if(commitDate>past):
                    if(commit.author.login==user.login):
                        count+=1
                        if(count>5):
                            repoList.append(repo.name)
                            break
                else:
                    break

        res={
            "username":user.login,
            "repoList":repoList
        }
        return jsonify(res)

    except github.BadAttributeException as e:
        return(jsonify({"Error":e.data.get("message"),"message":"Check api tokken or username"}))
    except Exception as e:
        return(jsonify({"message":"Unknown error occurred "+str(e)}))


if __name__=="__main__":
    app.run(debug=True)
