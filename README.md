## Installing Locally

Install python venv
```
sudo apt install python3.12-venv  
```
Create virtual env. Make sure you're at root level of repository  
```commandline
 python3 -m venv sustainabletextautomation 
``` 
Activate virtual env  
```commandline
source sustainabletextautomation/bin/activate    
pip install pytest-playwright  
playwright install  
```
## Add variables file to repository
Include a variables.env file inside the automation directory before proceeding  
To run  
```commandline
pytest
```

## Using Docker
### Build image
```commandline
docker build -t sustextautomation .  
```
### Run image
```commandline
docker run sustextautomation
```

### Useful Debugging Steps
```commandline
docker build --no-cache -t sustextautomation .
```
Change "pytest" in CMD command in Dockerfile to "bash", and run following
```commandline
docker run -it sustextautomation
```


Using Github
```
git clone https://github.com/ana108/sustextautomation.git
```

Creating a branch
```
git checkout -b updateReadmeWithGithub
```

Add remote, to enable pushing changes to github
```
git remote add "origin" git@github.com:ana108/sustextautomation.git

```