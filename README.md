# capstone: opinion mining movies on reddit

### Docker image and container
To create a Docker image of this Streamlit app, use the `Dockerfile`. To do this, make sure Docker is installed, and then `cd` into this directory (`cap23/`) and run the following command:
```bash
$ docker build --tag cap23 .   
```
Then, to run the Docker container using this image, run the following command: 
```bash
$ docker run -dp 8501:8501 cap23
```
You can then access the Streamlit app at [http://localhost:8501](http://localhost:8501/).
Note: if you're running the server from Docker and are using the "upload" button to upload a .txt file, this .txt file has to be in the Docker container.
