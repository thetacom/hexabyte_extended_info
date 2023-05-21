# Hexabyte Extended Info Plugin

[![Version](https://img.shields.io/pypi/v/hexabyte-extended-info.svg)](https://pypi.python.org/pypi/hexabyte-extended-info)
[![Status](https://img.shields.io/pypi/status/hexabyte-extended-info)](https://pypi.python.org/pypi/hexabyte-extended-info)
[![Wheel](https://img.shields.io/pypi/wheel/hexabyte-extended-info)](https://pypi.org/project/hexabyte-extended-info/)
[![Downloads](https://img.shields.io/pypi/dm/hexabyte-extended-info)](https://pypi.python.org/pypi/hexabyte-extended-info)
[![License](https://img.shields.io/pypi/l/hexabyte-extended-info.svg)](https://pypi.python.org/pypi/hexabyte-extended-info)
[![Python Implementation](https://img.shields.io/pypi/implementation/hexabyte-extended-info)](https://pypi.org/project/hexabyte-extended-info/)
[![Python Version](https://img.shields.io/pypi/pyversions/hexabyte-extended-info)](https://pypi.org/project/hexabyte-extended-info/)

[![Lint](https://github.com/thetacom/hexabyte-extended-info/actions/workflows/lint.yml/badge.svg)](https://github.com/thetacom/hexabyte-extended-info/actions/)
[![Test](https://github.com/thetacom/hexabyte-extended-info/actions/workflows/test.yml/badge.svg)](https://github.com/thetacom/hexabyte-extended-info/actions/)
[![Release](https://github.com/thetacom/hexabyte-extended-info/actions/workflows/release.yml/badge.svg)](https://github.com/thetacom/hexabyte-extended-info/actions/)
[![Publish](https://github.com/thetacom/hexabyte-extended-info/actions/workflows/publish.yml/badge.svg)](https://github.com/thetacom/hexabyte-extended-info/actions/)

[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

A hexabyte plugin for displaying additional file info.

## User

### Install

```bash
~/$ pip install hexabyte-extended-info
...
```

Add `hexabyte-extended-info` to the plugins list inside your hexabyte config (`~/.config/hexabyte/config.toml`).

```toml
plugins = [ "hexabyte-extended-info",]
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
~/$ git clone https://github.com/thetacom/hexabyte-extended-info
...
~/$ cd hexabyte
hexabyte-extended-info/$ poetry install
...
```

### Test

```bash
hexabyte-extended-info/$ make test
...
```
