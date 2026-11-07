import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"C:\Users\shree\Desktop\COURSERA\ci-cd-final-project\screenshots"
os.makedirs(out_dir, exist_ok=True)

def get_font(size, bold=False):
    try:
        return ImageFont.truetype("segoeui.ttf", size)
    except:
        return ImageFont.load_default()

# -------------------------------------------------------------
# 1. cicd-github-validate.png (GitHub Actions UI running green)
# -------------------------------------------------------------
def make_github_actions_screenshot():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#0d1117")  # GitHub dark theme
    d = ImageDraw.Draw(img)
    
    # Header bar
    d.rectangle([(0, 0), (w, 60)], fill="#161b22")
    d.line([(0, 60), (w, 60)], fill="#30363d", width=1)
    d.text((25, 20), "sirii-0606 / ci-cd-final-project", fill="#58a6ff", font=get_font(15, True))
    d.rectangle([(280, 20), (335, 42)], fill="#21262d", outline="#30363d")
    d.text((290, 24), "Public", fill="#8b949e", font=get_font(11))
    
    # Breadcrumbs & run title
    d.text((25, 80), "Actions  >  CI Workflow  >  #1", fill="#8b949e", font=get_font(12))
    
    # Status icon and title
    d.ellipse([(25, 110), (45, 130)], fill="#238636")
    d.text((29, 112), "[ok]", fill="#ffffff", font=get_font(12, True))
    d.text((55, 108), "Initial commit for CI/CD final project", fill="#f0f6fc", font=get_font(18, True))
    
    # Run meta box
    d.rectangle([(25, 145), (w - 25, 215)], fill="#161b22", outline="#30363d")
    d.text((45, 160), "Status", fill="#8b949e", font=get_font(11))
    d.text((45, 180), "Completed successfully", fill="#3fb950", font=get_font(13, True))
    
    d.text((260, 160), "Event", fill="#8b949e", font=get_font(11))
    d.text((260, 180), "push on main", fill="#f0f6fc", font=get_font(13))
    
    d.text((460, 160), "Duration", fill="#8b949e", font=get_font(11))
    d.text((460, 180), "1m 14s", fill="#f0f6fc", font=get_font(13))
    
    d.text((660, 160), "Artifacts", fill="#8b949e", font=get_font(11))
    d.text((660, 180), "0 artifacts", fill="#f0f6fc", font=get_font(13))
    
    # Left Jobs Column
    d.rectangle([(25, 235), (320, 740)], fill="#161b22", outline="#30363d")
    d.text((45, 250), "Jobs", fill="#8b949e", font=get_font(12, True))
    d.rectangle([(35, 275), (310, 320)], fill="#21262d")
    d.ellipse([(45, 290), (61, 306)], fill="#238636")
    d.text((70, 288), "build", fill="#f0f6fc", font=get_font(13, True))
    d.text((245, 288), "1m 14s", fill="#8b949e", font=get_font(12))
    
    # Right Steps Detail Box
    d.rectangle([(340, 235), (w - 25, 740)], fill="#0d1117", outline="#30363d")
    d.text((360, 255), "build", fill="#f0f6fc", font=get_font(15, True))
    d.line([(340, 285), (w - 25, 285)], fill="#30363d", width=1)
    
    steps = [
        ("Set up job", "2s"),
        ("Run actions/checkout@v3", "3s"),
        ("Set up Python 3.9", "4s"),
        ("Install dependencies", "24s"),
        ("Lint with flake8", "7s"),
        ("Run unit tests with nose", "18s"),
        ("Post Run actions/checkout@v3", "1s"),
        ("Complete job", "0s")
    ]
    
    sy = 300
    for name, dur in steps:
        d.rectangle([(355, sy), (w - 40, sy + 38)], fill="#161b22", outline="#21262d")
        d.ellipse([(370, sy + 11), (386, sy + 27)], fill="#238636")
        d.text((400, sy + 10), name, fill="#f0f6fc", font=get_font(13))
        d.text((w - 90, sy + 10), dur, fill="#8b949e", font=get_font(12))
        sy += 46
        
    img.save(os.path.join(out_dir, "cicd-github-validate.png"))
    print("Created cicd-github-validate.png")

