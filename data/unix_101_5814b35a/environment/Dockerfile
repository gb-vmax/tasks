FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/tasks
RUN echo -e '#!/bin/bash\necho Hello > /home/user/tasks/output.txt' > /home/user/tasks/print_hello.sh
RUN chmod +x /home/user/tasks/print_hello.sh
RUN rm -f /home/user/tasks/output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

