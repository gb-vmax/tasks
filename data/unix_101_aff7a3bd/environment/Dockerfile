FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/bin
RUN mkdir -p /usr/local/bin
RUN printf '#!/bin/bash\necho custom\n' > /home/user/bin/mycmd
RUN chmod +x /home/user/bin/mycmd
RUN printf '#!/bin/bash\necho custom2\n' > /usr/local/bin/mycmd
RUN chmod +x /usr/local/bin/mycmd
RUN echo 'export PATH=/home/user/bin:/usr/local/bin:$PATH' >> /home/user/.bashrc
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

