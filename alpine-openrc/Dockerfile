FROM alpine:3
RUN apk add --no-cache openrc
RUN sed -i 's/#rc_sys=""/rc_sys="docker"/g' /etc/rc.conf; \
    sed -i 's/^#\(rc_logger="YES"\)$/\1/' /etc/rc.conf; \
    sed -i 's/#rc_env_allow=".*"/rc_env_allow="\*"/g' /etc/rc.conf; \
    sed -i '/tty/d' /etc/inittab; \
    sed -i 's/hostname $opts/# hostname $opts/g' /etc/init.d/hostname; \
    sed -i 's/! mount -t tmpfs/mount -t tmpfs/g' /lib/rc/sh/init.sh; \
    sed -i 's/cgroup_add_service /# cgroup_add_service /g' /lib/rc/sh/openrc-run.sh; \
    sed -i 's/VSERVER/DOCKER/Ig' /lib/rc/sh/init.sh; \
    echo 'rc_provide="loopback net"' >> /etc/rc.conf; \
    rm -f /etc/init.d/hwdrivers /etc/init.d/hwclock /etc/init.d/hwdrivers /etc/init.d/modules /etc/init.d/modules-load /etc/init.d/modloop /etc/init.d/machine-id
ENTRYPOINT ["/sbin/init"]
