FROM unix101-base:latest

USER root
RUN echo '[{"id":2,"value":"B"},{"id":3,"value":"C"}]' > /home/user/data1.json
RUN echo '[{"id":1,"value":"A"}]' > /home/user/data2.json
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

