"""To Setup GitHub Self Hosted Runner (Note: Get these commands from your GitHub Repo -> Settings -> Actions -> Runner)"""

# Update system packages first
sudo apt update && sudo apt upgrade -y

# Create a directory for GitHub runner
mkdir actions-runner && cd actions-runner

# Download the latest runner package
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz

# Extract the installer
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

# Configure the runner
# Replace <REPOSITORY_URL> and <TOKEN> with values from your GitHub repository
./config.sh --url <REPOSITORY_URL> --token <TOKEN>

# Install and start the runner service
sudo ./svc.sh install
sudo ./svc.sh start

# Check the service status
sudo ./svc.sh status


"""To Setup Docker"""

# Install required packages
sudo apt install -y ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update apt package index
sudo apt update

# Install Docker Engine
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add your user to docker group (replace 'ubuntu' with your username if different)
sudo usermod -aG docker ubuntu
newgrp docker

# Test Docker installation
docker --version
docker run hello-world


"""Ensure Docker works properly with Runner"""

# Verify Docker permissions
ls -l /var/run/docker.sock
groups
docker ps


"""Required GitHub Repository Secrets"""
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
AWS_ECR_REPO_URI
OPENAI_API_KEY
WEATHER_API_KEY
SERPER_API_KEY
AMADEUS_API_KEY
AMADEUS_API_SECRET
SSH_KEY