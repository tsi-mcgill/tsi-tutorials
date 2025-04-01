FROM python:3.9-slim

RUN apt-get update && apt-get install -y gosu && rm -rf /var/lib/apt/lists/*

# Use pip to install the requirements
RUN pip install numpy matplotlib jupyterlab notebook ipykernel ipython ipywidgets

# Create a new user and change to that user
ADD entrypoint.sh /home/europa/entrypoint.sh
RUN chmod +x /home/europa/entrypoint.sh

# # Move the europa's home directory
WORKDIR /home/europa

# Set the entrypoint
ENTRYPOINT [ "/home/europa/entrypoint.sh" ]


CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8000"]