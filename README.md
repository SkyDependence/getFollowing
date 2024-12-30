# Social Media Following to OPML

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/SkyDependence/getFollowing)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/SkyDependence/getFollowing)](https://github.com/SkyDependence/getFollowing/issues)
[![GitHub stars](https://img.shields.io/github/stars/SkyDependence/getFollowing)](https://github.com/SkyDependence/getFollowing/stargazers)

A Python tool to export your following list from Iwara and Pixiv to OPML format, which can be imported into RSS readers. The RSS feeds are powered by [RSSHub](https://rsshub.app).

[中文文档](#社交媒体关注列表转opml)

## Features

- Export Iwara following list to OPML format
- Export Pixiv following list to OPML format
- Compatible with any RSS reader that supports OPML import
- Powered by RSSHub for feed generation

## Installation

### Prerequisites

- Python 3.8 or higher
- Git (optional but recommended)

### Recommended: Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: If you don't have a requirements.txt file, you can install the packages individually:
> ```bash
> pip install requests pixivpy3
> ```

## Usage

### Iwara Following Export

```bash
python iwaraFollowing.py
```

The script will:
1. Prompt for your Iwara credentials
2. Fetch your following list
3. Generate `iwara_following.opml` file

### Pixiv Following Export

```bash
python pixivFollowing.py
```

The script will:
1. Prompt for your Pixiv refresh token
2. Fetch your following list
3. Generate `pixiv_following.opml` file

> For instructions on obtaining your Pixiv refresh token, please refer to [this guide](https://www.nanoka.top/posts/e78ef86/)

### Example Output

After running the scripts, you'll get OPML files that can be imported into your RSS reader. Here's an example structure:

```xml
<opml version="1.0">
  <head>
    <title>Iwara Following</title>
  </head>
  <body>
    <outline text="User1" 
             title="User1"
             type="rss"
             xmlUrl="https://rsshub.app/iwara/users/User1/videos"/>
  </body>
</opml>
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeatureName`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeatureName`)
5. Create a new Pull Request

Please make sure to follow our [code of conduct](CODE_OF_CONDUCT.md).

## FAQ

### Q: Why do I need a Pixiv refresh token?
A: Pixiv's API requires OAuth2 authentication, and the refresh token is used to obtain access tokens securely.

### Q: Can I use this with other RSS readers?
A: Yes, any RSS reader that supports OPML import should work.

### Q: How often should I update my OPML file?
A: We recommend updating it whenever you follow/unfollow users to keep your RSS feeds up-to-date.

## Legacy Version

For the previous version's instructions, please refer to the [v1.0 README](./v1.0/README.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

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

- Python 3.8 或更高版本
- Git（可选但推荐）

### 推荐：创建虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows 系统：
venv\Scripts\activate
# macOS/Linux 系统：
source venv/bin/activate
```

### 安装依赖

```bash
pip install -r requirements.txt
```

> 注意：如果没有 requirements.txt 文件，可以单独安装所需包：
> ```bash
> pip install requests pixivpy3
> ```

## 使用方法

### Iwara 关注导出

```bash
python iwaraFollowing.py
```

脚本将会：
1. 提示输入 Iwara 账号信息
2. 获取关注列表
3. 生成 `iwara_following.opml` 文件

### Pixiv 关注导出

```bash
python pixivFollowing.py
```

脚本将会：
1. 提示输入 Pixiv refresh token
2. 获取关注列表
3. 生成 `pixiv_following.opml` 文件

> 如何获取 Pixiv refresh token 可以阅读[这篇文章](https://www.nanoka.top/posts/e78ef86/)

### 示例输出

运行脚本后，您将获得可以导入 RSS 阅读器的 OPML 文件。以下是一个示例结构：

```xml
<opml version="1.0">
  <head>
    <title>Iwara 关注列表</title>
  </head>
  <body>
    <outline text="用户1" 
             title="用户1"
             type="rss"
             xmlUrl="https://rsshub.app/iwara/users/用户1/videos"/>
  </body>
</opml>
```

## 贡献指南

欢迎贡献代码！请按照以下步骤进行：

1. Fork 本仓库
2. 创建新分支 (`git checkout -b feature/你的功能名称`)
3. 提交更改 (`git commit -m '添加新功能'`)
4. 推送分支 (`git push origin feature/你的功能名称`)
5. 创建 Pull Request

请确保遵守我们的[行为准则](CODE_OF_CONDUCT.md)。

## 常见问题

### Q: 为什么需要 Pixiv refresh token？
A: Pixiv 的 API 需要 OAuth2 认证，refresh token 用于安全地获取访问令牌。

### Q: 可以与其他 RSS 阅读器一起使用吗？
A: 可以，任何支持 OPML 导入的 RSS 阅读器都可以使用。

### Q: 应该多久更新一次 OPML 文件？
A: 建议在关注/取消关注用户时更新，以保持 RSS 订阅源的最新状态。

## 旧版本

查看旧版本使用方法请参考 [v1.0 说明文档](./v1.0/README.md)。

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。
