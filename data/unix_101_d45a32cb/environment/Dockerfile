FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e "apple\nbanana\ncherry\ndate" > /home/user/list1.txt
RUN echo -e "banana\ncherry\nfig\ngrape" > /home/user/list2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

