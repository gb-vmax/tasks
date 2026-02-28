FROM unix101-base:latest

USER root
RUN echo -e '#!/bin/bash' > /home/user/print_error.sh
RUN echo 'echo line1 1>&2' >> /home/user/print_error.sh
RUN echo 'echo line2 1>&2' >> /home/user/print_error.sh
RUN echo 'echo line3 1>&2' >> /home/user/print_error.sh
RUN chmod +x /home/user/print_error.sh
RUN rm -f /home/user/error.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

