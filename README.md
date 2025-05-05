# 🌿 Amazon Rainforest Travel Guide (Claude Agent + MCP)

An AI-powered travel assistant connected to Claude via MCP, designed to help users explore the Amazon Rainforest — from planning routes to discovering nearby hotels and adventure spots.

---

## 🚀 Features

- 🌍 Get directions from any location to Manaus, Brazil
- 🏨 Discover nearby hotels using Geoapify
- 🥾 Find adventure spots like hikes and nature trails
- 🏛️ Explore food, monuments, and cultural sites
- ⚠️ Get essential travel precautions
- 🤖 Powered by Claude + FastMCP

---

## 🛠️ Tech Stack

- [Claude](https://claude.ai/) (Anthropic Desktop Client)
- [FastMCP](https://github.com/codebasics/FastMCP) for Claude tool registration
- Python + HTTPX + dotenv
- OpenTripMap, Geoapify, OpenRouteService APIs

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/Ajey95/MCP.git
   cd MCP
 2. **commands**:
     ```bash
     # On Windows.
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
       uv init projectname
       Create a virtual environment (optional but recommended):
       python -m venv venv
       source venv/bin/activate   # On Windows: venv\Scripts\activate
     
       Add your API keys in a .env file:
       ORS_API_KEY=your_openrouteservice_api_key
       GEOAPIFY_API_KEY=your_geoapify_api_key
       OPENTRIPMAP_API_KEY=your_opentripmap_api_key
 3. **mcp command**:
     ```bash
      install mcp 
      install mcp[cli]
 4. **Final**:
       ```bash
       pip install -r requirements.txt
       To run uv run mcp install file.py
       #Continue building!
---
## 🧠 Connecting Claude to Your MCP Server
Run your server:
  uv run mcp install file.py
Open the Claude desktop app

Click on Add Tool

Paste your MCP endpoint (shown in terminal, e.g., http://localhost:3333/.well-known/ai-plugin.json)

Claude will scan and install tools like:

- get_travel_route

- get_nearby_hotels

- get_adventure_spots

- get_monuments_and_food

- get_precautions

- greet_user
---
🗣️ Sample Prompts to Try in Claude
  - "What's the distance and travel time from Rio de Janeiro to the Amazon Rainforest?"
  
  - "Find top hotels near Manaus."
  
  - "Suggest some adventure spots near Manaus."
  
  - "What cultural sites can I visit in the Amazon?"
  
  - "Give me precautions before visiting the rainforest."
---
## 🤝 Contributing
Pull requests welcome. For major changes, please open an issue first.

## 📄 License
MIT


