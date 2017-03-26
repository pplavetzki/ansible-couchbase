required_plugins = %w(vagrant-host-shell vagrant-docker-compose)
required_plugins.each do |plugin|
  system "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure("2") do |config|
  config.vm.define :ubuntu do |ubuntu|
    
    ubuntu.vm.hostname = :ubuntu
    ubuntu.vm.box = 'ubuntu/trusty64'

    ubuntu.vm.provider :virtualbox do |vb|
      vb.gui = false
      vb.cpus = 2
      vb.memory = 2048 # works with 1024, 512 will need a swap file
    end

    #port = 4200

    config.vm.network "private_network", ip: "150.10.0.2"
    #config.vm.network "forwarded_port", guest: port, host: port
    config.vm.provision :docker
    config.vm.provision :docker_compose, yml:'/vagrant/docker-compose.yml', compose_version: "1.8.0"

  end

  config.vm.define :vsrx1 do |vsrx|
    vsrx.vm.hostname = :vsrx1
    vsrx.vm.box = 'juniper/ffp-12.1X47-D15.4-packetmode'
    vsrx.vm.network :private_network, ip: '150.10.0.3'
    vsrx.vm.provider :virtualbox do |vb|
      vb.cpus = 2 # needs 2 to boot?
      vb.memory = 512
      vb.name = 'vsrx'
      vb.customize ['modifyvm', :id, '--uartmode1', 'server', '/tmp/vsrx2_config_serial']

    end
  end

end