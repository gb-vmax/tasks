FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/settings
RUN echo -e "set debug=true\nset timeout=30\nset verbose=false" > /home/user/settings/config.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

