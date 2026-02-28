FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN touch "/home/user/data/important.txt"
RUN touch "/home/user/data/file one.txt"
RUN touch "/home/user/data/file two.txt"
RUN touch "/home/user/data/keep.txt"
RUN printf '/home/user/data/file one.txt\0/home/user/data/file two.txt\0' > /home/user/delete_list.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

