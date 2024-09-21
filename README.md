
**新增获取pixiv关注的用户的id并生成opml文件，可导入rss阅读器**


# Iwara 关注用户用户名抓取工具(建议搭配rsshub使用)


这是一个使用 Python 和 Playwright 的项目，用于抓取你在 [Iwara](https://www.iwara.tv) 网站上关注的用户的用户名。该项目会自动登录你的 Iwara 账号，导航到关注列表页面，并提取你关注的所有用户的用户名。并且生成一份opml文件，可以帮助你快速导入到任何rss阅读器。

## 功能

- 自动登录到 Iwara 网站，使用你的账号凭证。
- 抓取你关注的用户的用户名。
- 将抓取到的用户名保存到文本文件 (followed_usernames.txt)。
- 处理动态加载内容（例如无限滚动）。

## 环境要求

- Python 3.x
- Playwright
- dotenv

## 安装步骤

1. 克隆此仓库到本地：
   ```bash
   git clone https://github.com/SkyDependence/getIwara.git
   ```

2. 进入项目目录：
   ```bash
   cd getIwara
   ```

3. 安装所需的依赖库：
   ```bash
   pip install playwright python-dotenv
   ```

4. 安装 Playwright 浏览器二进制文件：
   ```bash
   python -m playwright install
   ```

## 配置

### 使用环境变量

1. 在项目根目录创建 .env 文件：

2. 在 .env 文件中添加你的 Iwara 凭证：
   ```bash
   IWARA_USERNAME=你的用户名
   IWARA_PASSWORD=你的密码
   ```

如果没有设置隐私关注，那么，只需要设置IWARA_TARGET_USERNAME
```
IWARA_TARGET_USERNAME=你的用户名
```
同样，可以抓取其他用户的关注

### 手动设置环境变量

你也可以直接在终端中手动设置环境变量(不推荐)

**Linux/Mac**:
```bash
export IWARA_USERNAME='你的用户名'
export IWARA_PASSWORD='你的密码'
export IWARA_TARGET_USERNAME='你的用户名'
```
**Windows (PowerShell)**:
```bash
$env:IWARA_USERNAME="你的用户名"
$env:IWARA_PASSWORD="你的密码"
$env:IWARA_TARGET_USERNAME="你的用户名"
```

## 使用方法
使用了账号密码登入的情况下运行抓取脚本：
```bash
python getusername.py
```
不使用账号密码，只使用用户名：
```bash
python getTargetUser.py
```

脚本将会执行以下操作：

- 使用环境变量中存储的用户名和密码登录到你的 Iwara 账号。（非必须）
- 抓取你关注的用户的用户名。
- 将用户名保存到 followed_usernames.txt 文件中。
- 生成一份opml文件，能够导入到rss阅读器
脚本运行结束后，会在终端输出抓取到的用户总数。

## 输出示例
抓取结果保存在 followed_usernames.txt 文件中，示例格式如下：
```python
user12345
user67890
user11223
...
```

生成的opml文件示例如下(以ttrss的格式为例)：
```
<?xml version="1.0" ?>
<opml version="1.0">
  <head>
    <dateCreated>Sat, 21 Sep 2024 06:27:04 +0000</dateCreated>
    <title>Iwara Following Users OPML Export</title>
  </head>
  <body>
    <outline text="Iwara 关注用户" ttrssSortOrder="0">
      <outline type="rss" text="user218714" xmlUrl="https://rsshub.app/iwara/users/user218714" ttrssSortOrder="0" ttrssPurgeInterval="0" ttrssUpdateInterval="0" htmlUrl="https://www.iwara.tv/users/user218714"/>
    </outline>
  </body>
</opml>
```


# Pixiv 关注用户用户名抓取(建议搭配rsshub使用)

## 环境要求

- Python 3.x
- pixivpy3
- dotenv

## 安装步骤

如iwara目录所示

之后，使用pip安装必要的环境和依赖：
```bash
pip install pixivpy3 python-dotenv
```

## 配置

### 使用环境变量

1. 在项目根目录创建 .env 文件：

2. 在 .env 文件中添加你的 pixiv refresh token：
```
PIXIV_REFRESH_TOKEN=你的pixiv refresh token
```

## 使用方法
运行脚本getPixivFollowing.py
```bash
pythong getPixivFollowing.py
```

接着你就能在根目录下找到pixiv_following.opml和pixiv_following.txt这两个文件生成了

## 许可
该项目使用 MIT 许可证 - 请参阅 LICENSE 文件以获取更多信息。

## 贡献
欢迎任何形式的贡献！如果你有任何建议或发现问题，请在 GitHub 仓库中提出 pull request 或 issue。

**免责声明：请负责任地使用此抓取工具，确保遵守 Iwara 的 服务条款。未经授权的抓取行为可能违反其政策，导致账户被封禁或法律行动。**