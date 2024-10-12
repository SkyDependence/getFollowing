import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom

def get_user_id(username):
    """
    获取指定用户名的用户ID。
    """
    url = f"https://api.iwara.tv/profile/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None
    
    try:
        data = response.json()
    except ValueError:
        print("无法解析 JSON 响应。")
        return None
    
    if 'user' in data and data['user'] and 'id' in data['user']:
        return data['user']['id']
    else:
        print("未找到用户信息。")
        return None

def get_following_usernames(user_id):
    """
    获取指定用户ID的关注列表中的所有用户名，处理分页。
    """
    usernames = []
    page = 0
    limit = 36  # 根据API响应的limit值设置
    
    while True:
        url = f"https://api.iwara.tv/user/{user_id}/following?page={page}&limit={limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"请求失败: {e}")
            break
        
        try:
            data = response.json()
        except ValueError:
            print("无法解析 JSON 响应。")
            break
        
        # 验证响应结构
        if 'results' not in data or not isinstance(data['results'], list):
            print("无法解析关注列表。")
            break
        
        results = data['results']
        
        # 如果当前页没有数据，退出循环
        if not results:
            break
        
        # 提取用户名，确保username不是None或空字符串
        for item in results:
            user = item.get('user')
            if user and 'username' in user and user['username']:
                usernames.append(user['username'])
            else:
                print(f"跳过无效的用户数据: {user}")
        
        # 计算总页数
        count = data.get('count', 0)
        limit = data.get('limit', 36)
        total_pages = (count + limit - 1) // limit  # 向上取整
        
        # 检查是否已经是最后一页
        if page + 1 >= total_pages:
            break
        
        # 进入下一页
        page += 1
    
    return usernames

def save_usernames_to_file(usernames, filename="following_usernames.txt"):
    """
    将用户名列表保存到指定的文件中。
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for uname in usernames:
                f.write(f"{uname}\n")
        print(f"\n关注列表已保存到 '{filename}'")
    except Exception as e:
        print(f"保存文件时出错: {e}")

def generate_opml(usernames, username, filename=None):
    """
    生成 OPML 文件，包含所有关注用户的 RSS 订阅链接。
    """
    if not filename:
        filename = f"{username}_following.opml"
    
    # 创建 OPML 根元素
    opml = ET.Element('opml', version='1.0')
    
    # 创建 head 元素
    head = ET.SubElement(opml, 'head')
    title = ET.SubElement(head, 'title')
    title.text = f"{username} 的iwara关注列表 RSS 订阅"
    
    # 创建 body 元素
    body = ET.SubElement(opml, 'body')
    
    # 创建一个大纲元素作为根
    main_outline = ET.SubElement(body, 'outline', text=f"{username} 的iwara关注列表", title=f"{username} 的iwara关注列表")
    
    # 假设每个用户的 RSS Feed URL 结构
    rss_url_template = "https://rsshub.app/iwara/users/{}"  # 请根据实际情况调整
    
    for uname in usernames:
        if not uname:
            print("跳过空的用户名。")
            continue
        rss_url = rss_url_template.format(uname)
        if not rss_url:
            print(f"无效的 RSS URL 对于用户名: {uname}")
            continue
        # 使用 ET.SubElement 自动处理特殊字符
        ET.SubElement(main_outline, 'outline', 
                      text=uname, 
                      title=uname, 
                      type="rss", 
                      xmlUrl=rss_url)
    
    # 将 ElementTree 转换为字符串
    try:
        rough_string = ET.tostring(opml, 'utf-8')
    except Exception as e:
        print(f"序列化 XML 时出错: {e}")
        return
    
    # 使用 minidom 进行美化和格式化
    try:
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ", encoding='utf-8')
    except Exception as e:
        print(f"格式化 XML 时出错: {e}")
        return
    
    try:
        with open(filename, "wb") as f:
            f.write(pretty_xml)
        print(f"OPML 文件已生成并保存为 '{filename}'")
    except Exception as e:
        print(f"生成 OPML 文件时出错: {e}")

def main():
    username = input("请输入要查询的用户名：").strip()
    
    if not username:
        print("用户名不能为空。")
        return
    
    user_id = get_user_id(username)
    
    if not user_id:
        print("无法获取用户ID。")
        return
    
    print(f"用户ID: {user_id}")
    
    print("正在获取关注列表，请稍候...")
    following_usernames = get_following_usernames(user_id)
    
    if following_usernames:
        print(f"\n{username} 的关注列表中的用户名如下：")
        for idx, uname in enumerate(following_usernames, start=1):
            print(f"{idx}. {uname}")
        
        # 选择是否保存到文件
        save_choice = input("\n是否将关注列表保存到文本文件？（y/n）：").strip().lower()
        if save_choice == 'y':
            save_usernames_to_file(following_usernames)
        
        # 选择是否生成 OPML 文件
        opml_choice = input("是否生成 OPML 文件以导入 RSS 订阅？（y/n）：").strip().lower()
        if opml_choice == 'y':
            generate_opml(following_usernames, username)
    else:
        print(f"{username} 没有关注任何用户，或无法获取关注列表。")

if __name__ == "__main__":
    main()
