# ulauncher-docker

[![Build Status](https://img.shields.io/travis/com/brpaz/ulauncher-docker.svg)](https://github.com/brpaz/ulauncher-docker)
[![GitHub license](https://img.shields.io/github/license/brpaz/ulauncher-docker.svg)](https://github.com/brpaz/:ulauncher-docker/blob/master/LICENSE)

> Manage your Docker containers from Ulauncher

## Demo

![Demo](demo.gif)

## Features

- Lists all running Docker containers
- Display container name, image, ip and exposed ports.
- Allow executing common actions on containers like tailing logs, open a shell, start, stop and restart.
- And more

## Requirements

- Ulauncher
- Python >= 2.7 with packages:
- Docker daemon running on your machine

This extension also needs [docker-py](https://github.com/docker/docker-py) and [argparse](https://pypi.org/project/argparse) Python packages.

You can install them in one command using: `pip install argparse docker`

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-docker
```

## Usage

On Ulauncher, use "dk" as the default keyword to trigger the extension. By default it will show a list of running containers.

To display all the containers run `dk -a`.

Other commands:

- `dk info` - Show Docker version and provides quick access to Docker Documentation

- `dk utils`- Provides access to common commands like "Docker prune"

- `dk -c <containerid|name>` - Show container details like name, image and network information and allow to execute quick actions like tailing the container logs or start|stop|restart the container.

## Development

```
git clone https://github.com/brpaz/ulauncher-docker
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `ulauncher -v`.

## Contributing

- Fork it!
- Create your feature branch: git checkout -b my-new-feature
- Commit your changes: git commit -am 'Add some feature'
- Push to the branch: git push origin my-new-feature
- Submit a pull request :D

## License

MIT &copy; Bruno Paz
