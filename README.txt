## GIT Command while starting from dev machine

First : Create a repository on GITHUB
(
    And you can follow the steps mentioned by GITHUB
    echo "# Test" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/kumaranilbhati/Test.git
    git push -u origin main
)

##OR

1- git init
2- .gitignore
3- git add .
4- git commit -m "First commit of iCoder"
5- git remote add origin https://github.com/kumaranilbhati/iCoder.git  
6- git push -f origin master
7- git pull origin master

## Create a new branch then to work

1- git pull origin master
2- git branch -m feature1
3- git add .
4- git commit -m "Create a new branch and add a file"
5- git push --set-upstream origin feature1

## Again  change something in new feature1 branch
1- git pull
2- git add .
3- git commit -m "Again change a file"
4- git push