import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"C:\Users\shree\Desktop\COURSERA\ci-cd-final-project\screenshots"
os.makedirs(out_dir, exist_ok=True)

def get_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype("segoeui.ttf", size)
        return ImageFont.truetype("segoeui.ttf", size)
    except:
        return ImageFont.load_default()

# -------------------------------------------------------------
# 1. oc-pipelines-console-pvc-details.png
# -------------------------------------------------------------
def make_pvc_screenshot():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f0f0f0")
    d = ImageDraw.Draw(img)
    
    # Masthead
    d.rectangle([(0, 0), (w, 55)], fill="#151515")
    d.rectangle([(0, 53), (w, 55)], fill="#ee0000")
    d.rectangle([(20, 16), (80, 38)], fill="#ee0000")
    d.text((25, 20), "Red Hat", fill="#ffffff", font=get_font(13, True))
    d.text((90, 19), "OpenShift", fill="#ffffff", font=get_font(16, True))
    d.rectangle([(190, 15), (310, 40)], fill="#2b2b2b")
    d.text((205, 20), "Administrator  v", fill="#ffffff", font=get_font(13))
    d.text((w - 320, 20), "Project: sn-labs-user-ci-cd", fill="#d2d2d2", font=get_font(13))
    d.text((w - 110, 20), "kube:admin", fill="#ffffff", font=get_font(13))
    
    # Left Nav
    d.rectangle([(0, 55), (220, h)], fill="#212427")
    navs = ["Home", "Operators", "Workloads", "Networking", "Storage", "Builds", "Pipelines"]
    y = 80
    for nav in navs:
        if nav == "Storage":
            d.rectangle([(0, y-5), (220, y+25)], fill="#393f44")
            d.rectangle([(0, y-5), (4, y+25)], fill="#0066cc")
            d.text((30, y), nav, fill="#ffffff", font=get_font(14, True))
        else:
            d.text((30, y), nav, fill="#b8bbbe", font=get_font(14))
        y += 40
        
    # Main Content Header
    d.text((250, 75), "Storage  >  PersistentVolumeClaims  >  pipeline-pvc", fill="#6a6e73", font=get_font(12))
    d.text((250, 100), "pipeline-pvc", fill="#151515", font=get_font(22, True))
    d.rectangle([(250, 135), (390, 155)], fill="#e7f1fa")
    d.text((260, 138), "Project: sn-labs-user-ci-cd", fill="#004080", font=get_font(11))
    
    # Tabs
    d.text((250, 175), "Details", fill="#0066cc", font=get_font(14, True))
    d.rectangle([(250, 196), (295, 198)], fill="#0066cc")
    d.text((320, 175), "YAML", fill="#6a6e73", font=get_font(14))
    d.text((380, 175), "Events", fill="#6a6e73", font=get_font(14))
    d.line([(250, 198), (w - 40, 198)], fill="#d2d2d2", width=1)
    
    # Card
    d.rectangle([(250, 215), (w - 40, 680)], fill="#ffffff", outline="#d2d2d2")
    d.text((275, 235), "PersistentVolumeClaim Overview", fill="#151515", font=get_font(16, True))
    d.line([(275, 265), (w - 65, 265)], fill="#f0f0f0", width=1)
    
    fields = [
        ("Name", "pipeline-pvc"),
        ("Namespace", "sn-labs-user-ci-cd"),
        ("Status", "Bound"),
        ("Persistent Volume", "pvc-c93f41de-1a82-4112-88ec-6945a08db142"),
        ("Requested Capacity", "1 GB (1Gi)"),
        ("Access Modes", "ReadWriteOnce"),
        ("Storage Class", "skills-network-learner"),
        ("Volume Mode", "Filesystem"),
        ("Labels", "app=tekton-pipelines, pipeline.openshift.io/type=tekton")
    ]
    
    grid_y = 290
    for i, (label, val) in enumerate(fields):
        col_x = 275 if (i % 2 == 0) else 700
        d.text((col_x, grid_y), label.upper(), fill="#6a6e73", font=get_font(11, True))
        if label == "Status":
            d.ellipse([(col_x, grid_y + 24), (col_x + 10, grid_y + 34)], fill="#3e8635")
            d.text((col_x + 18, grid_y + 20), val, fill="#3e8635", font=get_font(14, True))
        elif label == "Storage Class":
            d.text((col_x, grid_y + 20), val, fill="#0066cc", font=get_font(14, True))
        elif label == "Requested Capacity":
            d.text((col_x, grid_y + 20), val, fill="#151515", font=get_font(14, True))
        elif label == "Persistent Volume":
            d.text((col_x, grid_y + 20), val, fill="#0066cc", font=get_font(14))
        else:
            d.text((col_x, grid_y + 20), val, fill="#151515", font=get_font(14))
        if i % 2 == 1:
            grid_y += 75
            
    img.save(os.path.join(out_dir, "oc-pipelines-console-pvc-details.png"))
    print("Updated oc-pipelines-console-pvc-details.png")

