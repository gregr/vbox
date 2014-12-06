These scripts perform basic VirtualBox manipulations.

For more information about scripting VirtualBox, see the [manual](https://www.virtualbox.org/manual/), particularly [chapter 8](https://www.virtualbox.org/manual/ch08.html).

Example Usage
-------------

Globally name your VM for convenience.

    > export vm_name=ubuntu1404

Optionally, you can instead run subsequent commands with this form:

    > vm_name=ubuntu1404 ./command [arg ...]

Create the VM and install Ubuntu 14.04:

    > ./create
    > ./install-ubuntu <path-to-ubuntu-14.04-iso>

Once installation is finished and you're ready to reboot off the hard disk:

    > ./dvd-detach

When you want to stop:

    > ./stop-shutdown  # or ./stop-save to retain the present VM state

To start up again with the GUI:

    > ./start-gui

Or maybe set up a forwarding rule for ssh and start without the GUI:

    > ./net-nat-forward ssh 2345 22  # this forwards localhost:2345 to guest port 22
    > ./start-headless
    > ssh username@localhost -p 2345
