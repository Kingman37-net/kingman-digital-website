import os

# Read nav and footer
with open('templates/nav.html', 'r') as f:
    nav = f.read()
with open('templates/footer.html', 'r') as f:
    footer = f.read()

# Basic CSS (same as index but minimal – we'll use the same variables)
base_css = """
:root {
  --primary: #0b7fab;
  --accent: #00d1ff;
  --dark: #0a0f14;
  --light: #ffffff;
  --muted: #b9c6cf;
  --bg-gradient: linear-gradient(180deg, #060b10, #0a1118);
  --card-bg: rgba(255,255,255,0.04);
  --border: rgba(255,255,255,0.08);
  --nav-bg: #0a1118;
  --footer-bg: #05080c;
}
* { margin:0; padding:0; box-sizing:border-box; font-family:"Segoe UI", system-ui, sans-serif; }
body { background:var(--bg-gradient); color:var(--light); line-height:1.7; }
nav { position:fixed; top:0; width:100%; background:var(--nav-bg); border-bottom:1px solid var(--border); z-index:999; padding:1rem; }
.nav-container { display:flex; justify-content:space-between; align-items:center; max-width:1200px; margin:auto; }
.nav-menu { display:flex; gap:30px; list-style:none; }
.nav-menu a { color:var(--light); text-decoration:none; font-weight:600; }
.logo img { height:40px; }
.hamburger { display:none; }
.bar { display:block; width:25px; height:3px; margin:5px auto; background:var(--light); }
.theme-toggle { background:none; border:none; font-size:1.5rem; cursor:pointer; margin-left:1rem; }
header { text-align:center; padding:140px 20px 80px; }
h1 { font-size:2.5rem; }
h1 span { color:var(--accent); }
section { max-width:800px; margin:auto; padding:70px 20px; text-align:center; }
p { color:var(--muted); }
footer { background:var(--footer-bg); padding:50px 20px 30px; color:var(--muted); text-align:center; }
"""

# Dropdown CSS (minimal)
dropdown_css = """
/* Dropdown styling */
.nav-menu li { position: relative; }
.dropdown-content { display:none; position:absolute; background:var(--nav-bg); min-width:200px; box-shadow:0 8px 16px rgba(0,0,0,0.5); z-index:1000; border-radius:8px; border:1px solid var(--border); }
.dropdown-content a { color:var(--light); padding:12px 16px; text-decoration:none; display:block; text-align:left; }
.dropdown-content a:hover { background:rgba(255,255,255,0.1); color:var(--accent); }
.dropdown:hover .dropdown-content { display:block; }
@media (max-width:768px) {
  .dropdown-content { position:static; box-shadow:none; border:none; background:transparent; }
  .dropdown.active .dropdown-content { display:block; }
}
"""

