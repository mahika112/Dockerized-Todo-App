FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the local 'app/' folder into the container's '/app'
# This includes app.py, requirements.txt, and the templates/ folder.
COPY app/ /app/

# Install dependencies.
# Since WORKDIR is /app, and requirements.txt is at /app/requirements.txt, 
# we only need the filename.
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

