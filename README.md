# Hexabyte Extended Info Plugin

[![Version](https://img.shields.io/pypi/v/hexabyte_extended_info.svg)](https://pypi.python.org/pypi/hexabyte_extended_info)
[![Status](https://img.shields.io/pypi/status/hexabyte_extended_info)](https://pypi.python.org/pypi/hexabyte_extended_info)
[![Wheel](https://img.shields.io/pypi/wheel/hexabyte_extended_info)](https://pypi.org/project/hexabyte_extended_info/)
[![Downloads](https://img.shields.io/pypi/dm/hexabyte_extended_info)](https://pypi.python.org/pypi/hexabyte_extended_info)
[![License](https://img.shields.io/pypi/l/hexabyte_extended_info.svg)](https://pypi.python.org/pypi/hexabyte_extended_info)
[![Python Implementation](https://img.shields.io/pypi/implementation/hexabyte_extended_info)](https://pypi.org/project/hexabyte_extended_info/)
[![Python Version](https://img.shields.io/pypi/pyversions/hexabyte_extended_info)](https://pypi.org/project/hexabyte_extended_info/)

[![Lint](https://github.com/thetacom/hexabyte_extended_info/actions/workflows/lint.yml/badge.svg)](https://github.com/thetacom/hexabyte_extended_info/actions/)
[![Test](https://github.com/thetacom/hexabyte_extended_info/actions/workflows/test.yml/badge.svg)](https://github.com/thetacom/hexabyte_extended_info/actions/)
[![Release](https://github.com/thetacom/hexabyte_extended_info/actions/workflows/release.yml/badge.svg)](https://github.com/thetacom/hexabyte_extended_info/actions/)
[![Publish](https://github.com/thetacom/hexabyte_extended_info/actions/workflows/publish.yml/badge.svg)](https://github.com/thetacom/hexabyte_extended_info/actions/)

[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

A hexabyte plugin for displaying additional file info.

This plugin uses the [python-magic](https://github.com/ahupp/python-magic) package to provide robust file type details when possible.

## User

### Install

```bash
~/$ pip install hexabyte-extended-info
...
```

Add `hexabyte_extended_info` to the plugins list inside your hexabyte config (`~/.config/hexabyte/config.toml`).

```toml
plugins = [ "hexabyte_extended_info",]
```

## x86_64 Hello World

Standard Info Panel

![Hello World Standard](imgs/hello_world_standard.png)

Extended Info Panel

![Hello World Extended](imgs/hello_world_extended.png)

## MacOS Bash

Standard Info Panel

![MacOS Bash Standard](imgs/bash_standard.png)

Extended Info Panel

![MacOS Bash Extended](imgs/bash_extended.png)

## Developer

```bash
~/$ git clone https://github.com/thetacom/hexabyte_extended_info
...
~/$ cd hexabyte
hexabyte_extended_info/$ poetry install
...
```

### Test

```bash
hexabyte_extended_info/$ make test
...
```
