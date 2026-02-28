FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/test_scripts
RUN echo -e '#!/bin/bash\necho Hello, world!' > /home/user/test_scripts/hello.sh
RUN chmod +x /home/user/test_scripts/hello.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

