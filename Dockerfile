FROM python:3.11

# Set the working directory
WORKDIR /cap23

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install requirements.txt
RUN pip install -r requirements.txt

# Copy current directory contents into the container
COPY . .

# Run streamlit
CMD ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]