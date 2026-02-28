FROM unix101-base:latest

USER root
RUN echo -e 'Hello world\nThis is the original file.\nGoodbye.' > /home/user/original.txt
RUN cat > /home/user/update.patch <<EOF
--- original.txt	2024-01-01 12:00:00.000000000 +0000
+++ original.txt	2024-01-01 12:00:00.000000000 +0000
@@ -1,3 +1,3 @@
 Hello world
-This is the original file.
+This is the UPDATED file.
 Goodbye.
EOF
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

