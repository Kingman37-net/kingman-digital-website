/* =========================================================
   KDCN AI AGENT v2.0 — Intelligent Chat Assistant
   Kingman Digital Cyber Network
   ========================================================= */

(function () {
  "use strict";

  // =========================================================
  // 1. KNOWLEDGE BASE — Intents, Keywords, Responses
  // =========================================================
  const KDCN_KB = {
    greeting: {
      keywords: ["hi", "hello", "hey", "habari", "mambo", "sasa", "good morning", "good afternoon", "good evening"],
      response: "👋 Karibu KDCN! I'm the KDCN AI assistant. I can help with our services, pricing, security solutions, or connecting you with the right team member. What brings you here today?",
      quickReplies: ["Our Services", "Get a Quote", "Cybersecurity Help", "Talk to Human"]
    },

    services: {
      keywords: ["service", "offer", "what do you do", "solutions", "help with", "capabilities"],
      response: "KDCN provides four core service pillars:\n\n🛡️ **Cybersecurity Systems** — Threat assessment, account protection, security audits\n☁️ **IT Infrastructure & Cloud** — Scalable systems, firewalls, cloud deployment\n💻 **Software Development** — Custom web platforms, APIs, digital systems\n📊 **Digital Systems Consulting** — Strategy, governance, digital transformation\n\nWhich one would you like to explore?",
      quickReplies: ["Cybersecurity", "Cloud & IT", "Software Dev", "Consulting"]
    },

    cybersecurity: {
      keywords: ["cyber", "security", "threat", "hack", "protect", "audit", "vulnerability", "penetration", "pentest", "malware", "ransomware"],
      response: "🛡️ **KDCN Cybersecurity Services:**\n\n• Threat Assessment & Penetration Testing\n• Account & Identity Protection\n• Security Audits & Vulnerability Analysis\n• Secure System Architecture\n• Incident Response & Forensics\n• Security Awareness Training\n\nEvery engagement follows our mandate: *\"No data left unguarded. No system left unsafe.\"*\n\nWould you like a free initial security assessment?",
      quickReplies: ["Get Free Assessment", "Pricing", "Talk to Human"]
    },

    cloud: {
      keywords: ["cloud", "infrastructure", "server", "hosting", "aws", "google cloud", "firebase", "vps", "deploy", "backend"],
      response: "☁️ **KDCN Cloud & Infrastructure:**\n\n• Cloud Architecture Design (AWS, GCP, Firebase)\n• Firewall & Network Security\n• Scalable System Deployment\n• Google Workspace Setup\n• Backup & Disaster Recovery\n• 24/7 Monitoring\n\nWe build systems that scale with your business. What's your current setup?",
      quickReplies: ["Migrate to Cloud", "Get a Quote", "Talk to Human"]
    },

    software: {
      keywords: ["software", "development", "web", "website", "app", "platform", "code", "build", "custom", "api"],
      response: "💻 **KDCN Software Development:**\n\n• Custom Web Platforms\n• Client Portals & Dashboards\n• REST APIs & Integrations\n• E-commerce Systems\n• CMS & Content Platforms\n• Legacy System Modernization\n\nWe build with clean architecture, security-first design, and long-term maintainability.\n\nWhat kind of system are you looking to build?",
      quickReplies: ["Client Portal", "E-commerce", "API Integration", "Get a Quote"]
    },

    consulting: {
      keywords: ["consulting", "consultant", "strategy", "advice", "guidance", "transformation", "digital transformation"],
      response: "📊 **KDCN Digital Systems Consulting:**\n\n• Digital Transformation Strategy\n• Technology Roadmap Development\n• Governance Frameworks\n• Process Automation\n• System Architecture Review\n• IT Budget Optimization\n\nWe help organizations build strong digital foundations. Tell me about your challenge — I'll point you in the right direction.",
      quickReplies: ["Book a Consultation", "Our Approach", "Talk to Human"]
    },

    pricing: {
      keywords: ["price", "pricing", "cost", "fee", "quote", "charge", "rate", "how much", "budget"],
      response: "💰 **KDCN Pricing:**\n\nOur engagements are project-based and tailored to your specific needs. We offer:\n\n• **Fixed-scope projects** (cybersecurity audits, website builds)\n• **Retainer engagements** (ongoing IT & security support)\n• **Consulting packages** (strategy, governance)\n\nTo give you an accurate quote, I'd need to understand your scope. Would you like to:\n\n📞 Book a free 30-min consultation\n📧 Send us project details\n💬 Chat on WhatsApp",
      quickReplies: ["Book Consultation", "Email Project Details", "WhatsApp Us"]
    },

    contact: {
      keywords: ["contact", "reach", "email", "phone", "call", "whatsapp", "talk", "human", "speak"],
      response: "📬 **Reach KDCN:**\n\n📧 Email: info@kingmandigital.co.ke\n📞 Phone: +254 111 843 716\n💬 WhatsApp: +254 111 843 716\n📍 Location: Manyatta, Embu, Kenya 🇰🇪\n🌐 Website: www.kingmandigital.co.ke\n\nOur team responds within a few hours during business hours (Mon–Fri, 8am–6pm EAT).",
      quickReplies: ["WhatsApp Now", "Email Us", "Book Consultation"]
    },

    location: {
      keywords: ["location", "where", "office", "address", "based", "from", "kenya", "embu", "nairobi"],
      response: "📍 **KDCN Location:**\n\nWe're headquartered in **Manyatta, Embu, Kenya** 🇰🇪 — but we serve clients globally.\n\nOur work spans Kenya, East Africa, and international clients across Africa, Europe, and Asia.",
      quickReplies: ["Contact Us", "Our Services", "Talk to Human"]
    },

    about: {
      keywords: ["about", "who are you", "company", "founded", "founder", "team", "who owns", "kdcn"],
      response: "🏢 **About KDCN:**\n\nKingman Digital Cyber Network (KDCN) is a Kenya-based digital systems organization founded by **CTO KINGMAN KE**.\n\nOur mission: Build secure, resilient, and scalable digital systems for organizations across Africa and beyond.\n\nOur mandate: *\"No data left unguarded. No system left unsafe.\"*\n\nWould you like to learn more about our approach?",
      quickReplies: ["Our Approach", "Leadership", "Our Services"]
    },

    platform: {
      keywords: ["platform", "portal", "dashboard", "login", "client area", "kdcn platform"],
      response: "🖥️ **KDCN Platform:**\n\nThe KDCN Platform is our operational core — currently in active development. It will offer:\n\n• Client Portal (projects, invoices, tickets)\n• Secure Dashboards\n• Service Management\n• Document Vault\n• Real-time Support\n\nWould you like early access when we launch?",
      quickReplies: ["Get Early Access", "Learn More", "Contact Us"]
    },

    security_concern: {
      keywords: ["hacked", "breach", "compromised", "urgent", "emergency", "attacked", "stolen", "leaked"],
      response: "🚨 **If you're experiencing a security incident, contact us immediately:**\n\n📞 **Emergency Line:** +254 111 843 716\n📧 **Urgent Email:** info@kingmandigital.co.ke\n\nInclude:\n• What happened\n• When it happened\n• Systems affected\n\nOur incident response team is on standby. Don't delay — every minute matters in a breach.",
      quickReplies: ["Call Now", "WhatsApp Emergency"]
    },

    careers: {
      keywords: ["career", "job", "hiring", "work", "internship", "vacancy", "apply", "position"],
      response: "🎯 **Careers at KDCN:**\n\nWe're always looking for talented people in:\n\n• Cybersecurity\n• Software Engineering\n• Cloud Infrastructure\n• Digital Consulting\n\nVisit our careers page or send your CV to info@kingmandigital.co.ke with the role you're interested in.",
      quickReplies: ["View Careers Page", "Send CV"]
    },

    partnership: {
      keywords: ["partner", "partnership", "collaborate", "reseller", "affiliate", "integration"],
      response: "🤝 **Partnership Opportunities:**\n\nKDCN is open to partnerships with:\n\n• Technology providers\n• Consulting firms\n• Educational institutions\n• Resellers & integrators\n• NGOs and development organizations\n\nTell me a bit about your organization and what kind of partnership you're exploring.",
      quickReplies: ["Email Partnership Team", "Book a Call"]
    },

    thanks: {
      keywords: ["thank", "thanks", "asante", "appreciate", "helpful"],
      response: "🙏 Karibu sana! If you need anything else — services, pricing, or just have a question — I'm here. \n\nWould you like me to connect you with our team for a deeper conversation?",
      quickReplies: ["Yes, Connect Me", "No Thanks", "Our Services"]
    },

    goodbye: {
      keywords: ["bye", "goodbye", "kwaheri", "see you", "later", "exit"],
      response: "👋 Kwaheri! Thanks for chatting with KDCN. \n\nRemember: *\"No data left unguarded. No system left unsafe.\"*\n\nYou can reach us anytime at info@kingmandigital.co.ke or WhatsApp +254 111 843 716.",
      quickReplies: ["Start New Chat"]
    }
  };

  // =========================================================
  // 2. CONVERSATION STATE
  // =========================================================
  const STATE = {
    lastIntent: null,
    turnCount: 0,
    userName: null,
    userEmail: null,
    leadCaptured: false,
    startedAt: Date.now()
  };

  // =========================================================
  // 3. INTENT DETECTION (Weighted Keyword Matching)
  // =========================================================
  function detectIntent(text) {
    const t = text.toLowerCase().trim();
    let bestIntent = null;
    let bestScore = 0;

    for (const [intent, data] of Object.entries(KDCN_KB)) {
      let score = 0;
      for (const kw of data.keywords) {
        if (t.includes(kw)) {
          // Longer keywords = higher weight
          score += kw.length;
          // Exact word match bonus
          const regex = new RegExp("\\b" + kw + "\\b", "i");
          if (regex.test(t)) score += 5;
        }
      }
      if (score > bestScore) {
        bestScore = score;
        bestIntent = intent;
      }
    }

    return bestScore > 0 ? bestIntent : null;
  }

  // =========================================================
  // 4. EMAIL DETECTION
  // =========================================================
  function extractEmail(text) {
    const match = text.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/);
    return match ? match[0] : null;
  }

  // =========================================================
  // 5. DOM SETUP
  // =========================================================
  function buildWidget() {
    const html = `
      <style>
        .kdcn-agent-btn {
          position: fixed; bottom: 25px; right: 25px;
          width: 64px; height: 64px; border-radius: 50%;
          background: linear-gradient(135deg, #0b7fab, #00d1ff);
          border: none; cursor: pointer;
          box-shadow: 0 8px 24px rgba(0,209,255,0.4), 0 0 0 0 rgba(0,209,255,0.5);
          z-index: 1000; display: flex; align-items: center; justify-content: center;
          font-size: 28px; color: #fff;
          transition: transform 0.3s, box-shadow 0.3s;
          animation: kdcn-pulse 2.5s infinite;
        }
        .kdcn-agent-btn:hover { transform: scale(1.1); }
        .kdcn-agent-btn.badge::after {
          content: "1"; position: absolute; top: -4px; right: -4px;
          width: 22px; height: 22px; background: #ff3b30; color: #fff;
          border-radius: 50%; font-size: 12px; font-weight: 700;
          display: flex; align-items: center; justify-content: center;
          border: 2px solid #0a1118;
        }
        @keyframes kdcn-pulse {
          0%, 100% { box-shadow: 0 8px 24px rgba(0,209,255,0.4), 0 0 0 0 rgba(0,209,255,0.5); }
          50% { box-shadow: 0 8px 24px rgba(0,209,255,0.4), 0 0 0 12px rgba(0,209,255,0); }
        }

        .kdcn-agent-panel {
          position: fixed; bottom: 100px; right: 25px;
          width: 380px; max-width: calc(100vw - 30px);
          height: 560px; max-height: calc(100vh - 130px);
          background: #0a1118;
          border: 1px solid rgba(0,209,255,0.2);
          border-radius: 20px;
          box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 40px rgba(0,209,255,0.1);
          display: none; flex-direction: column;
          overflow: hidden; z-index: 1001;
          font-family: 'Segoe UI', system-ui, sans-serif;
        }
        .kdcn-agent-panel.active { display: flex; animation: kdcn-slide 0.3s ease; }
        @keyframes kdcn-slide {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }

        .kdcn-agent-head {
          background: linear-gradient(135deg, #0b7fab, #00d1ff);
          padding: 16px 18px; color: #000;
          display: flex; justify-content: space-between; align-items: center;
        }
        .kdcn-agent-head-info { display: flex; align-items: center; gap: 12px; }
        .kdcn-agent-avatar {
          width: 42px; height: 42px; border-radius: 50%;
          background: rgba(0,0,0,0.15); display: flex;
          align-items: center; justify-content: center;
          font-size: 22px;
        }
        .kdcn-agent-name { font-weight: 800; font-size: 1.05rem; line-height: 1.2; }
        .kdcn-agent-status {
          font-size: 0.75rem; font-weight: 500; opacity: 0.85;
          display: flex; align-items: center; gap: 6px;
        }
        .kdcn-agent-status::before {
          content: ""; width: 8px; height: 8px; background: #00ff88;
          border-radius: 50%; box-shadow: 0 0 8px #00ff88;
          animation: kdcn-blink 2s infinite;
        }
        @keyframes kdcn-blink { 50% { opacity: 0.4; } }
        .kdcn-agent-close {
          background: rgba(0,0,0,0.15); border: none; width: 32px; height: 32px;
          border-radius: 50%; font-size: 20px; cursor: pointer; color: #000;
          display: flex; align-items: center; justify-content: center;
          transition: background 0.2s;
        }
        .kdcn-agent-close:hover { background: rgba(0,0,0,0.3); }

        .kdcn-agent-body {
          flex: 1; padding: 18px; overflow-y: auto;
          color: #fff; scroll-behavior: smooth;
        }
        .kdcn-agent-body::-webkit-scrollbar { width: 6px; }
        .kdcn-agent-body::-webkit-scrollbar-thumb {
          background: rgba(0,209,255,0.3); border-radius: 3px;
        }

        .kdcn-agent-msg {
          margin-bottom: 14px; display: flex; flex-direction: column;
          animation: kdcn-fade 0.3s ease;
        }
        @keyframes kdcn-fade {
          from { opacity: 0; transform: translateY(8px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .kdcn-agent-msg.bot { align-items: flex-start; }
        .kdcn-agent-msg.user { align-items: flex-end; }

        .kdcn-agent-bubble {
          max-width: 85%; padding: 11px 15px;
          border-radius: 16px;
          background: rgba(255,255,255,0.08);
          font-size: 0.9rem; line-height: 1.55;
          white-space: pre-wrap; word-wrap: break-word;
        }
        .kdcn-agent-msg.bot .kdcn-agent-bubble {
          border-bottom-left-radius: 4px;
          border: 1px solid rgba(0,209,255,0.15);
        }
        .kdcn-agent-msg.user .kdcn-agent-bubble {
          background: linear-gradient(135deg, #0b7fab, #00d1ff);
          color: #000; font-weight: 500;
          border-bottom-right-radius: 4px;
        }
        .kdcn-agent-bubble strong { color: #00d1ff; }
        .kdcn-agent-msg.user .kdcn-agent-bubble strong { color: #000; }
        .kdcn-agent-time {
          font-size: 0.68rem; color: #6c7a85;
          margin-top: 4px; padding: 0 4px;
        }

        .kdcn-agent-typing {
          display: flex; gap: 4px; padding: 12px 16px;
          background: rgba(255,255,255,0.08);
          border-radius: 16px; border-bottom-left-radius: 4px;
          border: 1px solid rgba(0,209,255,0.15);
          width: fit-content;
        }
        .kdcn-agent-typing span {
          width: 7px; height: 7px; background: #00d1ff;
          border-radius: 50%; animation: kdcn-typing 1.4s infinite;
        }
        .kdcn-agent-typing span:nth-child(2) { animation-delay: 0.2s; }
        .kdcn-agent-typing span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes kdcn-typing {
          0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
          30% { transform: translateY(-6px); opacity: 1; }
        }

        .kdcn-agent-quick {
          display: flex; flex-wrap: wrap; gap: 8px;
          margin: 8px 0 16px 0;
        }
        .kdcn-agent-quick button {
          background: rgba(0,209,255,0.1);
          border: 1px solid rgba(0,209,255,0.4);
          color: #00d1ff; padding: 8px 14px;
          border-radius: 20px; font-size: 0.82rem;
          font-weight: 600; cursor: pointer;
          transition: all 0.2s; font-family: inherit;
        }
        .kdcn-agent-quick button:hover {
          background: rgba(0,209,255,0.25);
          transform: translateY(-1px);
        }

        .kdcn-agent-input-wrap {
          display: flex; padding: 12px;
          background: rgba(0,0,0,0.3);
          border-top: 1px solid rgba(0,209,255,0.1);
          gap: 8px; align-items: center;
        }
        .kdcn-agent-input {
          flex: 1; padding: 12px 16px;
          border-radius: 24px;
          border: 1px solid rgba(255,255,255,0.12);
          background: rgba(255,255,255,0.05);
          color: #fff; outline: none;
          font-size: 0.9rem; font-family: inherit;
          transition: border 0.2s;
        }
        .kdcn-agent-input:focus {
          border-color: #00d1ff;
          background: rgba(0,209,255,0.05);
        }
        .kdcn-agent-input::placeholder { color: #6c7a85; }
        .kdcn-agent-send {
          width: 42px; height: 42px; border-radius: 50%;
          border: none; background: linear-gradient(135deg, #0b7fab, #00d1ff);
          color: #000; font-size: 18px; cursor: pointer;
          display: flex; align-items: center; justify-content: center;
          transition: transform 0.2s;
        }
        .kdcn-agent-send:hover { transform: scale(1.08); }
        .kdcn-agent-send:disabled {
          opacity: 0.4; cursor: not-allowed; transform: none;
        }

        .kdcn-agent-footer {
          text-align: center; padding: 6px 12px 10px;
          font-size: 0.7rem; color: #6c7a85;
          background: rgba(0,0,0,0.3);
        }
        .kdcn-agent-footer a { color: #00d1ff; text-decoration: none; }

        @media (max-width: 480px) {
          .kdcn-agent-panel {
            width: calc(100vw - 20px);
            right: 10px; bottom: 90px;
            height: calc(100vh - 120px);
            max-height: 600px;
          }
          .kdcn-agent-btn { bottom: 20px; right: 20px; width: 58px; height: 58px; }
        }
      </style>

      <button class="kdcn-agent-btn" id="kdcnAgentBtn" aria-label="Chat with KDCN AI">💬</button>

      <div class="kdcn-agent-panel" id="kdcnAgentPanel" role="dialog" aria-label="KDCN AI Chat">
        <div class="kdcn-agent-head">
          <div class="kdcn-agent-head-info">
            <div class="kdcn-agent-avatar">🐺</div>
            <div>
              <div class="kdcn-agent-name">KDCN Assistant</div>
              <div class="kdcn-agent-status">Online — AI-powered</div>
            </div>
          </div>
          <button class="kdcn-agent-close" id="kdcnAgentClose" aria-label="Close chat">&times;</button>
        </div>
        <div class="kdcn-agent-body" id="kdcnAgentBody"></div>
        <div class="kdcn-agent-input-wrap">
          <input
            type="text"
            class="kdcn-agent-input"
            id="kdcnAgentInput"
            placeholder="Ask me anything about KDCN..."
            autocomplete="off"
            aria-label="Type your message"
          >
          <button class="kdcn-agent-send" id="kdcnAgentSend" aria-label="Send message">➤</button>
        </div>
        <div class="kdcn-agent-footer">
          Powered by <a href="https://www.kingmandigital.co.ke/"

target="_blank">KDCN AI</a> • <a href="contact.html">Talk to Human</a>
        </div>
      </div>
    `;

    const container = document.createElement("div");
    container.innerHTML = html;
    document.body.appendChild(container);
  }

  // =========================================================
  // 6. UI HELPERS
  // =========================================================
  function getTime() {
    return new Date().toLocaleTimeString("en-KE", { hour: "2-digit", minute: "2-digit" });
  }

  function scrollBottom() {
    const body = document.getElementById("kdcnAgentBody");
    body.scrollTop = body.scrollHeight;
  }

  function addMessage(text, sender, quickReplies) {
    const body = document.getElementById("kdcnAgentBody");

    // Convert **bold** markdown
    const formatted = text.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

    const msg = document.createElement("div");
    msg.className = "kdcn-agent-msg " + sender;
    msg.innerHTML = `
      <div class="kdcn-agent-bubble">${formatted}</div>
      <div class="kdcn-agent-time">${getTime()}</div>
    `;
    body.appendChild(msg);

    // Remove old quick replies
    body.querySelectorAll(".kdcn-agent-quick").forEach(q => q.remove());

    if (quickReplies && quickReplies.length) {
      const q = document.createElement("div");
      q.className = "kdcn-agent-quick";
      quickReplies.forEach(label => {
        const btn = document.createElement("button");
        btn.textContent = label;
        btn.onclick = () => {
          handleUserInput(label);
        };
        q.appendChild(btn);
      });
      body.appendChild(q);
    }

    scrollBottom();
  }

  function showTyping() {
    const body = document.getElementById("kdcnAgentBody");
    const t = document.createElement("div");
    t.className = "kdcn-agent-msg bot";
    t.id = "kdcnTypingIndicator";
    t.innerHTML = `<div class="kdcn-agent-typing"><span></span><span></span><span></span></div>`;
    body.appendChild(t);
    scrollBottom();
  }

  function hideTyping() {
    const t = document.getElementById("kdcnTypingIndicator");
    if (t) t.remove();
  }

  // =========================================================
  // 7. AGENT LOGIC
  // =========================================================
  function getAgentResponse(userText) {
    STATE.turnCount++;

    // Check email capture first
    const email = extractEmail(userText);
    if (email && !STATE.leadCaptured) {
      STATE.userEmail = email;
      STATE.leadCaptured = true;
      return {
        text: "✅ Got it! I've noted your email: **" + email + "**\n\nOur team will reach out within a few hours. In the meantime, is there anything specific you'd like to know about our services?",
        quickReplies: ["Our Services", "Pricing", "Talk on WhatsApp"]
      };
    }

    // Detect intent
    const intent = detectIntent(userText);

    // No intent — but we have context
    if (!intent) {
      // Try to recover with lastIntent context
      if (STATE.lastIntent === "pricing") {
        STATE.lastIntent = null;
        return {
          text: "I want to give you an accurate quote — could you share a bit about your project? \n\n📧 Or email us directly at **info@kingmandigital.co.ke** with details.",
          quickReplies: ["Email Us", "Book a Call", "WhatsApp"]
        };
      }
      return {
        text: "I want to make sure I give you the right answer. Could you rephrase that, or pick one of these topics?",
        quickReplies: ["Our Services", "Pricing", "Cybersecurity", "Talk to Human"]
      };
    }

    // Special: capture email after pricing
    if (STATE.lastIntent === "pricing" && intent !== "contact") {
      STATE.lastIntent = intent;
      return {
        text: KDCN_KB[intent].response,
        quickReplies: KDCN_KB[intent].quickReplies
      };
    }

    STATE.lastIntent = intent;
    return {
      text: KDCN_KB[intent].response,
      quickReplies: KDCN_KB[intent].quickReplies
    };
  }

  function handleUserInput(text) {
    if (!text || !text.trim()) return;

    addMessage(text, "user");
    const input = document.getElementById("kdcnAgentInput");
    if (input) input.value = "";

    showTyping();

    // Simulate natural typing delay
    const delay = 500 + Math.random() * 700;

    setTimeout(() => {
      hideTyping();
      const response = getAgentResponse(text);
      addMessage(response.text, "bot", response.quickReplies);
    }, delay);
  }

  // =========================================================
  // 8. INIT
  // =========================================================
  function init() {
    buildWidget();

    const btn = document.getElementById("kdcnAgentBtn");
    const panel = document.getElementById("kdcnAgentPanel");
    const close = document.getElementById("kdcnAgentClose");
    const input = document.getElementById("kdcnAgentInput");
    const send = document.getElementById("kdcnAgentSend");

    // Welcome message
    addMessage(
      "👋 **Karibu KDCN!** I'm your AI assistant.\n\nI can help you with:\n• Our services & solutions\n• Pricing & quotes\n• Security concerns\n• Connecting with our team\n\nWhat can I help you with today?",
      "bot",
      ["Our Services", "Pricing", "Cybersecurity", "Talk to Human"]
    );

    btn.addEventListener("click", () => {
      panel.classList.toggle("active");
      btn.classList.remove("badge");
      if (panel.classList.contains("active")) {
        setTimeout(() => input.focus(), 300);
      }
    });

    close.addEventListener("click", () => {
      panel.classList.remove("active");
    });

    send.addEventListener("click", () => {
      handleUserInput(input.value.trim());
    });

    input.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        handleUserInput(input.value.trim());
      }
    });

    // Show badge after 8 seconds if not opened
    setTimeout(() => {
      if (!panel.classList.contains("active")) {
        btn.classList.add("badge");
      }
    }, 8000);
  }

  // Run on DOM ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
