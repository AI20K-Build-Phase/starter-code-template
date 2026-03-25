# Starter Code App

A basic template for building AI Agents in both **TypeScript** and **Python**. Choose your preferred language and start building.

## Structure

```
├── typescript/         # TypeScript starter
│   ├── src/
│   │   ├── agent.ts    # Main agent loop
│   │   ├── tools.ts    # Tool definitions
│   │   └── config.ts   # Configuration
│   ├── package.json
│   ├── tsconfig.json
│   └── .env.example
├── python/             # Python starter
│   ├── src/
│   │   ├── agent.py    # Main agent loop
│   │   ├── tools.py    # Tool definitions
│   │   └── config.py   # Configuration
│   ├── requirements.txt
│   └── .env.example
├── AGENTS.md           # AI agent rules (read before coding)
└── PROMPT_LOG.md       # Prompt log (must be updated per PR)
```

## Getting Started

### TypeScript

```bash
cd typescript
npm install
cp .env.example .env
# Fill in your API key in .env
npm start
# Or dev mode:
npm run dev
```

### Python

```bash
cd python
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

pip install -r requirements.txt
cp .env.example .env
# Fill in your API key in .env
python -m src.agent
```

## Important

Read [AGENTS.md](./AGENTS.md) carefully before you start coding.
Every PR **must** update [PROMPT_LOG.md](./PROMPT_LOG.md).
