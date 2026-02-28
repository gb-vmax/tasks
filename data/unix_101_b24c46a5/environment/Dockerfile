FROM unix101-base:latest

USER root
RUN echo '#!/bin/bash' > /home/user/ignore_term.sh
RUN echo 'trap "" TERM' >> /home/user/ignore_term.sh
RUN echo 'sleep 10' >> /home/user/ignore_term.sh
RUN echo 'echo finished > /home/user/kill_check.txt' >> /home/user/ignore_term.sh
RUN chmod +x /home/user/ignore_term.sh
RUN rm -f /home/user/kill_check.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

