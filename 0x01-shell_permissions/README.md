# 0x01. Shell, permissions
## Learning Objectives

### Permissions
1. What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do?
2. Linux file permissions.
3. How to represent each of the three sets of permissions (owner, group, and other) as a single digit.
4. How to change permissions, owner and group of a file
5. Why can’t a normal user `chown` a file?
6. How to run a command with root privileges.
7. How to change user ID or become superuser.

### Other Man Pages
1. How to create a user.
2. How to create a group.
3. How to print real and effective user and group IDs.
4. How to print the groups a user is in.
5. How to print the effective userid.

## Tasks
###  0. My name is Betty
Create a script that changes your user ID to `betty`.
* You should use exactly 8 characters for your command (+1 character for the new line)
###  1. Who am I
Write a script that prints the effective userid of the current user.
###  2. Groups
Write a script that prints all the groups the current user is part of.
###  3. New owner
Write a script that changes the owner of the file `hello` to the user `betty`.
###  4. Empty! 
Write a script that creates an empty file called `hello`.
###  5. Execute 
Write a script that adds execute permission to the owner of the file `hello`.
###  6. Multiple permissions
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
###  7. Everybody! 
Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`.
###  8. James Bond
Write a script that sets the permission to the file hello as follows:
* Owner: no permission at all
* Group: no permission at all
* Other users: all the permissions
###  9. John Doe
Write a script that sets the mode of the file hello to this:
```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```
### 10. Look in the mirror
Write a script that sets the mode of the file hello the same as olleh’s mode.
### 11. Directories
Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
### 12. More directories
Create a script that creates a directory called `dir_holberton` with permissions 751 in the working directory.
### 13. Change group
Write a script that changes the group owner to `holberton` for the file `hello`.
### 14. Owner and group
Write a script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.
### 15. Symbolic links
Write a script that changes the owner and the group owner of the file `_hello` to `betty` and `holberton` respectively.
### 16. If only
Write a script that changes the owner of the file `hello` to `bett`y only if it is owned by the user `guillaume`.
### 17. Star Wars
Write a script that will play the StarWars IV episode in the terminal.
### 18. RTFM
Create a man page.
