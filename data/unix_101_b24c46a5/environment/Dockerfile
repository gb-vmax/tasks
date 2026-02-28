FROM unix101-base:latest

USER root
RUN echo -e '#!/bin/bash\ntrap ":" TERM\nsleep 100' > /home/user/ignore_term.sh
RUN chmod +x /home/user/ignore_term.sh
RUN echo start > /home/user/marker.txt
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

