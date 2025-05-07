import requests
import json
import os
import subprocess

# GitHub 仓库路径
GITHUB_REPO = "https://github.com/DrestryRobot/icon-storage.git"

# 创建存储图标的目录（确保图标存储在仓库根目录的 `icons/`）
os.makedirs("icons", exist_ok=True)

# 设置请求头，模拟浏览器访问
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# JSON 数据（完整的网站列表）
json_data = [
    {"name": "百度", "domain": "baidu.com", "link": "https://www.baidu.com", "category": "搜索"},
    {"name": "360搜索", "domain": "so.com", "link": "https://www.so.com", "category": "搜索"},
    {"name": "搜狗搜索", "domain": "sogou.com", "link": "https://www.sogou.com", "category": "搜索"},
    {"name": "夸克", "domain": "quark.cn", "link": "https://www.quark.cn", "category": "搜索"},
    {"name": "Bing", "domain": "bing.com", "link": "https://www.bing.com", "category": "搜索"},
    {"name": "Google", "domain": "google.com", "link": "https://www.google.com", "category": "搜索"},
    {"name": "Yandex", "domain": "yandex.com", "link": "https://www.yandex.com", "category": "搜索"},
    
    {"name": "维基百科", "domain": "wikipedia.org", "link": "https://www.wikipedia.org", "category": "百科"},
    {"name": "百度百科", "domain": "baike.baidu.com", "link": "https://baike.baidu.com", "category": "百科"},
    
    {"name": "百度文库", "domain": "wenku.baidu.com", "link": "https://wenku.baidu.com", "category": "文档"},
    {"name": "印象笔记", "domain": "evernote.com", "link": "https://www.yinxiang.com", "category": "文档"},
    {"name": "Notion", "domain": "notion.so", "link": "https://www.notion.com", "category": "文档"},
    
    {"name": "豆瓣", "domain": "douban.com", "link": "https://www.douban.com", "category": "社区"},
    {"name": "简书", "domain": "jianshu.com", "link": "https://www.jianshu.com", "category": "社区"},
    {"name": "CSDN", "domain": "csdn.net", "link": "https://www.csdn.net", "category": "社区"},
    
    {"name": "知乎", "domain": "zhihu.com", "link": "https://www.zhihu.com", "category": "问答"},
    {"name": "百度知道", "domain": "zhidao.baidu.com", "link": "https://zhidao.baidu.com", "category": "问答"},
    
    {"name": "抖音", "domain": "douyin.com", "link": "https://douyin.com", "category": "视频"},
    {"name": "快手", "domain": "kuaishou.com", "link": "https://kuaishou.com", "category": "视频"},
    {"name": "小红书", "domain": "xiaohongshu.com", "link": "https://xiaohongshu.com", "category": "视频"},
    {"name": "爱奇艺", "domain": "iqiyi.com", "link": "https://www.iqiyi.com", "category": "视频"},
    {"name": "优酷", "domain": "youku.com", "link": "https://www.youku.com", "category": "视频"},
    {"name": "腾讯视频", "domain": "v.qq.com", "link": "https://v.qq.com", "category": "视频"},
    {"name": "芒果TV", "domain": "mgtv.com", "link": "https://www.mgtv.com", "category": "视频"},
    {"name": "哔哩哔哩", "domain": "bilibili.com", "link": "https://www.bilibili.com", "category": "视频"},
    {"name": "乐视视频", "domain": "le.com", "link": "https://www.le.com", "category": "视频"},
    
    {"name": "淘宝", "domain": "taobao.com", "link": "https://www.taobao.com", "category": "购物"},
    {"name": "京东", "domain": "jd.com", "link": "https://www.jd.com", "category": "购物"},
    {"name": "拼多多", "domain": "pinduoduo.com", "link": "https://www.pinduoduo.com", "category": "购物"},
    {"name": "苏宁易购", "domain": "suning.com", "link": "https://www.suning.com", "category": "购物"},
    {"name": "天猫", "domain": "tmall.com", "link": "https://www.tmall.com", "category": "购物"},
    
    {"name": "网易云课堂", "domain": "study.163.com", "link": "https://study.163.com", "category": "学习"},
    {"name": "腾讯课堂", "domain": "ke.qq.com", "link": "https://ke.qq.com", "category": "学习"},
    
    {"name": "微博", "domain": "weibo.com", "link": "https://weibo.com", "category": "社交"},
    {"name": "QQ", "domain": "qq.com", "link": "https://www.qq.com", "category": "社交"},
    
    {"name": "今日头条", "domain": "toutiao.com", "link": "https://www.toutiao.com", "category": "新闻"},
    {"name": "网易新闻", "domain": "news.163.com", "link": "https://news.163.com", "category": "新闻"},
    {"name": "腾讯新闻", "domain": "news.qq.com", "link": "https://news.qq.com", "category": "新闻"},
    {"name": "新浪新闻", "domain": "news.sina.com.cn", "link": "https://news.sina.com.cn", "category": "新闻"},
    {"name": "凤凰新闻", "domain": "news.ifeng.com", "link": "https://news.ifeng.com", "category": "新闻"},
    
    {"name": "网易云音乐", "domain": "music.163.com", "link": "https://music.163.com", "category": "音乐"},
    {"name": "QQ音乐", "domain": "y.qq.com", "link": "https://y.qq.com", "category": "音乐"},
    {"name": "酷狗音乐", "domain": "kugou.com", "link": "https://www.kugou.com", "category": "音乐"},
    {"name": "酷我音乐", "domain": "kuwo.cn", "link": "https://www.kuwo.cn", "category": "音乐"},
    {"name": "Spotify", "domain": "spotify.com", "link": "https://www.spotify.com", "category": "音乐"},
    {"name": "Apple Music", "domain": "music.apple.com", "link": "https://music.apple.com", "category": "音乐"},
    
    {"name": "QQ邮箱", "domain": "mail.qq.com", "link": "https://mail.qq.com", "category": "邮箱"},
    {"name": "网易邮箱", "domain": "163.com", "link": "https://mail.163.com", "category": "邮箱"},
    {"name": "Outlook", "domain": "outlook.com", "link": "https://outlook.live.com", "category": "邮箱"},
    {"name": "Yahoo邮箱", "domain": "yahoo.com", "link": "https://mail.yahoo.com", "category": "邮箱"},
    
    {"name": "OneDrive", "domain": "onedrive.live.com", "link": "https://onedrive.live.com", "category": "云盘"},
    {"name": "百度网盘", "domain": "pan.baidu.com", "link": "https://pan.baidu.com", "category": "云盘"},
    {"name": "腾讯微云", "domain": "weiyun.com", "link": "https://www.weiyun.com", "category": "云盘"},
    {"name": "阿里云盘", "domain": "aliyundrive.com", "link": "https://www.aliyundrive.com", "category": "云盘"},
    
    {"name": "Github", "domain": "github.com", "link": "https://github.com", "category": "开发"},
    {"name": "GitLab", "domain": "gitlab.com", "link": "https://gitlab.com", "category": "开发"},

    {"name": "DJI大疆创新", "domain": "dji.com", "link": "https://www.dji.com", "category": "产品"},
    {"name": "影石Insta360", "domain": "insta360.com", "link": "https://www.insta360.com", "category": "产品"},
    {"name": "Apple", "domain": "apple.cn", "link": "https://www.apple.cn", "category": "产品"},
    {"name": "小米", "domain": "mi.com", "link": "https://www.mi.com", "category": "产品"},
    {"name": "OPPO", "domain": "oppo.com", "link": "https://www.oppo.com", "category": "产品"},
    {"name": "vivo", "domain": "vivo.com", "link": "https://www.vivo.com", "category": "产品"},
    {"name": "联想", "domain": "lenovo.com", "link": "https://www.lenovo.com", "category": "产品"},
    {"name": "华硕", "domain": "asus.com", "link": "https://w3.asus.com.cn", "category": "产品"},
    {"name": "华为", "domain": "huawei.com", "link": "https://www.huawei.com", "category": "产品"},
    {"name": "荣耀", "domain": "honor.com", "link": "https://www.honor.com", "category": "产品"},
    {"name": "宇树科技", "domain": "unitree.com", "link": "https://www.unitree.com", "category": "产品"},
    {"name": "Bambu Lab 拓竹科技", "domain": "bambulab.com", "link": "https://bambulab.cn", "category": "产品"},
    {"name": "海尔", "domain": "haier.com", "link": "https://www.haier.com", "category": "产品"},
    {"name": "美的", "domain": "midea.com", "link": "https://www.midea.com", "category": "产品"},
    {"name": "格力", "domain": "gree.com", "link": "https://gree.com", "category": "产品"},
    {"name": "比亚迪", "domain": "byd.com", "link": "https://byd.com", "category": "产品"},
    {"name": "小鹏汽车", "domain": "xiaopeng.com", "link": "https://xiaopeng.com", "category": "产品"},
    {"name": "NIO蔚来", "domain": "nio.com", "link": "https://nio.com", "category": "产品"},
    {"name": "理想汽车", "domain": "lixiang.com", "link": "https://lixiang.com", "category": "产品"},



    {"name": "金山文档", "domain": "kdocs.cn", "link": "https://kdocs.cn", "category": "效率"},
    {"name": "WPS", "domain": "wps.com", "link": "https://wps.cn", "category": "效率"},
    {"name": "飞书", "domain": "feishu.cn", "link": "https://feishu.cn", "category": "效率"},
    {"name": "腾讯文档", "domain": "docs.qq.com", "link": "https://docs.qq.com", "category": "效率"},
    {"name": "腾讯会议", "domain": "meeting.tencent.com", "link": "https://meeting.tencent.com", "category": "效率"},

    {"name": "企业微信", "domain": "work.weixin.qq.com", "link": "https://work.weixin.qq.com", "category": "其他"},
    {"name": "微信", "domain": "weixin.qq.com", "link": "https://weixin.qq.com", "category": "其他"}, 
    {"name": "阿里云", "domain": "aliyun.com", "link": "https://aliyun.com", "category": "其他"},
    {"name": "华为云", "domain": "huaweicloud.com", "link": "https://huaweicloud.com", "category": "其他"},
    {"name": "DeepSeek", "domain": "deepseek.com", "link": "https://deepseek.com", "category": "其他"},
    {"name": "Copilot", "domain": "copilot.com", "link": "https://copilot.com", "category": "其他"}, 

    {"name": "Microsoft 微软", "domain": "microsoft.com", "link": "https://microsoft.com", "category": "其他"},
    {"name": "NVIDIA 英伟达", "domain": "nvidia.cn", "link": "https://nvidia.cn", "category": "其他"},
    {"name": "OpenAI", "domain": "openai.com", "link": "https://openai.com", "category": "其他"},
    {"name": "豆包", "domain": "doubao.com", "link": "https://doubao.com", "category": "其他"}, 
    {"name": "KiMi", "domain": "kimi-zh.com", "link": "https://kimi-zh.com", "category": "其他"},
    {"name": "扣子", "domain": "coze.cn", "link": "https://coze.cn", "category": "其他"},
    {"name": "通义", "domain": "tongyi.aliyun.com", "link": "https://tongyi.aliyun.com", "category": "其他"},
    {"name": "百度文心", "domain": "wenxin.baidu.com", "link": "https://wenxin.baidu.com", "category": "其他"}, 
    {"name": "文心一言", "domain": "yiyan.baidu.com", "link": "https://yiyan.baidu.com", "category": "其他"},
    {"name": "iCloud", "domain": "icloud.com.cn", "link": "https://icloud.com.cn", "category": "其他"},
    {"name": "ToDesk", "domain": "todesk.com", "link": "https://todesk.com", "category": "其他"},
    {"name": "向日葵", "domain": "sunlogin.oray.com", "link": "https://sunlogin.oray.com", "category": "其他"},
    
    {"name": "网易UU远程", "domain": "uuyc.163.com", "link": "https://uuyc.163.com", "category": "其他"},
    {"name": "TeamViewer", "domain": "teamviewer.cn", "link": "https://teamviewer.cn", "category": "其他"},
    {"name": "中国知网", "domain": "cnki.cn", "link": "https://cnki.net", "category": "其他"},
    {"name": "万方数据知识服务平台", "domain": "wanfangdata.com.cn", "link": "https://wanfangdata.com.cn", "category": "其他"}, 
    {"name": "Logitech", "domain": "logitech.com", "link": "https://logitech.com", "category": "其他"},
    {"name": "Unity中国官网", "domain": "unity.cn", "link": "https://unity.cn", "category": "其他"},
    {"name": "Visual Studio Code", "domain": "code.visualstudio.com", "link": "https://code.visualstudio.com", "category": "其他"},
    {"name": "Visual Studio", "domain": "visualstudio.microsoft.com", "link": "https://visualstudio.microsoft.com", "category": "其他"}, 
    {"name": "Qt", "domain": "qt.io", "link": "https://qt.io", "category": "其他"},
    {"name": "Keil", "domain": "keil.com", "link": "https://keil.com", "category": "其他"},
    {"name": "STMCU中文官网", "domain": "stmcu.com.cn", "link": "https://stmcu.com.cn", "category": "其他"},
    {"name": "意法半导体", "domain": "st.com.cn", "link": "https://st.com.cn", "category": "其他"},  

    {"name": "嘉立创EDA", "domain": "lceda.cn", "link": "https://lceda.cn", "category": "其他"},
    {"name": "立创商城", "domain": "szlcsc.com", "link": "https://szlcsc.com", "category": "其他"},
    {"name": "RoboMaster 机甲大师赛", "domain": "robomaster.com", "link": "https://robomaster.com", "category": "其他"},
    {"name": "Microsoft 365", "domain": "office.com", "link": "https://office.com", "category": "其他"},
    {"name": "Microsoft Apps", "domain": "apps.microsoft.com", "link": "https://apps.microsoft.com", "category": "其他"},
    {"name": "搜狐视频", "domain": "tv.sohu.com", "link": "https://tv.sohu.com", "category": "其他"}, 
    {"name": "央视频", "domain": "yangshipin.cn", "link": "https://yangshipin.cn", "category": "其他"},
    {"name": "咪咕音乐", "domain": "music.migu.cn", "link": "https://music.migu.cn", "category": "其他"},
    {"name": "咪咕视频", "domain": "miguvideo.com", "link": "https://miguvideo.com", "category": "其他"},
]

# 获取网站图标
def fetch_icon(domain):
    urls = [
        f"https://{domain}/manifest.json",
        f"https://{domain}/apple-touch-icon.png",
        f"https://{domain}/favicon.ico",
        f"https://api.iowen.cn/favicon/{domain}.png"  # 兜底方案
    ]
    
    for url in urls:
        try:
            response = requests.get(url, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                return url
        except requests.exceptions.RequestException:
            continue
    
    return None  # 如果所有图标都无法获取，则返回 None

# 保存图标到 `icons/` 目录
def save_icon(domain):
    icon_url = fetch_icon(domain)
    if icon_url:
        response = requests.get(icon_url, headers=HEADERS, stream=True)
        if response.status_code == 200:
            with open(f"icons/{domain}.png", "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ {domain} 图标已保存")
        else:
            print(f"❌ 无法获取 {domain} 图标")
    else:
        print(f"⚠️ {domain} 没有可用图标")

# 提取所有 `domain` 并抓取图标
domains = [item["domain"] for item in json_data]
for domain in domains:
    save_icon(domain)

# Git 操作：提交并推送到 GitHub
def git_push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "更新图标"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ 图标已推送到 GitHub")
    except Exception as e:
        print(f"❌ Git 操作失败: {e}")

git_push()
