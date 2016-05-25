# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure(2) do |config|

  config.vm.box ="ubuntu/trusty64"
  config.vm.network "forwarded_port", guest:8000, host:8000
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/site.yml"
    ansible.groups = {
      "develop" => ["default"]
    }
  end

  config.vm.provider "virtualbox" do |v, override|
    v.memory = 1024
    v.cpus = 2
  end

  config.vm.provider "lxc" do |v, override|
    override.vm.box = "fgrehm/trusty64-lxc"
  end

end
