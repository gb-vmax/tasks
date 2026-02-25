You are working as a container specialist managing Linux-based microservices. Under /home/user/microservices, there is a directory named "orderservice" which contains a file called "start.sh" (the startup script for the orderservice). 

Your task is as follows:

1. Change the permissions of the file /home/user/microservices/orderservice/start.sh so that only the file owner can read, write, and execute the file. No other users or groups should have any permissions for this file.
2. Ensure that the directory /home/user/microservices/orderservice itself is set so only the owner can list its contents, create, or delete files (i.e., full access), and no permissions are granted to group or others.
3. To verify the change, generate a permissions report in the following precise format:

- Create a file named "/home/user/microservices/orderservice/permissions_report.log".
- The file must contain exactly two lines, with no extra spacing or line breaks.
- The first line must be the output of the command: `stat -c "%A %n" /home/user/microservices/orderservice/start.sh`
- The second line must be the output of the command: `stat -c "%A %n" /home/user/microservices/orderservice`

The final state should have the permissions set as described, and the permissions_report.log should exactly match the specified output format.
