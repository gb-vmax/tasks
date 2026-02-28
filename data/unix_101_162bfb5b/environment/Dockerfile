FROM unix101-base:latest

USER root
RUN printf '#!/bin/bash\necho Hello World\n' > /home/user/myscript.sh
RUN chmod 644 /home/user/myscript.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

