# Cometlabs-assignment

## Setting up the environment
1. **Clone repository and installing virtual environment:** 
- Open terminal and run the following code one by one :
```
git clone https://github.com/Tushar-04/Cometlabs-assignment.git
```

- If virtualenv not installed in your system :

```
pip install virtualenv
```
2. **Running virtual environment:**

```
cd .\Cometlabs-assignment\
```

```
virtualenv venv
```
- Following code will enable virtual environment
```
.\venv\Scripts\activate
```
- Note: If you get any errors in the above command, run the following command in powershell as admin, else move to the next step.
```
Set-ExecutionPolicy RemoteSigned
```

3. **Instaling dependencies:**

```
pip install -r requirements.txt
```
4. **Running the api**
- First You need to paste your Github access token in the 9th line of cometLabsApi.py file.
![image](https://user-images.githubusercontent.com/75965694/175099416-cad7a723-45bf-457c-bd5d-080420e63d64.png)
- Now run the following command in terminal where your virtual environment is running
```
py .\cometLabsApi.py
```
- If you see the following screen, it means you followed all of the steps correctly and your API is running on your local host; otherwise, repeat all of the steps correctly.
![image](https://user-images.githubusercontent.com/75965694/175101671-a9fc95ba-e8d4-4ee7-a30b-424439b5c620.png)

- Now you can test all the endponits of the api mentioned in the next section using Postman.

## Testing Endpoints of api
### 1. "http://127.0.0.1:5000/test" : GET Request
**This is an additional end-point to check that your token**
![image](https://user-images.githubusercontent.com/75965694/175105041-2ae3fe92-3a5a-4301-b1c7-56f85e31a5a4.png)
<br>
### 2. "http://127.0.0.1:5000/createRepo" : POST Request
**This is an endpoint that can create a repo with the name provided by the user.**
- **params**
    - name : contains repo name(Required)
    - desc : contains description of repo (Optional)
    - private : contains visibility of repo (Optional,True or False only and True by default)
![image](https://user-images.githubusercontent.com/75965694/175106662-407de4dd-6157-424a-b6f5-8fd885eb2679.png)
<br>

### 3. "http://127.0.0.1:5000/repoList" : GET Request
**This is an endpoint that can list all repos of a user.**
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    ![image](https://user-images.githubusercontent.com/75965694/175107739-596a29e3-1b26-447b-9947-77078e683699.png)

### 4. "http://127.0.0.1:5000/topics/list" : GET Request
**This is an endpoint that return all topis of a given repo of a user.**
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    - repo : contains reponame(Required).
    ![image](https://user-images.githubusercontent.com/75965694/175108601-f7255c99-5b15-409c-a0d7-1faae177efa2.png)
<br>

### 5. "http://127.0.0.1:5000/topics/update" : GET Request
**This is an endpoint that can udate topics of a given repo of a user.**
- **params**
    - username : contains  username(If left blank,the  authenticated user will be considered.).
    - repo : contains reponame(Required).
    - topics : list of new topis in comma-space seperated lower-case string (Required)
    ![image](https://user-images.githubusercontent.com/75965694/175109519-e4189c45-649d-4fd9-87b3-dc160504bb12.png)
  
<br>

### 6. "http://127.0.0.1:5000/topics/delete" : GET Request
**This is an endpoint that can delte topics of a given repo of a user.**
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    - repo : contains reponame(Required).
    - topics : list of topis to be delted in comma-space seperated lower-case string (Required)
    ![image](https://user-images.githubusercontent.com/75965694/175109896-8a8d4e01-ef61-405f-8b73-80e8cc830ad0.png)

<br>

### 7. "http://127.0.0.1:5000/list/contributors" : GET Request
**This is an endpoint that can return list of all contributors of a given repo of a user.**
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    - repo : contains reponame(Required).
    ![image](https://user-images.githubusercontent.com/75965694/175110778-fff2b7af-3138-4e50-872b-461bccc9b67d.png)
<br>


### 8. "http://127.0.0.1:5000/list/stargazers" : GET Request
**This is an endpoint that can return list of all stargazers of a given repo of a user.**
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    - repo : contains reponame(Required).
    ![image](https://user-images.githubusercontent.com/75965694/175111083-3b8ba960-dc5f-48e4-8246-7ccf7eefd1a4.png)

<br>

### 9. "http://127.0.0.1:5000/repoListSpecial" : GET Request
**This is an endpoint to list all the repos of a given user with > 5 stars and > 5 forks.**
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    ![image](https://user-images.githubusercontent.com/75965694/175112243-93ae4b8b-211d-4aab-8ef4-5946f69adff6.png)
<br>

### 10. "http://127.0.0.1:5000/repoListSpecial" : GET Request
**This is an endpoint to list all the stargazers who have started more than 2 repos of a given user**<br>
NOTE : This request can take upto 5 min if number of repo or stargarzers is large
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    ![image](https://user-images.githubusercontent.com/75965694/175113697-ed4e71eb-dc57-44f0-b652-8758715075c1.png)

<br>

### 11. "http://127.0.0.1:5000/repoListSpecial2" : GET Request
**This is an endpoint to list all the stargazers who have started exactly 2 repos of a given user**<br>
NOTE : This request can take upto 5 min if number of repo or stargarzers is large
- **params**
    - username : contains  username(If left blank,the authenticated user will be considered.).
    ![image](https://user-images.githubusercontent.com/75965694/175113905-531fba8e-d3e4-4115-bb8a-c7c25efeaa0a.png)

