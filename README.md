# Recipe-Doc-Code-Generator
Generates HTML Recipe File from CSV database

Git procedure

Make sure any changes have been merged to master or that you checkout a branch that you want to make changes to
(what is the command to sync the local repository from the remote? On GUI it is "Sync" in upper right hand corner)

In the GUI, create a new branch for your changes and label descriptively. Shell equivalent is git branch "branch name". 

Make the changes in Notepad++ and save.

The GUI will notice that the file has changed. Navigate to the file(s) that has changed and you will see that the GUI has noticed changes. Add a description of your changes and click the "Commit" button at the bottom of the GUI. Shell equivalent is git commit -m -a "description"

If you wish to merge the branch into the master before pushing to GitHub, in the GUI, after committing your change to the branch, then switch to the master branch. You should see an option button on the left of the timeline to "Update from <name of branch". If you click that button, your branch changes will be merged to the master (I havent found a way to merge branches at the GitHub level), the shell equivalent is: 

git checkout master
git merge <name of branch>   (this will merge your changes to the master branch)

When ready to push to remote respository, then make the branch current in th GUI then click on the endpoint circle of the branch and the button above will allow you to "publish". The shell equivalent follows:

git checkout <name of branch>
git push

or if you just want to merge into the master branch first, then 

git checkout master
git merge <name of branch>   (this will merge your changes to the master branch)
git push

To push changes to GitHub from the GUI, use the "Publish" button

Note: when you change branches in the GUI, Notepad++ may/will notify you that an open file has changed if there is a difference between the files in the different branches.
