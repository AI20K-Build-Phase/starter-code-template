# Agent Guidelines

## Mandatory Rules When Using AI Coding Agents

### 1. Record Your Prompt Log

**Every time you create a Pull Request, you MUST record all prompts you used.**

Create or update the `PROMPT_LOG.md` file in the root directory with this format:

```markdown
## PR #<number>: <title>

### Prompt 1
> <the prompt you sent to the AI agent>

**Result:** <brief description of what the AI did>

### Prompt 2
> <next prompt>

**Result:** <brief description>

...
```

### 2. Pull Request Requirements

- **Title**: Short description of the change
- **Description**: Must include:
  - Summary of changes
  - Number of prompts used
  - Link to the corresponding section in `PROMPT_LOG.md`
- **PROMPT_LOG.md**: Must be updated in the same PR

### 3. Rules for AI Agents

If you are an AI coding agent (Claude Code, Cursor, GitHub Copilot, etc.):

- **DO NOT** create a PR without a prompt log
- **MUST** automatically remind the user to record prompts if they forget
- **MUST** add a new section to `PROMPT_LOG.md` before committing
- **MUST** include the total number of prompts in the PR description
- PR description format:

```
## Summary
<description of changes>

## Prompt Log
- Total prompts: <count>
- See: [PROMPT_LOG.md](./PROMPT_LOG.md#pr-<number>)

## Changes
- <list of changed files>
```
