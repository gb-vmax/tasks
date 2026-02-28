FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/website/.git/hooks
RUN mkdir -p /home/user/website/assets/images
RUN touch /home/user/website/index.html
RUN touch /home/user/website/.env
RUN touch /home/user/website/.git/config
RUN touch /home/user/website/.git/hooks/pre-commit
RUN touch /home/user/website/assets/logo.png
RUN touch /home/user/website/assets/images/banner.jpg
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

