/**
 * Basic agent loop using the Anthropic Claude API.
 * Receives user input, calls tools as needed, and returns results.
 */

import Anthropic from '@anthropic-ai/sdk';
import * as readline from 'node:readline';
import { config } from './config.js';
import { getToolSchemas, executeTool } from './tools.js';

const SYSTEM_PROMPT = `You are an intelligent AI assistant.
You can use the provided tools to complete tasks.
Think step by step and use tools when necessary.`;

function createAgent(): Anthropic {
  if (!config.anthropicApiKey) {
    throw new Error('ANTHROPIC_API_KEY is not configured. Check your .env file');
  }
  return new Anthropic({ apiKey: config.anthropicApiKey });
}

async function runAgentLoop(
  client: Anthropic,
  userInput: string,
  maxTurns = 10,
): Promise<string> {
  const messages: Anthropic.Messages.MessageParam[] = [
    { role: 'user', content: userInput },
  ];
  const tools = getToolSchemas();

  for (let turn = 0; turn < maxTurns; turn++) {
    console.log(`  [turn ${turn + 1}/${maxTurns}]`);

    const response = await client.messages.create({
      model: config.defaultModel,
      max_tokens: 4096,
      system: SYSTEM_PROMPT,
      tools,
      messages,
    });

    // If agent stops (no more tool calls)
    if (response.stop_reason === 'end_turn') {
      return response.content
        .filter((b): b is Anthropic.Messages.TextBlock => b.type === 'text')
        .map((b) => b.text)
        .join('');
    }

    // Handle tool calls
    const toolUseBlocks = response.content.filter(
      (b): b is Anthropic.Messages.ToolUseBlock => b.type === 'tool_use',
    );

    if (toolUseBlocks.length === 0) {
      return response.content
        .filter((b): b is Anthropic.Messages.TextBlock => b.type === 'text')
        .map((b) => b.text)
        .join('');
    }

    const toolResults: Anthropic.Messages.ToolResultBlockParam[] = [];

    for (const block of toolUseBlocks) {
      console.log(`  Tool: ${block.name}(${JSON.stringify(block.input)})`);
      const result = await executeTool(block.name, block.input as Record<string, string>);
      console.log(`  Result: ${result.slice(0, 200)}`);
      toolResults.push({
        type: 'tool_result',
        tool_use_id: block.id,
        content: result,
      });
    }

    messages.push({ role: 'assistant', content: response.content });
    messages.push({ role: 'user', content: toolResults });
  }

  return 'Agent reached the maximum number of processing turns.';
}

async function main() {
  const client = createAgent();

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  console.log('Agentic App (type "quit" to exit)');
  console.log('-'.repeat(50));

  const askQuestion = () => {
    rl.question('\nYou: ', async (input) => {
      const trimmed = input.trim();
      if (!trimmed || ['quit', 'exit', 'q'].includes(trimmed.toLowerCase())) {
        console.log('Bye!');
        rl.close();
        return;
      }

      try {
        const response = await runAgentLoop(client, trimmed);
        console.log(`\nAgent: ${response}`);
      } catch (e) {
        console.error(`\nError: ${e}`);
      }

      askQuestion();
    });
  };

  askQuestion();
}

main();
