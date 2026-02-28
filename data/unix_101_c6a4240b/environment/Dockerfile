FROM unix101-base:latest

USER root
RUN echo '#!/bin/bash' > /home/user/slow_script.sh
RUN echo 'sleep 10' >> /home/user/slow_script.sh
RUN echo 'echo done > /home/user/script_finished.txt' >> /home/user/slow_script.sh
RUN chmod +x /home/user/slow_script.sh
RUN rm -f /home/user/script_finished.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

