# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.6.2"

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/xenial64"
  # config.vm.box = "https://cloud-images.ubuntu.com/vagrant/wily/current/wily-server-cloudimg-amd64-vagrant-disk1.box"

  # config.vm.hostname = "xenb"
  # config.vm.network :private_network, :ip => '10.4.4.4'
  number_of_nodes = 3
  number_of_nodes.times do |i|
    config.vm.define "xenb-#{i}" do |node|
      node.vm.hostname = "xenb-#{i}"
      node.vm.network :private_network, :ip => "10.4.5.#{i}"
      node.vm.provider :virtualbox do |vb|
        #vb.gui = true
        vb.customize ["modifyvm", :id, "--memory", "512"]
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "off"]
        vb.customize ["modifyvm", :id, "--natdnsproxy1", "off"]
        vb.name = "xenb-#{i}"
      end
    end
    i += 1
  end

  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true


end