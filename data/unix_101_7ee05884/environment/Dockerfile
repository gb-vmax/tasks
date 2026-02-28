FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/test_scripts
RUN mkdir -p /home/user/output
RUN echo -e '#!/bin/bash\nsleep 1' > /home/user/test_scripts/sleep.sh
RUN chmod +x /home/user/test_scripts/sleep.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

