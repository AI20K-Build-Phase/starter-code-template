import 'dotenv/config';

export const config = {
  anthropicApiKey: process.env.ANTHROPIC_API_KEY ?? '',
  openaiApiKey: process.env.OPENAI_API_KEY ?? '',
  defaultModel: process.env.DEFAULT_MODEL ?? 'claude-sonnet-4-20250514',
  logLevel: process.env.LOG_LEVEL ?? 'info',
} as const;
