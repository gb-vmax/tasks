FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/source/config
RUN echo 'main.py content' > /home/user/source/main.py
RUN echo 'config.yaml' > /home/user/source/config/settings.yaml
RUN cd /home/user && zip -r project.zip source/
RUN rm -rf /home/user/source
RUN rm -rf /home/user/output_dir
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