# Chat widget script (same as previously inserted)
chat_widget = """
<!-- KDCN Chat Widget -->
<style>
.kdcn-chat-btn { position:fixed; bottom:25px; right:25px; width:60px; height:60px; border-radius:50%; background:linear-gradient(135deg,#0b7fab,#00d1ff); border:none; cursor:pointer; box-shadow:0 8px 20px rgba(0,0,0,0.3); z-index:1000; display:flex; align-items:center; justify-content:center; font-size:30px; color:#000; transition:transform 0.3s; }
.kdcn-chat-btn:hover { transform:scale(1.1); }
.kdcn-chat-panel { position:fixed; bottom:95px; right:25px; width:320px; max-width:90vw; height:420px; max-height:70vh; background:#0a1118; border:1px solid rgba(255,255,255,0.1); border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.5); display:none; flex-direction:column; overflow:hidden; z-index:1001; }
.kdcn-chat-panel.active { display:flex; }
.kdcn-chat-header { background:linear-gradient(135deg,#0b7fab,#00d1ff); padding:15px; color:#000; font-weight:bold; display:flex; justify-content:space-between; align-items:center; }
.kdcn-chat-header span { font-size:1.1rem; }
.kdcn-chat-close { background:none; border:none; font-size:1.5rem; cursor:pointer; color:#000; }
.kdcn-chat-body { flex:1; padding:15px; overflow-y:auto; color:#fff; }
.kdcn-chat-message { margin-bottom:12px; display:flex; flex-direction:column; }
.kdcn-chat-message.bot { align-items:flex-start; }
.kdcn-chat-message.user { align-items:flex-end; }
.kdcn-chat-bubble { max-width:80%; padding:10px 15px; border-radius:18px; background:rgba(255,255,255,0.1); font-size:0.9rem; line-height:1.4; }
.kdcn-chat-message.user .kdcn-chat-bubble { background:#00d1ff; color:#000; }
.kdcn-chat-input { display:flex; padding:10px; background:rgba(0,0,0,0.2); }
.kdcn-chat-input input { flex:1; padding:10px; border-radius:20px; border:1px solid rgba(255,255,255,0.2); background:#fff; color:#000; outline:none; }
.kdcn-chat-input button { margin-left:10px; padding:10px 20px; border-radius:20px; border:none; background:#00d1ff; color:#000; font-weight:bold; cursor:pointer; }
</style>
<button class="kdcn-chat-btn" id="kdcnChatBtn" aria-label="Chat with us">💬</button>
<div class="kdcn-chat-panel" id="kdcnChatPanel">
  <div class="kdcn-chat-header">
    <span>KDCN Assistant</span>
    <button class="kdcn-chat-close" id="kdcnChatClose">&times;</button>
  </div>
  <div class="kdcn-chat-body" id="kdcnChatBody">
    <div class="kdcn-chat-message bot">
      <div class="kdcn-chat-bubble">Hello! I'm the KDCN virtual assistant. Ask me about our services, pricing, or how to get started.</div>
    </div>
  </div>
  <div class="kdcn-chat-input">
    <input type="text" id="kdcnChatInput" placeholder="Type your question...">
    <button id="kdcnChatSend">Send</button>
  </div>
</div>
<script>
(function() {
  var btn = document.getElementById('kdcnChatBtn');
  var panel = document.getElementById('kdcnChatPanel');
  var close = document.getElementById('kdcnChatClose');
  var body = document.getElementById('kdcnChatBody');
  var input = document.getElementById('kdcnChatInput');
  var send = document.getElementById('kdcnChatSend');
  if (!btn || !panel) return;
  btn.addEventListener('click', function() { panel.classList.toggle('active'); });
  close.addEventListener('click', function() { panel.classList.remove('active'); });
  function addMessage(text, sender) {
    var msgDiv = document.createElement('div');
    msgDiv.className = 'kdcn-chat-message ' + sender;
    var bubble = document.createElement('div');
    bubble.className = 'kdcn-chat-bubble';
    bubble.textContent = text;
    msgDiv.appendChild(bubble);
    body.appendChild(msgDiv);
    body.scrollTop = body.scrollHeight;
  }
  function getBotResponse(userText) {
    var t = userText.toLowerCase();
    if (t.indexOf('hello') !== -1 || t.indexOf('hi') !== -1) return "Hi there! How can I help you today?";
    if (t.indexOf('service') !== -1 || t.indexOf('offer') !== -1) return "We provide Cybersecurity Systems, IT Infrastructure & Cloud, Software Development, and Digital Systems Consulting. Which one are you interested in?";
    if (t.indexOf('price') !== -1 || t.indexOf('cost') !== -1 || t.indexOf('fee') !== -1) return "Our pricing depends on the scope of the project. Please contact us via email or WhatsApp for a custom quote.";
    if (t.indexOf('contact') !== -1 || t.indexOf('reach') !== -1) return "You can email us at kingmandigitalcybernetwork@gmail.com or WhatsApp +254111843716.";
    if (t.indexOf('location') !== -1 || t.indexOf('where') !== -1) return "We are based in Embu, Kenya, serving clients globally.";
    if (t.indexOf('platform') !== -1 || t.indexOf('ecosystem') !== -1) return "Our KDCN Platform and Ecosystem are coming soon! Stay tuned for updates.";
    if (t.indexOf('security') !== -1 || t.indexOf('cyber') !== -1) return "We offer threat assessment, account protection, secure system architecture, and vulnerability analysis.";
    return "I'm not sure I understand. For detailed assistance, please email kingmandigitalcybernetwork@gmail.com or WhatsApp +254111843716.";
  }
  send.addEventListener('click', function() {
    var text = input.value.trim();
    if (!text) return;
    addMessage(text, 'user');
    input.value = '';
    setTimeout(function() { addMessage(getBotResponse(text), 'bot'); }, 500);
  });
  input.addEventListener('keypress', function(e) { if (e.key === 'Enter') send.click(); });
})();
</script>
"""

