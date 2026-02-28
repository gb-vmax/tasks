FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN printf '#!/bin/bash\nsleep 60\n' > /home/user/holdopen.sh
RUN chmod +x /home/user/holdopen.sh
RUN bash -c 'setsid /home/user/holdopen.sh &'
RUN sleep 2
RUN pgrep -f /home/user/holdopen.sh | head -n1 > /home/user/run_pid.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

