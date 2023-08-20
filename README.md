# capstone: opinion mining movies on reddit

### Get authentication tokens from reddit 
For the reddit submission extraction pipeline to work, you need user_agent, client_id, client_secret tokens from your reddit account (register if you don't have one already). 

#### Get client_secret
Log in your reddit account, go to https://www.reddit.com/prefs/apps. click 'create app' or 'create another app', choose 'script' among the 4 options, fill in 'name' and 'description'. you can use this website for 'redirect url': http://www.example.com/unused/redirect/uri. After you created the app, you will see on the top a token called 'secret'. Save it. 

here's the official guide https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

#### Get client_id


### Docker image and container

make sure you have docker desktop downloaded and opened. in terminal, cd to the cap23 directory and run the following command to build docker image from dockerfile:

```sh
docker build --tag cap .   
```

After the image finishes building, run this command to run docker image in a container: 

```sh
docker run -dp 5000:5000 cap
```
Go to http://127.0.0.1:5000/. the streamlit app will be running. 
