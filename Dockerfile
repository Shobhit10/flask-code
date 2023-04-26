FROM centos:7

# Install Python and required packages
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python-pip python-devel gcc && \
    yum clean all

# Copy application code to container
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

