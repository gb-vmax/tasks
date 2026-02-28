FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf "pear\napple\nbanana\nkiwi\n" > /home/user/unsorted.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

