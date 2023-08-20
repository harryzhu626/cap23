# capstone: opinion mining movies on reddit

### Register a reddit account
download the repo. log into your reddit account (register for one if you don't). 

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
