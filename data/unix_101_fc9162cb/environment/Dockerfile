FROM unix101-base:latest

USER root
RUN echo 'apple' > /home/user/data1.txt
RUN echo 'banana' >> /home/user/data1.txt
RUN echo 'cherry' >> /home/user/data1.txt
RUN xz /home/user/data1.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