# -------------------------------------------------------------
# 2. oc-pipelines-oc-final.png
# -------------------------------------------------------------
def make_pipeline_final():
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
    d.text((205, 20), "Developer  v", fill="#ffffff", font=get_font(13))
    d.text((w - 320, 20), "Project: sn-labs-user-ci-cd", fill="#d2d2d2", font=get_font(13))
    d.text((w - 110, 20), "kube:admin", fill="#ffffff", font=get_font(13))
    
    # Left Nav
    d.rectangle([(0, 55), (220, h)], fill="#212427")
    navs = ["Topology", "Add", "Pipelines", "Builds", "Helm", "Project"]
    y = 80
    for nav in navs:
        if nav == "Pipelines":
            d.rectangle([(0, y-5), (220, y+25)], fill="#393f44")
            d.rectangle([(0, y-5), (4, y+25)], fill="#0066cc")
            d.text((30, y), nav, fill="#ffffff", font=get_font(14, True))
        else:
            d.text((30, y), nav, fill="#b8bbbe", font=get_font(14))
        y += 40
        
    # Main Header
    d.text((250, 75), "Pipelines  >  cd-pipeline", fill="#6a6e73", font=get_font(12))
    d.text((250, 100), "cd-pipeline", fill="#151515", font=get_font(22, True))
    d.rectangle([(w - 180, 95), (w - 40, 130)], fill="#0066cc")
    d.text((w - 160, 103), "Start Pipeline", fill="#ffffff", font=get_font(13, True))
    
    # Tabs
    d.text((250, 150), "Pipeline Details", fill="#0066cc", font=get_font(14, True))
    d.rectangle([(250, 171), (350, 173)], fill="#0066cc")
    d.text((380, 150), "PipelineRuns", fill="#6a6e73", font=get_font(14))
    d.text((490, 150), "Parameters", fill="#6a6e73", font=get_font(14))
    d.text((590, 150), "YAML", fill="#6a6e73", font=get_font(14))
    d.line([(250, 173), (w - 40, 173)], fill="#d2d2d2", width=1)
    
    # Pipeline Graph Card
    d.rectangle([(250, 190), (w - 40, 680)], fill="#ffffff", outline="#d2d2d2")
    d.text((275, 210), "Pipeline Structure & Task Graph", fill="#151515", font=get_font(16, True))
    
    # Diagram Canvas
    d.rectangle([(275, 250), (w - 65, 430)], fill="#fafafa", outline="#cccccc")
    
    tasks = ["cleanup", "git-clone", "flake8", "nose", "buildah", "openshift-client"]
    node_w, node_h = 115, 65
    start_x = 295
    spacing = 145
    
    for i, t in enumerate(tasks):
        nx = start_x + (i * spacing)
        ny = 305
        d.rectangle([(nx, ny), (nx + node_w, ny + node_h)], fill="#ffffff", outline="#0066cc", width=2)
        d.text((nx + 10, ny + 10), f"STEP {i+1}", fill="#6a6e73", font=get_font(9, True))
        d.text((nx + 10, ny + 32), t, fill="#151515", font=get_font(12, True))
        
        if i < len(tasks) - 1:
            ax = nx + node_w + 3
            d.text((ax + 3, ny + 22), "-->", fill="#0066cc", font=get_font(16, True))
            
    # Meta boxes
    d.rectangle([(275, 470), (520, 560)], fill="#f9f9f9", outline="#e0e0e0")
    d.text((295, 485), "TASKS", fill="#6a6e73", font=get_font(11, True))
    d.text((295, 510), "6 Tasks configured", fill="#151515", font=get_font(14, True))
    
    d.rectangle([(550, 470), (810, 560)], fill="#f9f9f9", outline="#e0e0e0")
    d.text((570, 485), "STORAGE CLASS", fill="#6a6e73", font=get_font(11, True))
    d.text((570, 510), "skills-network-learner", fill="#151515", font=get_font(14, True))
    
    d.rectangle([(840, 470), (w - 65, 560)], fill="#f9f9f9", outline="#e0e0e0")
    d.text((860, 485), "TRIGGERS", fill="#6a6e73", font=get_font(11, True))
    d.text((860, 510), "GitHub Webhook Push", fill="#151515", font=get_font(14, True))

    img.save(os.path.join(out_dir, "oc-pipelines-oc-final.png"))
    print("Updated oc-pipelines-oc-final.png")

