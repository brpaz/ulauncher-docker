# ulauncher-docker

> Manage your Docker containers from Ulauncher

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-docker)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-docker/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-docker/workflows)
![License](https://img.shields.io/github/license/brpaz/ulauncher-docker.svg?style=for-the-badge)

## Demo

![Demo](demo.gif)

## Features

- Lists all running Docker containers
- Display container name, image, ip and exposed ports.
- Allow executing common actions on containers like tailing logs, open a shell, start, stop and restart.
- And more

## Requirements

- Ulauncher 5
- Python >= 3
- Docker daemon running on your machine

This extension also needs [docker-py](https://github.com/docker/docker-py).

To install it, after installing the extension, run the following command on your terminal:

```bash
cd ~/.local/share/ulauncher/extensions/com.github.brpaz.ulauncher-docker
pip3 install -r requirementx.txt
```

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-docker
```

## Usage

On Ulauncher, type `Docker` to see the available commands:

![Extension Commands](./assets/screenshots/extension_demo.png)

## Development

```
git clone https://github.com/brpaz/ulauncher-docker
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `ulauncher -v`.

## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


## License

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
