FROM unix101-base:latest

USER root
RUN echo '#!/bin/bash' > /home/user/task1_script.sh
RUN echo 'echo Task1 done' >> /home/user/task1_script.sh
RUN chmod +x /home/user/task1_script.sh
RUN rm -f /home/user/nohup.out
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