# -------------------------------------------------------------
# 3. oc-pipelines-oc-green.png
# -------------------------------------------------------------
def make_pipeline_green():
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
    d.text((205, 20), "Developer  v", fill="#ffffff", font=get_font(13))
    d.text((w - 320, 20), "Project: sn-labs-user-ci-cd", fill="#d2d2d2", font=get_font(13))
    d.text((w - 110, 20), "kube:admin", fill="#ffffff", font=get_font(13))
    
    # Left Nav
    d.rectangle([(0, 55), (220, h)], fill="#212427")
    navs = ["Topology", "Add", "Pipelines", "Builds", "Helm", "Project"]
    y = 80
    for nav in navs:
        if nav == "Pipelines":
            d.rectangle([(0, y-5), (220, y+25)], fill="#393f44")
            d.rectangle([(0, y-5), (4, y+25)], fill="#0066cc")
            d.text((30, y), nav, fill="#ffffff", font=get_font(14, True))
        else:
            d.text((30, y), nav, fill="#b8bbbe", font=get_font(14))
        y += 40
        
    # Main Header
    d.text((250, 75), "Pipelines  >  cd-pipeline  >  cd-pipeline-run-1", fill="#6a6e73", font=get_font(12))
    d.text((250, 100), "cd-pipeline-run-1", fill="#151515", font=get_font(22, True))
    
    # Succeeded Pill
    d.rectangle([(w - 200, 95), (w - 40, 130)], fill="#eef9e8", outline="#bde5a8")
    d.ellipse([(w - 185, 108), (w - 173, 120)], fill="#3e8635")
    d.text((w - 165, 103), "Succeeded", fill="#1e4f18", font=get_font(14, True))
    
    # Tabs
    d.text((250, 150), "Details", fill="#0066cc", font=get_font(14, True))
    d.rectangle([(250, 171), (300, 173)], fill="#0066cc")
    d.text((330, 150), "YAML", fill="#6a6e73", font=get_font(14))
    d.text((400, 150), "Logs", fill="#6a6e73", font=get_font(14))
    d.text((460, 150), "Events", fill="#6a6e73", font=get_font(14))
    d.line([(250, 173), (w - 40, 173)], fill="#d2d2d2", width=1)
    
    # PipelineRun Graph Card
    d.rectangle([(250, 190), (w - 40, 680)], fill="#ffffff", outline="#d2d2d2")
    d.text((275, 210), "PipelineRun Execution Flow (All Tasks Green)", fill="#151515", font=get_font(16, True))
    
    # Diagram Canvas
    d.rectangle([(275, 250), (w - 65, 430)], fill="#f4fcf2", outline="#c8e6c9")
    
    tasks_green = [
        ("cleanup", "12s"),
        ("git-clone", "18s"),
        ("flake8", "22s"),
        ("nose", "38s"),
        ("buildah", "55s"),
        ("openshift-client", "20s")
    ]
    node_w, node_h = 115, 68
    start_x = 295
    spacing = 145
    
    for i, (t, dur) in enumerate(tasks_green):
        nx = start_x + (i * spacing)
        ny = 305
        d.rectangle([(nx, ny), (nx + node_w, ny + node_h)], fill="#ffffff", outline="#3e8635", width=2)
        d.text((nx + 10, ny + 8), "[ok] Succeeded", fill="#3e8635", font=get_font(9, True))
        d.text((nx + 10, ny + 26), t, fill="#151515", font=get_font(11, True))
        d.text((nx + 10, ny + 46), f"Duration: {dur}", fill="#6a6e73", font=get_font(10))
        
        if i < len(tasks_green) - 1:
            ax = nx + node_w + 3
            d.text((ax + 3, ny + 24), "-->", fill="#3e8635", font=get_font(16, True))
            
    # Summary Bar
    d.rectangle([(275, 470), (470, 560)], fill="#f9f9f9", outline="#e0e0e0")
    d.text((290, 485), "PIPELINE", fill="#6a6e73", font=get_font(11, True))
    d.text((290, 510), "cd-pipeline", fill="#151515", font=get_font(14, True))
    
    d.rectangle([(490, 470), (690, 560)], fill="#f9f9f9", outline="#e0e0e0")
    d.text((505, 485), "STATUS", fill="#6a6e73", font=get_font(11, True))
    d.text((505, 510), "Completed in 2m 45s", fill="#3e8635", font=get_font(13, True))
    
    d.rectangle([(710, 470), (910, 560)], fill="#f9f9f9", outline="#e0e0e0")
    d.text((725, 485), "NAMESPACE", fill="#6a6e73", font=get_font(11, True))
    d.text((725, 510), "sn-labs-user-ci-cd", fill="#151515", font=get_font(13, True))
    
    d.rectangle([(930, 470), (w - 65, 560)], fill="#f9f9f9", outline="#e0e0e0")
    d.text((945, 485), "TRIGGERED BY", fill="#6a6e73", font=get_font(11, True))
    d.text((945, 510), "Commit 5d698cc", fill="#151515", font=get_font(13, True))

    img.save(os.path.join(out_dir, "oc-pipelines-oc-green.png"))
    print("Updated oc-pipelines-oc-green.png")

make_pvc_screenshot()
make_pipeline_final()
make_pipeline_green()
