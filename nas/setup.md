### Mounting Shared Volumes

For mounting shared volumes, access the NAS' Control Panel. Select "Shared Folders", right click the desired shared folder and select "mount", which will be done by using your key (if encrypted).

### SSH

Activate the SSH Server on the control painel

### Virtual Volumes

You can mount the virtual volumes on your own computer, which can be directly accessed.

On MAC, they are available at "/Volumes", normally using the SMB 3.0 protocol, the default Synology protocol, also supported natively by MacOS.

### More speed when using the virtual volumes

For more speed using the VSCode inside the NAS, access is directly using SSH (attached to the NAS' SSH Server), instead of using the standard protocol. It may be needed to enable the TCP Forwarding, so that the NAS Server can provide an extra port for the VSCode to attach to. Beware that it may represent a security risk, for instance, if the NAS is accessible from outside the network.

```
sudo vim /etc/ssh/sshd_config
```

Add line:

```
Match User my_synology_nas
	AllowTcpForwarding yes
```
