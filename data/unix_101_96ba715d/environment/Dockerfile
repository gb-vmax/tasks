FROM unix101-base:latest

USER root
RUN mkdir -p /home/user
RUN if ! id -u nobody >/dev/null 2>&1; then useradd -r nobody; fi
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

