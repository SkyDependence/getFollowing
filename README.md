# Social Media Following to OPML

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/SkyDependence/getFollowing)](LICENSE)

A Python tool to export your following list from Iwara and Pixiv to OPML format, which can be imported into RSS readers. The RSS feeds are powered by [RSSHub](https://rsshub.app).

[中文文档](#社交媒体关注列表转opml)

## Features

- Export Iwara following list to OPML format
- Export Pixiv following list to OPML format
- Compatible with any RSS reader that supports OPML import
- Powered by RSSHub for feed generation

## Installation

### Prerequisites

- Python 3.x
- Required Python packages:
  ```bash
  # For Iwara
  pip install requests

  # For Pixiv
  pip install pixivpy3
  ```

## Usage

### Iwara Following Export

1. Run the script:
   ```bash
   python iwaraFollowing.py
   ```
2. Follow the prompts to enter your credentials
3. The script will generate an OPML file with your following list

### Pixiv Following Export

1. Run the script:
   ```bash
   python pixivFollowing.py
   ```
2. Enter your Pixiv refresh token when prompted
   > For instructions on obtaining your Pixiv refresh token, please refer to [this guide](https://www.nanoka.top/posts/e78ef86/)

## Legacy Version

For the previous version's instructions, please refer to the [v1.0 README](./v1.0/README.md).

---

# 社交媒体关注列表转OPML

将您在 Iwara 和 Pixiv 的关注列表导出为 OPML 格式，可导入至 RSS 阅读器。订阅源由 [RSSHub](https://rsshub.app) 提供支持。

## 功能特点

- 导出 Iwara 关注列表为 OPML 格式
- 导出 Pixiv 关注列表为 OPML 格式
- 兼容支持 OPML 导入的 RSS 阅读器
- 使用 RSSHub 生成订阅源

## 安装

### 环境要求

- Python 3.x
- 所需 Python 包：
  ```bash
  # Iwara 所需
  pip install requests

  # Pixiv 所需
  pip install pixivpy3
  ```

## 使用方法

### Iwara 关注导出

1. 运行脚本：
   ```bash
   python iwaraFollowing.py
   ```
2. 根据提示输入相关信息
3. 脚本将生成包含您关注列表的 OPML 文件

### Pixiv 关注导出

1. 运行脚本：
   ```bash
   python pixivFollowing.py
   ```
2. 输入您的 Pixiv refresh token
   > 如何获取 Pixiv refresh token 可以阅读[这篇文章](https://www.nanoka.top/posts/e78ef86/)

## 旧版本

查看旧版本使用方法请参考 [v1.0 说明文档](./v1.0/README.md)。
