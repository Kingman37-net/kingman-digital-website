import re, os

# Floating social icon patterns to remove
# 1. Inline style floating divs (index.html, resources.html)
pattern_inline = re.compile(r'<div style="position:fixed; bottom:20px; right:20px;.*?</div>\s*</div>', re.DOTALL)
# 2. Class-based floating social (resources.html also has .floating-social)
pattern_class = re.compile(r'<div class="floating-social">.*?</div>\s*</div>', re.DOTALL)
# More generic: any div with position:fixed and bottom:20px etc.
pattern_generic = re.compile(r'<div[^>]*style="[^"]*position:\s*fixed;\s*bottom:\s*20px[^"]*".*?</div>\s*</div>', re.DOTALL)

# Chat widget HTML/CSS/JS to insert
chat_widget = """
<!-- KDCN Chat Widget -->
<style>
  .kdcn-chat-btn {
    position: fixed;
    bottom: 25px;
    right: 25px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0b7fab, #00d1ff);
    border: none;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    color: #000;
    transition: transform 0.3s;
  }
  .kdcn-chat-btn:hover { transform: scale(1.1); }
  .kdcn-chat-panel {
    position: fixed;
    bottom: 95px;
    right: 25px;
    width: 320px;
    max-width: 90vw;
    height: 420px;
    max-height: 70vh;
    background: #0a1118;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    display: none;
    flex-direction: column;
    overflow: hidden;
    z-index: 1001;
  }
  .kdcn-chat-panel.active { display: flex; }
  .kdcn-chat-header {
    background: linear-gradient(135deg, #0b7fab, #00d1ff);
    padding: 15px;
    color: #000;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .kdcn-chat-header span { font-size: 1.1rem; }
  .kdcn-chat-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #000; }
  .kdcn-chat-body {
    flex: 1;
    padding: 15px;
    overflow-y: auto;
    color: #fff;
  }
  .kdcn-chat-message {
    margin-bottom: 12px;
    display: flex;
    flex-direction: column;
  }
  .kdcn-chat-message.bot { align-items: flex-start; }
  .kdcn-chat-message.user { align-items: flex-end; }
  .kdcn-chat-bubble {
    max-width: 80%;
    padding: 10px 15px;
    border-radius: 18px;
    background: rgba(255,255,255,0.1);
    font-size: 0.9rem;
    line-height: 1.4;
  }
  .kdcn-chat-message.user .kdcn-chat-bubble {
    background: #00d1ff;
    color: #000;
  }
  .kdcn-chat-input {
    display: flex;
    padding: 10px;
    background: rgba(0,0,0,0.2);
  }
  .kdcn-chat-input input {
    flex: 1;
    padding: 10px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.2);
    background: #fff;
    color: #000;
    outline: none;
  }
  .kdcn-chat-input button {
    margin-left: 10px;
    padding: 10px 20px;
    border-radius: 20px;
    border: none;
    background: #00d1ff;
    color: #000;
    font-weight: bold;
    cursor: pointer;
  }
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
    const btn = document.getElementById('kdcnChatBtn');
    const panel = document.getElementById('kdcnChatPanel');
    const close = document.getElementById('kdcnChatClose');
    const body = document.getElementById('kdcnChatBody');
    const input = document.getElementById('kdcnChatInput');
    const send = document.getElementById('kdcnChatSend');

    btn.addEventListener('click', () => panel.classList.toggle('active'));
    close.addEventListener('click', () => panel.classList.remove('active'));

    function addMessage(text, sender) {
      const msgDiv = document.createElement('div');
      msgDiv.className = 'kdcn-chat-message ' + sender;
      const bubble = document.createElement('div');
      bubble.className = 'kdcn-chat-bubble';
      bubble.textContent = text;
      msgDiv.appendChild(bubble);
      body.appendChild(msgDiv);
      body.scrollTop = body.scrollHeight;
    }

    function getBotResponse(userText) {
      const t = userText.toLowerCase();
      if (t.includes('hello') || t.includes('hi')) return "Hi there! How can I help you today?";
      if (t.includes('service') || t.includes('offer')) return "We provide Cybersecurity Systems, IT Infrastructure & Cloud, Software Development, and Digital Systems Consulting. Which one are you interested in?";
      if (t.includes('price') || t.includes('cost') || t.includes('fee')) return "Our pricing depends on the scope of the project. Please contact us via email or WhatsApp for a custom quote.";
      if (t.includes('contact') || t.includes('reach')) return "You can email us at kingmandigitalcybernetwork@gmail.com or WhatsApp +254111843716.";
      if (t.includes('location') || t.includes('where')) return "We are based in Embu, Kenya, serving clients globally.";
      if (t.includes('platform') || t.includes('ecosystem')) return "Our KDCN Platform and Ecosystem are coming soon! Stay tuned for updates.";
      if (t.includes('security') || t.includes('cyber')) return "We offer threat assessment, account protection, secure system architecture, and vulnerability analysis.";
      return "I'm not sure I understand. For detailed assistance, please email kingmandigitalcybernetwork@gmail.com or WhatsApp +254111843716.";
    }

    send.addEventListener('click', () => {
      const text = input.value.trim();
      if (!text) return;
      addMessage(text, 'user');
      input.value = '';
      setTimeout(() => {
        addMessage(getBotResponse(text), 'bot');
      }, 500);
    });

    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') send.click();
    });
  })();
</script>
"""

# Process all HTML files
for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
    with open(filename, 'r') as f:
        content = f.read()
    
    # Remove floating social icons (all possible patterns)
    content = pattern_inline.sub('', content)
    content = pattern_class.sub('', content)
    content = pattern_generic.sub('', content)
    # Also remove if there's a leftover closing div from removed blocks (safety)
    # content = content.replace('</div>\n</div>\n</section>', '</section>')
    
    # Insert chat widget before </body>
    content = content.replace('</body>', chat_widget + '\n</body>')
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f'Updated {filename}')
