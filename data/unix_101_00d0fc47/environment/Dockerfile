FROM unix101-base:latest

USER root
RUN printf 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi.\nVestibulum ante ipsum primis in faucibus orci luctus et ultrices.\n' > /home/user/article.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

