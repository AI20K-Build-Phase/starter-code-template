/**
 * Tool definitions for the agent.
 * Add new tools by creating a function and registering it in the TOOLS map.
 */

import type Anthropic from '@anthropic-ai/sdk';

type ToolFn = (args: Record<string, string>) => Promise<string>;

interface ToolDef {
  fn: ToolFn;
  description: string;
  parameters: Record<string, string>;
}

async function searchWeb(args: Record<string, string>): Promise<string> {
  return `Search results for: ${args.query}`;
}

async function calculate(args: Record<string, string>): Promise<string> {
  try {
    // Simple math eval — for demo only, use a math library in production
    const fn = new Function('return ' + args.expression);
    return String(fn());
  } catch (e) {
    return `Error: ${e}`;
  }
}

async function fetchUrl(args: Record<string, string>): Promise<string> {
  try {
    const resp = await fetch(args.url, { signal: AbortSignal.timeout(10_000) });
    const text = await resp.text();
    return text.slice(0, 2000);
  } catch (e) {
    return `Error: ${e}`;
  }
}

// Tool registry
const TOOLS: Record<string, ToolDef> = {
  search_web: {
    fn: searchWeb,
    description: 'Search for information on the web',
    parameters: { query: 'string' },
  },
  calculate: {
    fn: calculate,
    description: 'Evaluate a math expression',
    parameters: { expression: 'string' },
  },
  fetch_url: {
    fn: fetchUrl,
    description: 'Fetch content from a URL',
    parameters: { url: 'string' },
  },
};

export function getToolSchemas(): Anthropic.Messages.Tool[] {
  return Object.entries(TOOLS).map(([name, tool]) => ({
    name,
    description: tool.description,
    input_schema: {
      type: 'object' as const,
      properties: Object.fromEntries(
        Object.entries(tool.parameters).map(([k, v]) => [k, { type: v, description: k }]),
      ),
      required: Object.keys(tool.parameters),
    },
  }));
}

export async function executeTool(name: string, args: Record<string, string>): Promise<string> {
  const tool = TOOLS[name];
  if (!tool) return `Tool '${name}' does not exist`;
  return tool.fn(args);
}
