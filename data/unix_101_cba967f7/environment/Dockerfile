FROM unix101-base:latest

USER root
RUN printf "apple\nbanana\ncherry\n" > /home/user/base.txt
RUN printf "apple\nbanana\ndate\n" > /home/user/branch1.txt
RUN printf "apple\nblueberry\ncherry\n" > /home/user/branch2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

