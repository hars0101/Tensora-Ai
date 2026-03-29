# Tensora AI 🤖
### Autonomous Multi-Agent Execution Framework

> One prompt. Any app. Real actions. No hard-coded rules.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![React](https://img.shields.io/badge/Frontend-React-61DAFB.svg)](https://reactjs.org)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-green.svg)](https://langchain-ai.github.io/langgraph/)
[![MCP](https://img.shields.io/badge/Protocol-MCP-orange.svg)](https://modelcontextprotocol.io)
[![Docker](https://img.shields.io/badge/Deploy-Docker-2496ED.svg)](https://docker.com)
[![Zapier](https://img.shields.io/badge/Integrations-Zapier%201000%2B-FF4A00.svg)](https://zapier.com)

---

## 📹 Demo Video

> 🎥 **[Watch Full Demo on YouTube](https://youtu.be/Au-bGwkqBKE)**

*The demo shows Tensora AI executing Gmail, Google Calendar, Google Drive, and LinkedIn actions simultaneously from a single natural language prompt — with live real-time verification across all platforms.*

> **Note:** The demo video tests only 5 integrations for illustration. Tensora AI supports the **entire Zapier ecosystem of 1000+ applications** — any app on Zapier can be controlled via natural language through MCP.

---

## 🚀 What is Tensora AI?

Tensora AI is a **fully autonomous, multi-agent AI execution framework** that understands natural language commands and executes real-world tasks across your entire digital ecosystem — simultaneously, intelligently, and without hard-coded rules.

Unlike traditional automation tools (Zapier, Make, n8n) that require manual workflow building, Tensora AI uses an **LLM brain** to reason about your intent and autonomously plan, orchestrate, and execute multi-step actions across multiple platforms in a single prompt.

**Just tell it what you want. It figures out everything else.**

---

## ⚡ Real World Demo — One Prompt, Four Actions

Here's what Tensora AI executed from a **single natural language command:**

**Prompt:**
```
Create a file in Google Drive named harsha-now with the text "n8n is working". 
Schedule a meeting on 31 March 2026 about n8n servers from 4pm to 8pm IST. 
Send an email via Gmail to imadabathuniharsha@gmail.com about that I have made 
a working prototype regards Harsha. Post on LinkedIn about "n8n vs MCP".
```

**Results — all executed simultaneously:**

| Action | Tool | Status |
|--------|------|--------|
| Created Google Drive file "harsha-now" with exact content | `google_drive_create_file_from_text` | ✅ Success |
| Scheduled "n8n servers" meeting Mar 31, 4–8pm IST | `google_calendar_create_detailed_event` | ✅ Success |
| Sent email "Update: Working Prototype Developed" | `gmail_send_email` | ✅ Success |
| Published LinkedIn post about n8n vs MCP to 2,290 followers | `linkedin_create_share_update` | ✅ Success |

> This is not a mock. This is not a prototype. **Every action above is verifiable in real accounts.**
> These 4 are just examples — Tensora AI works with **any of the 1000+ apps on Zapier.**

---

## 🌐 Supported Integrations (1000+ via Zapier MCP)

Tensora AI can control **any app available on Zapier** through natural language. Here's a sample:

| Category | Apps |
|----------|------|
| 📧 Email | Gmail, Outlook, Yahoo Mail, SendGrid |
| 📅 Calendar | Google Calendar, Outlook Calendar, Calendly |
| 📁 Storage | Google Drive, Dropbox, OneDrive, Box |
| 💼 Social | LinkedIn, Twitter/X, Instagram, Facebook |
| 💬 Messaging | Slack, Discord, Microsoft Teams, Telegram |
| 📝 Productivity | Notion, Airtable, Trello, Asana, ClickUp |
| 🛒 E-Commerce | Shopify, WooCommerce, BigCommerce |
| 📊 Spreadsheets | Google Sheets, Excel, Smartsheet |
| 🎥 Meetings | Zoom, Google Meet, Microsoft Teams |
| 💰 Payments | Stripe, PayPal, Square |
| 🔔 CRM | HubSpot, Salesforce, Pipedrive |
| 🔗 And more | **1000+ apps total** |

---

## ✨ Key Features

### 🧠 Intelligent Intent Routing
Tensora AI automatically detects whether your input requires:
- **Chat mode** — Conversational responses, questions, explanations
- **Tool mode** — Real-world action execution across connected apps

No explicit mode switching. It just knows.

### 🤖 Multi-Agent Architecture
- **LangGraph** orchestrates complex multi-step workflows
- **MCP (Model Context Protocol)** handles all tool communication
- **Playwright** powers browser automation for web interactions
- Agents collaborate to complete tasks spanning multiple platforms simultaneously

### 🧬 Custom Fine-tuned LLM
- Fine-tuned on **Qwen 2.5 32B** (upgraded from LLaMA)
- Custom training using **LoRA/PEFT** for domain-specific reasoning
- Deployed on **Modal.com A10G GPU** for production-grade inference
- Optimized for **intent parsing** and **tool selection accuracy**

### 🔒 Confirmation-First Execution
Before taking any real-world action, Tensora AI:
1. Shows you a **detailed plan** of what it will do
2. Displays a **confidence score** (e.g., 95%)
3. Waits for your **approval** before executing
4. Reports **detailed results** for every action taken

### 🎙️ Voice Input Support
- Google Cloud Speech-to-Text integration
- Speak your commands naturally — Tensora AI handles the rest

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│              User Natural Language Input         │
│           (Text or Voice via Speech-to-Text)     │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│         Tensora AI Intent Parser                │
│    (Fine-tuned Qwen 2.5 32B via Modal GPU)      │
│                                                 │
│  Chat Intent? ──► Conversational Response       │
│  Tool Intent? ──► Multi-Agent Orchestration     │
└─────────────────────┬───────────────────────────┘
                      │ Tool Intent
                      ▼
┌─────────────────────────────────────────────────┐
│           LangGraph Orchestrator                │
│  • Plans multi-step execution                   │
│  • Assigns tasks to specialized agents          │
│  • Handles dependencies between actions         │
│  • Shows plan + confidence before executing     │
└──────┬──────────────┬──────────────┬────────────┘
       │              │              │
       ▼              ▼              ▼
┌──────────┐  ┌──────────────┐  ┌───────────────┐
│  Zapier  │  │  Playwright  │  │  REST APIs    │
│   MCP    │  │   Browser    │  │  (Custom)     │
│ 1000+Apps│  │  Automation  │  │               │
└──────┬───┘  └──────┬───────┘  └───────┬───────┘
       │              │                  │
       └──────────────┴──────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│         Real World Actions Executed             │
│  Gmail ✓  Calendar ✓  Drive ✓  LinkedIn ✓ ...  │
│         Any of 1000+ Zapier Apps ✓              │
└─────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Primary LLM | Qwen 2.5 32B (fine-tuned with LoRA/PEFT) |
| Fallback LLM | Claude 3.5 / Gemini Flash 2.5 |
| Orchestration | LangGraph |
| Tool Protocol | MCP (Model Context Protocol) |
| App Integrations | Zapier MCP (1000+ apps) |
| Browser Automation | Playwright |
| Frontend | React + Vite + Tailwind CSS |
| Backend | Python + FastAPI |
| Proxy Layer | Custom proxy.py |
| Auth & Database | Firebase + Firestore |
| Model Deployment | Modal.com (A10G GPU) |
| App Deployment | Docker + Vercel |
| Speech Input | Google Cloud Speech-to-Text |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker (optional but recommended)
- Zapier account (for MCP integrations)
- Firebase project (for auth)

### 1. Clone the Repository

```bash
git clone https://github.com/hars0101/Tensora-Ai.git
cd Tensora-Ai
```

### 2. Install Dependencies

```bash
# Python dependencies
pip install -r requirements.txt

# Frontend dependencies
npm install
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# AI Providers (use at least one)
GEMINI_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key          # optional fallback
ANTHROPIC_API_KEY=your_anthropic_key    # optional fallback

# Zapier MCP Integration
ZAPIER_MCP_URL=https://mcp.zapier.com/api/mcp/s/YOUR_KEY/mcp

# Firebase Auth
FIREBASE_API_KEY=your_firebase_key
FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id

# Google Cloud (for Speech-to-Text)
GOOGLE_APPLICATION_CREDENTIALS=server/gcp_key.json

# Modal (for custom LLM - optional)
MODAL_ENDPOINT=https://your-modal-endpoint.modal.run
```

### 4. Set Up Zapier MCP

1. Go to [mcp.zapier.com](https://mcp.zapier.com)
2. Create a new MCP server
3. Connect your apps (Gmail, Calendar, Drive, LinkedIn, etc.)
4. Copy your MCP server URL
5. In Tensora AI → ⚙️ Settings → MCP Webhook URL → paste → Save Settings

### 5. Run the Application

```bash
# Start backend
python start_backend.py

# Start frontend (new terminal)
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) 🎉

### Docker (Recommended)

```bash
docker build -t tensora-ai .
docker run -p 5173:5173 -p 8000:8000 tensora-ai
```

---

## ⚙️ Settings

Access via the ⚙️ icon in the UI:

| Setting | Description |
|---------|-------------|
| MCP Webhook URL | Your Zapier MCP server endpoint |
| AI Provider | Gemini, Claude, OpenAI, or Tensora (custom) |
| Auto Execute Plans | Skip confirmation, execute immediately |
| Enable Streaming | Real-time streaming responses |

---

## 📁 Project Structure

```
Tensora-Ai/
├── LLM/                          # Fine-tuning scripts and model configs
├── server/                       # Python FastAPI backend
│   ├── proxy.py                  # Main proxy + MCP handler
│   ├── intentParser.py           # LLM intent classification
│   ├── conversation_manager.py   # Chat history management
│   ├── html_formatter.py         # Response formatting
│   └── title_generator.py        # Chat title generation
├── App.jsx                       # Main React app
├── ChatHistory.jsx               # Chat history sidebar
├── ChatInput.jsx                 # Input component
├── ChatMessage.jsx               # Message rendering
├── LandingPage.jsx               # Landing page
├── MainApp.jsx                   # Core app layout
├── SettingsModal.jsx             # Settings panel
├── Welcome.jsx                   # Welcome screen
├── Dockerfile                    # Docker configuration
├── start_backend.py              # Backend entry point
├── requirements.txt              # Python dependencies
└── package.json                  # Node dependencies
```

---

## 🔧 How It Works — Step by Step

1. **You type or speak a command**
   > *"Schedule a Zoom meeting with John tomorrow at 3pm and send him a Slack message about it"*

2. **Intent Parser activates**
   Fine-tuned LLM classifies intent as `tool` (not `chat`)

3. **LangGraph plans execution**
   Breaks into: `zoom_create_meeting` + `slack_send_message`

4. **Plan shown to you**
   Full action plan with confidence score and JSON payload

5. **You approve**
   Click "Execute Plan" (or auto-execute if enabled)

6. **MCP executes via Zapier**
   Real API calls made across your connected apps

7. **Results reported**
   Detailed success/failure summary for every action

---

## 🌟 Tensora AI vs The Alternatives

| Feature | Zapier | Make/n8n | ChatGPT Plugins | **Tensora AI** |
|---------|--------|----------|-----------------|----------------|
| Natural language control | ❌ | ❌ | ✅ | ✅ |
| Multi-step from one prompt | ❌ | ❌ | Partial | ✅ |
| Custom fine-tuned LLM | ❌ | ❌ | ❌ | ✅ |
| No workflow building needed | ❌ | ❌ | ✅ | ✅ |
| 1000+ integrations | ✅ | ✅ | Limited | ✅ |
| Confirmation before execution | ❌ | ❌ | ❌ | ✅ |
| Open source | ❌ | Partial | ❌ | ✅ |
| Self-hostable | ❌ | ✅ | ❌ | ✅ |
| Voice input | ❌ | ❌ | ❌ | ✅ |

---

## 🗺️ Roadmap

- [x] Gmail, Calendar, Drive, LinkedIn automation
- [x] Zapier MCP with 1000+ app support
- [x] Custom Qwen 2.5 32B fine-tuned model
- [x] Voice input via Google Cloud Speech-to-Text
- [x] Docker deployment
- [ ] Mobile app (React Native)
- [ ] Multi-user workspace support
- [ ] Plugin marketplace for custom MCP tools
- [ ] Public release of fine-tuned model weights (pending copyright registration)

---

## 💡 The Story Behind Tensora AI

I'm a final-year B.Tech student (CSE-AIML) who spent **$200 of my own money** — leaving myself financially drained — to build something I genuinely believed in.

There were sleepless nights, dozens of failed experiments, broken APIs, GPU bills I couldn't afford, and moments where I wanted to quit.

But I kept going because I believe **AI should do things, not just talk about things.**

Tensora AI is proof that one determined person with a laptop can build production-grade agentic AI infrastructure.

---

## 🏆 Recognition & Achievements

- 🥇 **1st Prize — CODESPARK INDIA 2025** — National Level Hackathon — Prompt-Driven AI integrating Gemini, GPT & Groq — Best Innovation Award + Brand New Laptop
- 🥇 **1st Place among 100 Projects** — Smart Mirror Innovation — Best Innovation Award + ₹5,000 Cash Prize
- 🏅 **IIT Hackathon** — Smart Parking Space Identification System (YOLO + OpenCV)
- 🤝 **APSRTC Collaboration** — Real-world Driver Distraction Alert System for Andhra Pradesh State Road Transport Corporation
- 🎓 **Infosys Springboard Virtual Internship** — AI, ML & Web Development (3 Months)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

> **Note on Model Weights:** The custom fine-tuned Qwen 2.5 32B model weights are currently undergoing copyright registration and will be publicly released on Hugging Face upon completion.

---

## 👨‍💻 Author

**Imadabathuni Harsha Venkat** — AIML Engineer & Web Developer

[![Portfolio](https://img.shields.io/badge/Portfolio-iharsha.space-blue)](http://iharsha.space/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-harsha0101-0077B5)](https://www.linkedin.com/in/harsha0101)
[![Email](https://img.shields.io/badge/Email-imadabathuniharsha%40gmail.com-red)](mailto:imadabathuniharsha@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-hars0101-black)](https://github.com/hars0101)

---

<div align="center">

⭐ **If Tensora AI impressed you, please star this repo!** ⭐

*It means everything to an indie developer who put blood, sweat, and $200 into building this.*

**[⭐ Star this repo](https://github.com/hars0101/Tensora-Ai)**

</div>
