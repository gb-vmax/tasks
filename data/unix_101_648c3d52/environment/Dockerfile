FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/results
RUN echo '#!/bin/bash' > /home/user/task2_long.sh
RUN echo 'echo Processing' >> /home/user/task2_long.sh
RUN echo 'sleep 1' >> /home/user/task2_long.sh
RUN echo 'echo Completed' >> /home/user/task2_long.sh
RUN chmod +x /home/user/task2_long.sh
RUN rm -f /home/user/results/task2.out
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

