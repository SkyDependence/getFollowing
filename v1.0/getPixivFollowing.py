# getPixivFollowing.py

from xml.dom import minidom
import datetime
import os
import time
from pixivpy3 import AppPixivAPI
from dotenv import load_dotenv
import xml.etree.ElementTree as ET

def main():
    # 加载 .env 文件中的环境变量
    load_dotenv()

    # 从环境变量中读取 refresh token
    REFRESH_TOKEN = os.getenv('PIXIV_REFRESH_TOKEN')

    if not REFRESH_TOKEN:
        print("请在 .env 文件中设置 PIXIV_REFRESH_TOKEN。")
        return

    # 初始化 Pixiv API 客户端
    api = AppPixivAPI()

    # 使用 refresh_token 获取 access_token 并登录
    try:
        api.auth(refresh_token=REFRESH_TOKEN)
        print("成功登录 Pixiv。")
    except Exception as e:
        print(f"登录失败: {e}")
        return

    # 获取当前登录用户信息
    try:
        user_pid = api.user_id
        print(f"当前用户 PID: {user_pid}")
    except AttributeError:
        print("'AppPixivAPI' 对象没有 'me' 方法。请确认 PixivPy3 是否正确安装。")
        return
    except Exception as e:
        print(f"获取用户信息失败: {e}")
        return

    # 获取关注列表
    all_pid_name_pairs = []  # 保存 (pid, name) 对
    offset = 0
    limit = 30  # PixivPy3 默认每页30条

    print("开始获取关注的画师列表...")

    while True:
        try:
            # 获取关注列表
            json_result = api.user_following(user_pid, restrict='public', offset=offset)
            # 打印完整的响应数据用于调试
            print(f"API 响应数据: {json_result}")

            # 检查 'user_previews' 键是否存在于返回的数据中
            if 'user_previews' not in json_result or not json_result['user_previews']:
                print("没有更多的关注用户。")
                break

            users = json_result['user_previews']
            if not users:
                print("没有更多的关注用户。")
                break

            # 打印第一个用户数据用于调试
            first_user = users[0]['user']
            print(f"第一个用户数据: 用户名: {first_user['name']}, PID: {first_user['id']}")

            # 提取 pid 和用户名
            pid_name_pairs = [(user_preview['user']['id'], user_preview['user']['name']) for user_preview in users]
            all_pid_name_pairs.extend(pid_name_pairs)

            print(f"已获取 {len(pid_name_pairs)} 个 pid，当前总数: {len(all_pid_name_pairs)}")

            if len(users) < limit:
                # 已经到达最后一页
                break

            offset += limit

            # 暂停1秒，避免过于频繁的请求
            time.sleep(1)

        except AttributeError as e:
            print(f"方法调用失败: {e}")
            break
        except TypeError as e:
            print(f"方法参数错误: {e}")
            break
        except Exception as e:
            print(f"请求关注列表失败: {e}")
            break

    # 去重
    unique_pid_name_pairs = list(set(all_pid_name_pairs))
    print(f"总共获取到 {len(unique_pid_name_pairs)} 个唯一的 pid。")

    # 输出 PID 列表
    if unique_pid_name_pairs:
        print("\n关注列表的 PID:")
        for pid, name in unique_pid_name_pairs:
            print(f"{pid} - {name}")
    else:
        print("未获取到任何关注的 pid。")

    # 保存 UID 到文件
    with open('pixiv_following.txt', 'w', encoding='utf-8') as f:
        for pid, _ in unique_pid_name_pairs:
            f.write(f"{pid}\n")
    print("已将所有 UID 保存到 pixiv_following.txt 文件中。")

    # 生成 OPML 文件
    # 创建 OPML 根元素
    opml = ET.Element('opml', version='1.0')
    head = ET.SubElement(opml, 'head')
    body = ET.SubElement(opml, 'body')

    # 添加头部信息
    date_created = ET.SubElement(head, 'dateCreated')
    date_created.text = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')
    title = ET.SubElement(head, 'title')
    title.text = 'Pixiv Followings Feed Export'

    # 创建一个分类，例如 "Pixiv Followings"
    outline_pixiv = ET.SubElement(body, 'outline', text='Pixiv Followings', ttrssSortOrder='0')

    # 为每个 UID 添加一个订阅源
    for pid, user_name in unique_pid_name_pairs:
        # 构造 RSS 订阅链接，这里假设使用 rsshub.app 的 Pixiv 用户订阅
        rss_url = f'https://rsshub.app/pixiv/user/{pid}'
        html_url = f'https://www.pixiv.net/users/{pid}'
        ET.SubElement(
            outline_pixiv,
            'outline',
            type='rss',
            text=f"{user_name} 的 pixiv 动态",
            xmlUrl=rss_url,
            ttrssSortOrder='0',
            ttrssPurgeInterval='0',
            ttrssUpdateInterval='0',
            htmlUrl=html_url
        )

   

    # 使用 minidom 进行美化
    rough_string = ET.tostring(opml, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    # 保存 OPML 文件
    with open('pixiv_following.opml', 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    print("已生成 OPML 文件：pixiv_following.opml")

if __name__ == "__main__":
    main()
