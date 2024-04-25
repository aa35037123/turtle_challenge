FROM debian:bullseye

# Create the user first before changing ownership
# and put user in sudo group to allow administrative operations.
RUN useradd -ms /bin/bash user && \     
    usermod -aG sudo user 
    echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user

WORKDIR /home/challenger
COPY src .
RUN chown -R user:user /home/challenger && \
    apt-get update && \
    apt-get install -y python3 \
                    python3-pip \
                    python3-tk \
                    sudo \
                    vim

USER user

CMD ["/bin/bash"]