# 0x19. Postmortem

## Description
What you should learn from this project:

---

### [0. My first postmortem](./README.md)
Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:

Issue Summary:
* Start Date: 02/23/20 12:00 PM PST
* End Date: 02/23/20 1:00 PM PST
* 10% of users were complaining that they were getting a 404 error when trying to log into their page.
* The root casue was that GET requests weren't being properly sent.


* The issue was detected at 12pm.
* The issue was detected when users started contacting cutomer service about loging into their account
* The engineering team for that department was contacted to view bugs in the system.
* Misleading investigation was that certain servers were down. There were various tests taken to ensure it wasn't the servers.
* The account and log ion team was contacted to take care fo the issue. It was escalated to the head of the team.
* The incident was solved by fixing bugs in the system.

Preventative measures:
* HTTPS has been improved for security to enable all GET requests from users.
* Always keep your Apache HTTP server up to date.
* Double check your permissions on ServerRoot directories.
* Protect server files by Default Access, directives might overturn which leads to access of files to non root users.
* Monitor your server by checking your logs regularly.
* Install an application that does server monitoring to check how server’s current situation and future trends.


## Author
* **Joan Cruz** - [joancruzz](https://github.com/joancruzz)