# Page definitions: filename, title, heading, description
pages = [
    ("cybersecurity.html", "Cybersecurity Systems | KDCN", "Cybersecurity <span>Systems</span>", "Advanced protection systems for individuals and businesses."),
    ("infrastructure.html", "IT Infrastructure & Cloud | KDCN", "IT Infrastructure <span>& Cloud</span>", "Scalable cloud and infrastructure solutions."),
    ("software-development.html", "Software Development | KDCN", "Software <span>Development</span>", "Custom web platforms built for security and performance."),
    ("digital-consulting.html", "Digital Systems Consulting | KDCN", "Digital Systems <span>Consulting</span>", "Strategic advice for secure digital operations."),
    ("client-portal.html", "Client Portal | KDCN", "Client <span>Portal</span>", "Access your KDCN services and account."),
    ("platform-access.html", "Platform Access | KDCN", "Platform <span>Access</span>", "Login or register for the KDCN Platform."),
    ("ecosystem-overview.html", "Explore Ecosystem | KDCN", "Explore <span>Ecosystem</span>", "Discover the future KDCN ecosystem."),
    ("cookies.html", "Cookie Policy | KDCN", "Cookie <span>Policy</span>", "How KDCN uses cookies."),
    ("cookie-preferences.html", "Cookie Preferences | KDCN", "Cookie <span>Preferences</span>", "Manage your cookie settings."),
]

for filename, title, heading, description in pages:
    filepath = os.path.join('docs', filename)
    if os.path.exists(filepath):
        print(f"Skipping {filename} (exists)")
        continue
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{description}">
<link rel="icon" href="images/logo-transparent.png">
<style>
{base_css}
{dropdown_css}
</style>
</head>
<body>
{nav}
<header>
  <h1>{heading}</h1>
  <p>{description}</p>
</header>
<section>
  <p>This page is under construction. For more information, please <a href="contact.html" style="color:var(--accent);">contact us</a>.</p>
</section>
{footer}
{chat_widget}
<script>
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');
  if (hamburger && navMenu) {{
    hamburger.addEventListener('click', () => navMenu.classList.toggle('active'));
  }}
  const toggle = document.getElementById('theme-toggle');
  if (localStorage.getItem('theme') === 'light') {{
    document.body.classList.add('light');
    toggle.textContent = '☀️';
  }}
  toggle.addEventListener('click', () => {{
    document.body.classList.toggle('light');
    const isLight = document.body.classList.contains('light');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    toggle.textContent = isLight ? '☀️' : '🌙';
  }});
  // Mobile dropdown toggle
  document.querySelectorAll('.dropdown').forEach(item => {{
    item.addEventListener('click', function(e) {{
      if (window.innerWidth <= 768) {{
        e.preventDefault();
        this.classList.toggle('active');
      }}
    }});
  }});
</script>
</body>
</html>"""
    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Created {filename}")

print("Done creating missing pages.")
