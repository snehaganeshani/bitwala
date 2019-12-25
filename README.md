#Task1

In this task I have used Ansible and Docker to deploy flask app which is accessible over https via nginx and uWSGI.

1.Install Ansible 
   Install ansible on of the machine which will be used to run playbook

   sudo apt-add-repository ppa:ansible/ansible
   sudo apt update
   sudo apt install ansible

   After ansible is installed, make sure to add all the hosts which will ne managed by ansible.

2.Once initial setup is completed, you can clone this repo and run ansible-playbook --ask-vault-pass site.yml which will:
  
  a. Decrypt certificate file.
 
  b. Install Docker CE on host specified in task1/ansible/site.yml
  
  c. Copy all dependencies and config file to host like Dockerfile, requirement.txt, configs related to nginx, uWSGI and certificates.
  
  d. Create Ansible image using Dockerfile
  
  e. Finally build container using image created in above steps on port 443 and 80.

3.Container is finally deployed, you can check your app using :
  
  Https://public ip of your machine:443


#Task2

In this you will create lambda and SNS topic using ansible and serverless
 
1. Prequisite:
   Run below commands to install node, npm and serverless
      sudo apt-get update
      sudo apt-get install nodejs
      sudo apt-get install npm
      npm install -g serverless
      Finnay create project serverless create --template aws-python3 --path ~/bitwala/task2/serverless-task
      
2.Run ansible-playbook lambda.yml , this playbook will:

  a. Run serverless module on local machine on which ansible is installed.
  
  b. Serverless module will trigger CouldFormation on AWS and create lambda and API gateway on the region specified and also copy the configuration on S3 and create SNS topic.
 
NOTE : For running task2 you will need configure AWS credentials
