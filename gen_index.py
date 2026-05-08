html_code = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PAT Unlock - Professional iPhone Services</title>
    <meta name="description" content="Unlock iPhone IMEI từ xa uy tín, bảo hành vĩnh viễn. Mọi dòng máy.">
    <meta property="og:title" content="PAT Unlock iPhone Pro">
    <meta property="og:description" content="Giải pháp mở mạng iPhone IMEI vĩnh viễn từ Server. Uy tín - Bảo hành trọn đời.">
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0d1117;
            --card-bg: #161b22;
            --text-primary: #f0f6fc;
            --text-secondary: #8b949e;
            --accent-color: #2f81f7; /* Zalo Blue */
            --accent-hover: #58a6ff;
            --border-color: #30363d;
        }

        * { box-sizing: border-box; }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            margin: 0;
            display: flex;
            justify-content: center;
            min-height: 100vh;
            padding: 40px 20px;
        }

        .container {
            width: 100%;
            max-width: 450px;
            text-align: center;
        }

        .avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 3px solid var(--accent-color);
            margin-bottom: 20px;
            object-fit: cover;
            /* Thêm hiệu ứng phát sáng neon nhẹ cho avatar */
            box-shadow: 0 0 15px rgba(47, 129, 247, 0.4);
        }

        h1 {
            font-size: 1.6rem;
            margin: 0;
            letter-spacing: -0.5px;
        }

        .bio {
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin: 15px 0 32px;
            line-height: 1.6;
        }

        .links-group {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .link-item {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px;
            text-decoration: none;
            color: var(--text-primary);
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .link-item:hover {
            transform: scale(1.02);
            border-color: var(--accent-hover);
            background-color: #1c2128;
        }

        /* Nút Zalo nổi bật */
        .link-item.primary {
            background-color: var(--accent-color);
            border: none;
            color: #ffffff;
            box-shadow: 0 4px 20px rgba(47, 129, 247, 0.25);
            animation: pulse 2s infinite;
        }

        .link-item.primary:hover {
            background-color: var(--accent-hover);
        }

        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 4px 15px rgba(47, 129, 247, 0.25); }
            50% { transform: scale(1.03); box-shadow: 0 6px 20px rgba(47, 129, 247, 0.35); }
            100% { transform: scale(1); box-shadow: 0 4px 15px rgba(47, 129, 247, 0.25); }
        }

        footer {
            margin-top: 60px;
            color: var(--text-secondary);
            font-size: 0.8rem;
        }

        .dev-tag { font-family: monospace; color: var(--accent-color); }
    </style>
</head>
<body>

    <div class="container">
        <img src="pat-logo.jpg" alt="PAT Unlock iPhone PRO Logo" class="avatar">
        
        <h1>PAT Unlock iPhone Pro</h1>
        <p class="bio">
            Mở mạng iPhone IMEI vĩnh viễn từ Server.<br>
            Bảo hành trọn đời • Mọi dòng máy • 100% Online.<br>
            👨‍💻 Hỗ trợ 24/7 trực tiếp từ Senior Dev.
        </p>

        <div class="links-group">
            <a href="https://zalo.me/0785812801" class="link-item primary" id="zalo-cta">
                GỬI IMEI - CHECK TỈ LỆ THÀNH CÔNG
            </a>

            <a href="https://facebook.com/pat.unlockiphonepro" class="link-item">
                Facebook: Cộng đồng & Feedback
            </a>
            <a href="https://youtube.com/@patunlockiphonepro" class="link-item">
                YouTube: Quy trình kỹ thuật
            </a>
            <a href="https://www.tiktok.com/@pat.unlock.iphone.pro" class="link-item">
                TikTok: Tin tức & Mẹo iPhone
            </a>
        </div>

        <footer>
            Xử lý bởi <span class="dev-tag">Senior Backend Dev</span><br>
            &copy; 2026 PAT Unlock. Crafted with care.
        </footer>
    </div>

    <script>
        // Logic Tracking Source
        (function() {
            const urlParams = new URLSearchParams(window.location.search);
            const source = urlParams.get('src');
            
            if (source) {
                const cta = document.getElementById('zalo-cta');
                const currentHref = cta.getAttribute('href');
                // Gắn source vào link Zalo để anh biết khách từ đâu tới
                cta.setAttribute('href', currentHref + '?utm_source=' + source);
                console.log('Source detected: ' + source);
            }
        })();
    </script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)
