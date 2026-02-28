FROM unix101-base:latest

USER root
RUN printf "apple\nbanana\ncarrot\ndate\nkiwi\n" > /home/user/list1.txt
RUN printf "apricot\nbanana\ncarrot\nfig\nkiwi\npear\n" > /home/user/list2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

