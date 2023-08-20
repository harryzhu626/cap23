# capstone: opinion mining movies on reddit

### Register a reddit account
to make the reddit submission extraction pipeline work, you need user_agent, client_id, client_secret from your reddit account. register for one if you don't already have one. here's the official guide https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps  

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
