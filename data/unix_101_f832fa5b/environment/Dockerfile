FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/input /home/user/output
RUN echo -e 'math physics\nphysics chemistry\nenglish math\nchemistry biology' > /home/user/input/partial_order.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

