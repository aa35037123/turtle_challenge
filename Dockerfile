FROM debian:bullseye

# Create the user first before changing ownership
# and put user in sudo group to allow administrative operations.
RUN useradd -ms /bin/bash challenger && \     
    usermod -aG sudo challenger
    # mkdir -p /etc/sudoers.d && \  # Ensure the directory exists
    # echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user && \
    # chmod 0440 /etc/sudoers.d/user  # Set correct permissions for the file

WORKDIR /home/challenger
COPY src .
RUN chown -R challenger:challenger /home/challenger && \
    chmod +x /home/challenger/save_canvas.sh && \
    apt-get update && \
    apt-get install -y python3 \
                    python3-pip \
                    python3-tk \
                    sudo \
                    vim && \
    pip3 install Pillow

USER challenger

CMD ["/bin/bash"]