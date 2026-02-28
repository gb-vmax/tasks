FROM unix101-base:latest

USER root
RUN echo -e '#!/bin/bash\nsleep 10\necho finished > /home/user/result.txt' > /home/user/slow_script.sh
RUN chmod +x /home/user/slow_script.sh
RUN rm -f /home/user/result.txt
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