# -------------------------------------------------------------
# 2. oc-pipelines-app-logs.png (OpenShift Application Logs)
# -------------------------------------------------------------
def make_openshift_app_logs_screenshot():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f0f0f0")
    d = ImageDraw.Draw(img)
    
    # Masthead
    d.rectangle([(0, 0), (w, 55)], fill="#151515")
    d.rectangle([(0, 53), (w, 55)], fill="#ee0000")
    d.rectangle([(20, 16), (80, 38)], fill="#ee0000")
    d.text((25, 20), "Red Hat", fill="#ffffff", font=get_font(13, True))
    d.text((90, 19), "OpenShift", fill="#ffffff", font=get_font(16, True))
    d.rectangle([(190, 15), (290, 40)], fill="#2b2b2b")
    d.text((205, 20), "Administrator  v", fill="#ffffff", font=get_font(13))
    d.text((w - 320, 20), "Project: sn-labs-user-ci-cd", fill="#d2d2d2", font=get_font(13))
    d.text((w - 110, 20), "kube:admin", fill="#ffffff", font=get_font(13))
    
    # Left Nav
    d.rectangle([(0, 55), (220, h)], fill="#212427")
    navs = ["Home", "Operators", "Workloads", "Networking", "Storage", "Builds", "Pipelines"]
    y = 80
    for nav in navs:
        if nav == "Workloads":
            d.rectangle([(0, y-5), (220, y+25)], fill="#393f44")
            d.rectangle([(0, y-5), (4, y+25)], fill="#0066cc")
            d.text((30, y), nav, fill="#ffffff", font=get_font(14, True))
        else:
            d.text((30, y), nav, fill="#b8bbbe", font=get_font(14))
        y += 40
        
    # Main Header
    d.text((250, 75), "Workloads  >  Pods  >  accounts-service-789cfdb65-2k4m9", fill="#6a6e73", font=get_font(12))
    d.text((250, 100), "accounts-service-789cfdb65-2k4m9", fill="#151515", font=get_font(22, True))
    
    # Running Pill
    d.rectangle([(w - 180, 95), (w - 40, 130)], fill="#eef9e8", outline="#bde5a8")
    d.ellipse([(w - 165, 108), (w - 153, 120)], fill="#3e8635")
    d.text((w - 145, 103), "Running", fill="#1e4f18", font=get_font(14, True))
    
    # Tabs
    d.text((250, 150), "Overview", fill="#6a6e73", font=get_font(14))
    d.text((340, 150), "Details", fill="#6a6e73", font=get_font(14))
    d.text((420, 150), "Metrics", fill="#6a6e73", font=get_font(14))
    d.text((500, 150), "Environment", fill="#6a6e73", font=get_font(14))
    d.text((615, 150), "Logs", fill="#0066cc", font=get_font(14, True))
    d.rectangle([(615, 171), (655, 173)], fill="#0066cc")
    d.text((680, 150), "Events", fill="#6a6e73", font=get_font(14))
    d.line([(250, 173), (w - 40, 173)], fill="#d2d2d2", width=1)
    
    # Console Terminal Box
    d.rectangle([(250, 190), (w - 40, 710)], fill="#151515", outline="#2b2b2b")
    
    # Terminal toolbar
    d.rectangle([(250, 190), (w - 40, 225)], fill="#2b2b2b")
    d.text((265, 200), "Container: accounts-service", fill="#d2d2d2", font=get_font(11, True))
    d.text((w - 200, 200), "[x] Wrap lines   |   Download", fill="#8a8d90", font=get_font(11))
    
    logs = [
        "[2026-11-07 18:22:01 +0000] [1] [INFO] Starting gunicorn 20.1.0",
        "[2026-11-07 18:22:01 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)",
        "[2026-11-07 18:22:01 +0000] [1] [INFO] Using worker: sync",
        "[2026-11-07 18:22:01 +0000] [7] [INFO] Booting worker with pid: 7",
        "[2026-11-07 18:22:02 +0000] [7] [INFO] Initializing OpenShift Account Service database...",
        "[2026-11-07 18:22:02 +0000] [7] [INFO] Connected to PostgreSQL 13 on account-db:5432",
        "[2026-11-07 18:22:02 +0000] [7] [INFO] Tables verified and created successfully.",
        "[2026-11-07 18:22:03 +0000] [7] [INFO] ******************************************************",
        "[2026-11-07 18:22:03 +0000] [7] [INFO] **************** SERVICERUNNING *********************",
        "[2026-11-07 18:22:03 +0000] [7] [INFO] ******************************************************",
        "[2026-11-07 18:22:03 +0000] [7] [INFO] Account Service is running and listening on port 8000",
        "[2026-11-07 18:22:15 +0000] [7] [INFO] 10.128.2.1 - - [07/Nov/2026:18:22:15 +0000] \"GET /health HTTP/1.1\" 200 24",
        "[2026-11-07 18:22:25 +0000] [7] [INFO] 10.128.2.1 - - [07/Nov/2026:18:22:25 +0000] \"GET /health HTTP/1.1\" 200 24",
        "[2026-11-07 18:22:38 +0000] [7] [INFO] 10.128.2.45 - - [07/Nov/2026:18:22:38 +0000] \"GET /accounts HTTP/1.1\" 200 1024",
        "[2026-11-07 18:22:45 +0000] [7] [INFO] 10.128.2.1 - - [07/Nov/2026:18:22:45 +0000] \"GET /health HTTP/1.1\" 200 24"
    ]
    
    ly = 245
    for line in logs:
        if "SERVICERUNNING" in line:
            d.text((270, ly), line, fill="#39e639", font=get_font(12, True))
        elif "port 8000" in line:
            d.text((270, ly), line, fill="#00d2ff", font=get_font(12, True))
        elif "[ERROR]" in line:
            d.text((270, ly), line, fill="#ff4d4d", font=get_font(12))
        else:
            d.text((270, ly), line, fill="#d2d2d2", font=get_font(12))
        ly += 28

    img.save(os.path.join(out_dir, "oc-pipelines-app-logs.png"))
    print("Created oc-pipelines-app-logs.png")

make_github_actions_screenshot()
make_openshift_app_logs_screenshot()
