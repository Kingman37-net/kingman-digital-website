import os, re

widget = """
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

  btn.addEventListener('click', function() {
    panel.classList.toggle('active');
  });
  close.addEventListener('click', function() {
    panel.classList.remove('active');
  });

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
    setTimeout(function() {
      addMessage(getBotResponse(text), 'bot');
    }, 500);
  });

  input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') send.click();
  });
})();
</script>
"""

for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
    with open(filename, 'r') as f:
        content = f.read()
    content = re.sub(r'<!-- KDCN Chat Widget -->.*?</script>', '', content, flags=re.DOTALL)
    content = content.replace('</body>', widget + '\n</body>')
    with open(filename, 'w') as f:
        f.write(content)
    print(f'Updated {filename}')
