FROM python:3.8

# Set the working directory in the container
WORKDIR /cap23

# Copy the requirements file into the container at /app
COPY requirements.txt /cap23/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /cap23/

# Expose the port that Streamlit runs on
EXPOSE 5000

# Define the command to run your Streamlit app when the container starts
CMD ["streamlit", "run", "streamlit.py"]