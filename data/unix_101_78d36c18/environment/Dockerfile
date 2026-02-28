FROM unix101-base:latest

USER root
RUN printf "1 Alice\n2 Bob\n3 Carol\n4 David\n" > /home/user/list1.txt
RUN printf "2 Engineer\n3 Doctor\n4 Artist\n5 Chef\n" > /home/user/list2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

