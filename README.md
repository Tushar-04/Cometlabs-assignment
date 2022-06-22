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


