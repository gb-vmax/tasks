FROM unix101-base:latest

USER root
RUN echo -e '#!/bin/bash\necho "$1 $2" > /home/user/positional.txt' > /home/user/setpos.sh
RUN chmod +x /home/user/setpos.sh
RUN rm -f /home/user/positional.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

