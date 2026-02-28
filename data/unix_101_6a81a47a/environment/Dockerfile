FROM unix101-base:latest

USER root
RUN printf "apple\nbanana\ncherry\ndate\nfig\ngrape\nkiwi\n" > /home/user/fruits.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

