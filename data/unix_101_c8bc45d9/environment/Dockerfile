FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN echo -e 'Section 1 content\n---END---\nSection 2 content\n---END---\nSection 3 content' > /home/user/sections.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

