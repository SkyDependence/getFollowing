from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 加载 .env 文件
load_dotenv()

# 从环境变量中获取目标用户名
TARGET_USERNAME = os.getenv('IWARA_TARGET_USERNAME')

# 检查是否成功加载环境变量
if not TARGET_USERNAME:
    print("错误：未能加载环境变量中的目标用户名。请确保 .env 文件中设置了 IWARA_TARGET_USERNAME。")
    exit(1)

def generate_opml(usernames, output_file='target_followed_users.opml'):
    """
    根据用户名列表生成 OPML 文件
    """
    opml = ET.Element('opml', version="1.0")
    
    head = ET.SubElement(opml, 'head')
    date_created = ET.SubElement(head, 'dateCreated')
    date_created.text = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    title = ET.SubElement(head, 'title')
    title.text = "Iwara Following Users OPML Export"
    
    body = ET.SubElement(opml, 'body')
    outline_main = ET.SubElement(body, 'outline', text="Iwara 关注用户", ttrssSortOrder="0")
    
    for uname in usernames:
        outline = ET.SubElement(
            outline_main,
            'outline',
            type="rss",
            text=uname,
            xmlUrl=f"https://rsshub.app/iwara/users/{uname}",
            ttrssSortOrder="0",
            ttrssPurgeInterval="0",
            ttrssUpdateInterval="0",
            htmlUrl=f"https://www.iwara.tv/users/{uname}"
        )
    
    # 使用 minidom 进行美化
    rough_string = ET.tostring(opml, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"OPML 文件已生成：{output_file}")

def scrape_iwara_following(target_username):
    with sync_playwright() as p:
        # 启动浏览器（Chromium, Firefox, WebKit）
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # 访问关注列表页面
        following_url = f'https://www.iwara.tv/profile/{target_username}/following'
        page.goto(following_url)

        # 初始化用户名列表
        followed_usernames = []

        # 设置最大页面数以防止死循环
        MAX_PAGES = 100
        current_page = 1

        while current_page <= MAX_PAGES:
            print(f"正在处理第 {current_page} 页...")

            # 等待关注列表加载
            try:
                page.wait_for_selector('div.text.text--truncate.text--muted.text--small', timeout=10000)
            except Exception as e:
                print("关注列表页面未正确加载。")
                browser.close()
                raise e

            # 记录当前用户名数量
            previous_count = len(followed_usernames)

            # 抓取当前页的关注用户名
            user_elements = page.query_selector_all("div.text.text--truncate.text--muted.text--small")

            for elem in user_elements:
                text = elem.inner_text().strip()
                if text.startswith("@"):
                    uname = text[1:].strip()  # 去除 "@"
                    if uname not in followed_usernames:  # 避免重复
                        followed_usernames.append(uname)
                        print(uname)

            # 检查是否有“下一页”按钮
            try:
                # 根据提供的HTML结构，选择包含特定SVG的<li>元素
                next_button_li = page.query_selector("li.pagination__item:has(svg[data-icon='angle-right'])")
                
                if next_button_li:
                    # 在<li>元素中查找可点击的子元素
                    clickable = next_button_li.query_selector("a, button, div.icon")
                    if clickable:
                        clickable.click()
                        print("导航到下一页...")
                        # 等待页面加载完成
                        page.wait_for_load_state('networkidle')
                        time.sleep(2)  # 等待额外时间以确保内容加载
                        current_page += 1
                    else:
                        print("“下一页”按钮不可点击。")
                        break
                else:
                    print("已到最后一页。")
                    break
            except Exception as e:
                print("无法找到下一页按钮或点击失败。")
                break

            # 检查是否有新用户名被添加
            new_count = len(followed_usernames)
            if new_count == previous_count:
                print("没有新用户被添加，可能已到最后一页。")
                break

        print(f"共抓取到 {len(followed_usernames)} 个关注的用户。")

        # 保存用户名到文本文件
        with open('followed_usernames.txt', 'w', encoding='utf-8') as f:
            for uname in followed_usernames:
                f.write(uname + '\n')

        # 生成 OPML 文件
        generate_opml(followed_usernames, output_file='target_followed_users.opml')

        # 关闭浏览器
        browser.close()

if __name__ == "__main__":
    scrape_iwara_following(TARGET_USERNAME)
