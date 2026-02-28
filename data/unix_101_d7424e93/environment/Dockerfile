FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e '#!/bin/bash\nsleep 300' > /home/user/mywait
RUN chmod +x /home/user/mywait
RUN su user -c 'nohup /home/user/mywait > /home/user/mywait_user1.out 2>&1 &'
RUN su user -c 'nohup /home/user/mywait > /home/user/mywait_user2.out 2>&1 &'
RUN nohup /home/user/mywait > /home/user/mywait_root1.out 2>&1 &
RUN sleep 1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

