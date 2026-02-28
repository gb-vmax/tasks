FROM unix101-base:latest

USER root
RUN printf '#!/bin/bash\necho "$1" > /home/user/arg_output.txt\n' > /home/user/writearg.sh
RUN chmod +x /home/user/writearg.sh
RUN rm -f /home/user/arg_output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

