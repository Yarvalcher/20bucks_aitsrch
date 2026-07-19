# $20 AI Development Tools Comparison — Complete Data Reference

> Last verified: 2026-07-19
> Use case: Full-stack React + FastAPI development on a $20/month budget

---

## Google Antigravity 2.0

- **Vendor:** Google
- **Price:** $19.99/mo (AI Pro) | $100/mo (AI Ultra 5×) | $200/mo (AI Ultra 20×)
- **Effective $20 capacity:** 1,200–1,600 tasks/month
- **Cost per task:** ~$0.014

### Models
| Model | Notes |
|-------|-------|
| Gemini 3.5 Flash | Primary — 4× faster than 3.1 Pro, outperforms it on coding benchmarks |
| Gemini 3.1 Pro | Deep reasoning fallback |
| Claude Opus 4.6 | Available on Ultra tiers |
| GPT-OSS-120b | Open-source tier |

### Interfaces
- **CLI:** Antigravity CLI (Go-based, replaced Gemini CLI June 18, 2026)
- **IDE:** Standalone desktop app (agent-first workspace)
- **SDK:** Antigravity SDK for custom agent workflows
- **Web:** Yes (browser-based workspace)

### Architecture
- Multi-agent workspace: Manager Agent coordinates parallel sub-agents
- 5 components: Desktop app, CLI, SDK, Managed Agents API, Enterprise path
- Sub-agents can work simultaneously (one writes FastAPI schemas while another generates React views)

### Benchmarks
- Gemini 3.5 Flash outperforms 3.1 Pro across almost all coding benchmarks
- No published SWE-Bench Verified score for the platform itself

### Metering
- AI Credit Pool with Tiered Rate Windows
- Free tier: unlimited basic commands, severe throttling on multi-agent
- Pro ($19.99): mandatory for multi-agent execution loops

### $20 Budget Behavior
- **Scale resilience:** 85% (large native context windows absorb growing projects well)
- **Catch:** Free tier is heavily throttled; Pro mandatory for real dev work
- **Strength:** Parallel sub-agents mean you can scaffold an entire project in one session

### Sources
- https://vibecoding.app/blog/google-antigravity-pricing-2026
- https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/
- https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/

---

## Kimi K2.7 Code

- **Vendor:** Moonshot AI
- **Price:** Pay-as-you-go (CLI is free, MIT license)
- **Effective $20 capacity:** 600–1,000 tasks/month
- **Cost per task:** ~$0.025

### Models
| Model | Params | Context | Notes |
|-------|--------|---------|-------|
| Kimi K2.7 Code | 1T MoE (32B active) | 256K | Primary coding model |
| Kimi K2.6 | 1T MoE | 256K | Previous gen, cheaper |
| Kimi K3 | TBD | 256K | Open weights shipping late Jul 2026 |

### Pricing (API tokens)
| Type | Cost per 1M tokens |
|------|-------------------|
| Input (cache miss) | $0.95 |
| Input (cache hit) | $0.19 (80% discount) |
| Output (standard) | $4.00 |
| Output (high-speed) | $8.00 |

### Interfaces
- **CLI:** Kimi Code CLI (TypeScript, MIT, distributed via npm)
- **IDE:** VS Code, Zed, JetBrains via Agent Client Protocol (ACP)
- **Web:** Kimi web app (chat + agent)
- **Subagents:** Built-in coder, explore, plan agents in isolated contexts

### Architecture
- MoE (Mixture-of-Experts): activates only 32B of 1T parameters per task
- 256K context window tuned for repository-scale codebases
- Agent Swarm: coordinates up to 100 parallel sub-agents (4.5× speedup)
- Native MCP (Model Context Protocol) configuration via `/mcp-config`

### Benchmarks
| Benchmark | Score |
|-----------|-------|
| SWE-Bench Verified | 76.8% |

### Metering
- Pure token consumption (per million tokens)
- No subscription required — CLI is free, you pay API costs only
- Open weights available: run locally for $0

### $20 Budget Behavior
- **Scale resilience:** 92% (prompt caching makes repeated context 80% cheaper)
- **Catch:** First-pass of new files costs full rate; subsequent iterations are heavily cached
- **Strength:** Gets MORE cost-efficient as project grows (opposite of context snowball)

### Subscription Tiers (Kimi Platform)
| Tier | Price | Includes |
|------|-------|----------|
| Adagio (Free) | $0 | Basic chat, no Kimi Code, ~6 agent credits |
| Moderato | $19/mo | Kimi Code access, more credits |
| Allegretto | $39/mo | Higher limits |
| Allegro | $99/mo | Agent Swarm access |
| Vivace | $199/mo | Maximum capacity |

*Note: These tiers do NOT include API calls — API is billed separately.*

### Sources
- https://www.kimi.com/resources/kimi-k2-7-code-pricing
- https://github.com/MoonshotAI/kimi-code
- https://www.marktechpost.com/2026/06/06/moonshot-ai-releases-kimi-code-cli-a-terminal-ai-coding-agent-built-in-typescript-for-next-gen-agents/
- https://kimik2ai.com/pricing/
- https://medium.com/@tentenco/kimi-k2-6-kimi-code-review-saving-88-coding-costs-b7e8c5eaf5f1

---

## Cursor AI

- **Vendor:** Anysphere
- **Price:** $20/mo (Pro)
- **Effective $20 capacity:** 250–500 tasks/month
- **Cost per task:** ~$0.053

### Models
| Model | Role |
|-------|------|
| Composer 2.5 | Primary in-house model (shipped May 18, 2026) |
| Claude Sonnet 4.6 | Fallback for complex reasoning |
| GPT-4o | Fallback for general tasks |

### Pricing (Composer 2.5 tiers)
| Tier | Input/1M | Output/1M | Speed |
|------|----------|-----------|-------|
| Standard | $0.50 | $2.50 | Normal |
| Fast | $3.00 | $15.00 | ~30% faster |

### Interfaces
- **CLI:** N/A (IDE-only product)
- **IDE:** Custom VS Code fork with inline predictions + Composer multi-file editing
- **Web:** N/A

### Architecture
- Operates directly on active text buffer
- Composer: multi-file editing from high-level instructions
- Inline predictive typing (tab completion)
- Auto-pulls related files into prompt window for context coherence

### Benchmarks
| Benchmark | Score |
|-----------|-------|
| SWE-Bench Multilingual | 79.8% |
| CursorBench v3.1 | 63.2% |
| Terminal-Bench 2.0 | Evaluated (score not public) |

*Matches Claude Opus 4.7 and GPT-5.5 at ~1/10th the cost per token.*

### Metering
- Usage-equivalent dollar drawdown pool (~$20 value on Pro)
- Fast tier is 6× more expensive but 30% faster
- Context auto-inclusion charges tokens for every related file pulled in

### $20 Budget Behavior
- **Scale resilience:** 50% (WORST — context snowball effect)
- **Catch:** As project grows 1K→20K lines, per-task cost rises 10–12×. A $0.02 task on day 1 becomes $0.25 by week 3.
- **Strength:** Best-in-class UX for small projects; inline completions feel magical

### Sources
- https://www.buildfastwithai.com/blogs/cursor-composer-2-5-review-2026
- https://artificialanalysis.ai/articles/cursor-composer-2-5-coding-agent-index
- https://beyondtmrw.org/article/cursor-composer-25-release-pricing-benchmarks-2026
- https://tech-insider.org/cursor-vs-copilot-2026/

---

## VS Code + Kiro

- **Vendor:** AWS (Amazon)
- **Price:** $20/mo (Pro, 1,000 credits)
- **Effective $20 capacity:** 500–1,000 tasks/month
- **Cost per task:** ~$0.027

### Models
| Model | Role |
|-------|------|
| Claude Sonnet 4.5 | Primary (default "Auto" mode) |
| Claude Sonnet 4.6 | Available (costs 1.3× more credits) |
| Custom auto-routing ensemble | Task-optimized selection |

### Interfaces
- **CLI:** N/A (IDE-only)
- **IDE:** Kiro IDE (VS Code fork by AWS)
- **Web:** N/A
- **Auth:** AWS Builder ID, IAM Identity Center

### Architecture
- Spec-driven workflow: Prompt → Executable Requirement Spec → Architecture Design → Code Generation → Property-based Tests
- Rejects "vibe coding" — forces you to agree on a technical spec before writing code
- Automatically writes property-based tests to verify code matches spec

### Benchmarks
- No published SWE-Bench score (spec-driven approach eliminates iterative benchmark-style loops)

### Metering
| Plan | Credits/mo | Price |
|------|-----------|-------|
| Free | 50 | $0 |
| Pro | 1,000 | $20/mo |
| Pro+ | 2,000 | $40/mo |
| Power | 10,000 | $200/mo |
| Overage | Per credit | $0.04/credit |

*Credits do NOT roll over. Sonnet 4.6 costs 1.3× more credits than Auto mode.*

### $20 Budget Behavior
- **Scale resilience:** 95% (deterministic credit consumption per spec)
- **Catch:** Requires disciplined architectural thinking; slower for quick experimentation
- **Strength:** Most predictable budget consumption — you know exactly what 1,000 credits buys

### Sources
- https://kiro.dev/docs/models/
- https://lushbinary.com/blog/kiro-ide-developer-guide-specs-hooks-agents-pricing/
- https://pingax.com/kiro-aws-launch-announcement/
- https://weavai.app/blog/en/2026/04/29/amazon-kiro-2026-review-spec-driven-ide-vs-cursor/

---

## Ollama Cloud

- **Vendor:** Ollama
- **Price:** $20/mo (Pro)
- **Effective $20 capacity:** 600–900 tasks/month
- **Cost per task:** ~$0.027

### Models
| Model | Category |
|-------|----------|
| DeepSeek-V4-Pro | Extra heavy (Level 4) |
| Qwen 3 Coder | Heavy (Level 3) |
| GPT-OSS (Level 1–4) | Various sizes |
| All open-weight frontier models | Immediately available on release |

### Interfaces
- **CLI:** `ollama` CLI (unified local + cloud interface)
- **IDE:** Any editor via OpenAI-compatible API endpoint
- **Web:** Ollama Cloud dashboard

### Architecture
- GPU-time billing: billed for literal GPU seconds of compute, NOT token count
- Large context does NOT increase cost proportionally (unlike token-metered tools)
- As hardware improves, you get more from the same plan

### Metering
| Plan | Price | Concurrency | Usage |
|------|-------|-------------|-------|
| Free | $0 | 1 model | Baseline |
| Pro | $20/mo | 3 models | 50× Free |
| Max | $100/mo | Unlimited | Maximum |

*Session limits reset every 5 hours. Weekly limits reset every 7 days.*

### $20 Budget Behavior
- **Scale resilience:** 98% (BEST — GPU-time billing immune to context cost penalties)
- **Catch:** Quality depends on which open model you choose (may trail proprietary frontier)
- **Strength:** Pass an enormous codebase context and you aren't penalized for file size

### Sources
- https://ollama.com/pricing
- https://dev.to/amareswer/ollama-cloud-free-vs-pro-usage-limits-pricing-what-you-actually-get-2026-3ieo
- https://pooyagolchian.com/blog/ollama-cloud-pricing-hardware-requirements-2026/
- https://daniliants.com/insights/pricing-ollama/

---

## GitHub Copilot

- **Vendor:** GitHub (Microsoft)
- **Price:** $10/mo (Pro) | $39/mo (Pro+) | $100/mo (Max)
- **Effective $20 capacity:** 300–500 tasks/month (on Pro + some Pro+ features)
- **Cost per task:** ~$0.050

### Models
| Model | Available on |
|-------|-------------|
| GPT-4o | Pro, Pro+, Max |
| Claude Sonnet 4.6 | Pro, Pro+, Max |
| Gemini 2.5 Pro | Pro, Pro+, Max |
| Claude Opus 4.6 | Pro+, Max only |
| o3 | Pro+, Max only |

### Interfaces
- **CLI:** GitHub Copilot CLI + Agent Mode
- **IDE:** VS Code, JetBrains, Neovim (native extensions)
- **Web:** github.com integrated (Copilot Chat)
- **Agent:** Assigns GitHub issues → autonomous PR generation

### Architecture
- Multi-model routing: selects best model per task type
- Agent Mode (GA since Mar 2026): multi-step autonomous coding in VS Code/JetBrains
- Coding Agent: assign an issue to Copilot → it writes code, runs tests, opens PR
- Agentic Code Review (Mar 2026): auto-generates fix PRs from review comments

### Benchmarks
| Benchmark | Score |
|-----------|-------|
| SWE-Bench Verified | 56.0% |

### Metering (since June 2026 — usage-based billing)
| Plan | Price | AI Credits/mo |
|------|-------|--------------|
| Free | $0 | Limited completions |
| Pro | $10/mo | $15 ($10 base + $5 flex) |
| Pro+ | $39/mo | Higher limits + premium models |
| Max | $100/mo | Maximum capacity |
| Business | $19/seat/mo | Org management |
| Enterprise | $39/seat/mo | Full compliance |

### $20 Budget Behavior
- **Scale resilience:** 80%
- **Catch:** Pro only gives $15 in credits; heavy agent mode usage needs Pro+ ($39)
- **Strength:** Best CI/CD integration — auto-assigns issues to PRs. Multi-model means you can match model to task.

### Sources
- https://www.nxcode.io/resources/news/github-copilot-complete-guide-2026-features-pricing-agents
- https://tech-insider.org/github-copilot-vs-cursor-2026-2/
- https://github.com/features/copilot/plans
- https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing

---

## Microsoft Copilot

- **Vendor:** Microsoft
- **Price:** $20/mo (Copilot Pro consumer)
- **Effective $20 capacity:** 300–400 tasks/month
- **Cost per task:** ~$0.057

### Models
| Model | Role |
|-------|------|
| GPT-4o | Primary general model |
| GPT-5.2 | Complex reasoning tasks |
| Phi-4 | Fast/light tasks (Microsoft proprietary) |
| Work IQ | Dynamic hybrid routing layer |

### Interfaces
- **CLI:** N/A
- **IDE:** N/A (not a code IDE — it's an office productivity tool)
- **Web:** Edge integration, Bing Chat, Microsoft 365 apps
- **Office:** Word, Excel, PowerPoint, Outlook, Teams

### Architecture
- Work IQ: dynamically selects from GPT-4o/5.2/Phi-4 based on task complexity and latency
- Deep Microsoft Graph grounding (accesses your M365 data for context)
- DALL-E 3 image generation included
- Primarily an office productivity AI, not a code-focused tool

### Benchmarks
- No code-specific SWE-Bench score (not designed for autonomous coding)

### Metering
| Plan | Price | Target |
|------|-------|--------|
| Free | $0 | Basic chat |
| Pro | $20/mo | Consumer (priority access, all models) |
| M365 Copilot | $30/user/mo | Enterprise (requires E3/E5 license) |

### $20 Budget Behavior
- **Scale resilience:** 80%
- **Catch:** Limited multi-file code reasoning; designed for office productivity, not dev workflows
- **Strength:** If you already pay for M365, the integration is seamless for docs/emails alongside coding

### Sources
- https://ucstrategies.com/news/microsoft-copilot-guide-specs-pricing-graph-grounding-explained-2026/
- https://www.datastudios.org/post/microsoft-copilot-model-lineup-combines-gpt-5-gpt-4o-phi-series-and-custom-studio-options-to-powe
- https://tech-insider.org/chatgpt-vs-copilot-2026/

---

## OpenAI Codex

- **Vendor:** OpenAI
- **Price:** $20/mo (Plus) | $100/mo (Pro 5×) | $200/mo (Pro 20×)
- **Effective $20 capacity:** 200–400 tasks/month
- **Cost per task:** ~$0.067

### Models
| Model | Availability |
|-------|-------------|
| GPT-5.3-Codex | Default for code agent tasks |
| GPT-5.4-Mini | Lighter/cheaper tasks |
| GPT-5.3-Codex-Spark | Research preview (Pro only) |
| GPT-5.5 | Highest capability (Pro only) |

### Interfaces
- **CLI:** Codex CLI
- **IDE:** VS Code extension
- **Web:** Codex web app (codex.openai.com)
- **Mobile:** iOS app
- **Integrations:** GitHub, Slack bot, auto code review

### Architecture
- Cloud-sandboxed agent: reads repo, writes code, runs tests autonomously
- Token-based billing aligned with API rates (changed Apr 2, 2026)
- Supports automated code review and PR generation

### Benchmarks
| Benchmark | Score |
|-----------|-------|
| SWE-Bench Verified | ~72% (GPT-5.3-Codex estimated) |

### Metering
| Plan | Price | Notes |
|------|-------|-------|
| Free | $0 | Very limited |
| Go | $8/mo | Basic access |
| Plus | $20/mo | Expanded Codex usage |
| Pro 5× | $100/mo | 5× capacity |
| Pro 20× | $200/mo | 20× capacity |

*Real-world heavy usage: ~$100–200/developer/month due to reasoning model overhead.*

### $20 Budget Behavior
- **Scale resilience:** 70%
- **Catch:** Reasoning models (o1, GPT-5.5) consume quotas 2–3× faster than standard completions
- **Strength:** Strongest autonomous agent when budget isn't constrained; excellent at test-driven development

### Sources
- https://www.eesel.ai/blog/codex-pricing
- https://www.morphllm.com/codex-pricing
- https://www.verdent.ai/guides/codex-pricing-2026
- https://www.taskade.com/blog/codex-pricing-explained

---

## Claude Code (CLI)

- **Vendor:** Anthropic
- **Price:** $20/mo (Pro) | $100/mo (Max 5×) | $200/mo (Max 20×)
- **Effective $20 capacity:** 150–250 tasks/month
- **Cost per task:** ~$0.100

### Models
| Model | Input/1M | Output/1M |
|-------|----------|-----------|
| Claude Sonnet 5 | $3 | $15 |
| Claude Opus 4.6/4.7/4.8 | $5 | $25 |
| Claude Haiku 4.5 | $1 | $5 |
| Claude Fable 5 | $10 | $50 |

### Interfaces
- **CLI:** Claude Code (official Anthropic terminal agent)
- **IDE:** VS Code extension, JetBrains extension
- **Web:** claude.ai/code
- **Desktop:** Mac and Windows app

### Architecture
- Agentic loop: reads/edits code, runs shell commands, iterates on errors
- Native MCP (Model Context Protocol) support
- Subagents for parallel work
- Computer use: can open apps and navigate browsers from terminal
- Extended thinking for complex reasoning chains

### Benchmarks
| Benchmark | Score |
|-----------|-------|
| SWE-Bench Verified | 80.8% (Opus 4.6) — highest of all tools |

### Metering
| Plan | Token Window (5hr) | Sonnet/week | Opus/week |
|------|-------------------|-------------|-----------|
| Pro ($20) | ~44K tokens | Limited | Very limited |
| Max 5× ($100) | ~88K tokens | 140–280 hrs | 15–35 hrs |
| Max 20× ($200) | ~220K tokens | 240–480 hrs | 24–40 hrs |

### Cost Optimization (API mode)
- Cache reads: 10% of standard input price
- Batch API: 50% discount on all models
- Prompt caching is the largest cost lever for API users

### $20 Budget Behavior
- **Scale resilience:** 60% (agentic loops consume window rapidly)
- **Catch:** Pro gives only ~44K tokens/5hr (10–40 prompts). Agentic loops where the model iterates multiple times drain this fast.
- **Strength:** Highest benchmark scores. Best for hard problems where getting it right on fewer attempts saves money vs. cheaper tools that need more iterations.

### Sources
- https://www.verdent.ai/guides/claude-code-pricing-2026
- https://www.nxcode.io/resources/news/claude-code-pricing-2026-free-api-costs-max-plan
- https://www.finout.io/blog/claude-code-pricing-2026
- https://platform.claude.com/docs/en/about-claude/pricing

---

## Ollama (Local)

- **Vendor:** Ollama (open-source)
- **Price:** Free ($0)
- **Effective $20 capacity:** Unlimited (hardware-bound)
- **Cost per task:** $0 (electricity only)

### Models
| Model | Size | Quality |
|-------|------|---------|
| Qwen 3 Coder | 7B–72B | Good for completions |
| DeepSeek-Coder-V2 | 16B–236B | Strong code generation |
| Llama 3.3 | 8B–70B | General purpose |
| CodeGemma | 7B | Fast, lightweight |
| Any GGUF model | Varies | Community models |
| Kimi K3 (upcoming) | TBD | Near-frontier when released |

### Interfaces
- **CLI:** `ollama pull`, `ollama run`, `ollama serve`
- **IDE:** Any editor via localhost OpenAI-compatible API (Continue, Aider, Cody, etc.)
- **Web:** Open WebUI (self-hosted)
- **API:** OpenAI-compatible endpoint at localhost:11434

### Architecture
- Local inference on your GPU (no network dependency)
- Full privacy — code never leaves your machine
- GGUF quantization for running large models on consumer hardware
- No rate limits, no quotas, no accounts

### Benchmarks
| Model | SWE-Bench (estimated) |
|-------|----------------------|
| Qwen 3 32B | ~55% |
| DeepSeek-Coder-V2 236B | ~65% |

### Requirements
- Minimum: 8GB RAM, any GPU with 4GB+ VRAM (or CPU-only, slower)
- Recommended: 16GB+ RAM, GPU with 12GB+ VRAM (RTX 3060+)
- For 70B models: 32GB+ RAM, 24GB VRAM (RTX 4090 / A6000)

### $20 Budget Behavior
- **Scale resilience:** 100% (cost never increases)
- **Catch:** Quality is below cloud frontier models. Generation speed limited by your hardware.
- **Strength:** Unlimited usage. Run Kimi K3 / DeepSeek open weights for $0 once released. Perfect for bulk boilerplate, completions, and privacy-sensitive code.

### Sources
- https://ollama.com
- https://ollama.com/pricing (local is free)

---

## Comparison Leaderboard Sources

These websites maintain live rankings and can be used as data sources:

| Site | URL | What it tracks |
|------|-----|---------------|
| Lushbinary | https://lushbinary.com/blog/ai-coding-agents-comparison-cursor-windsurf-claude-copilot-kiro-2026/ | Full feature + pricing comparison |
| LogRocket | https://blog.logrocket.com/ai-dev-tool-power-rankings/ | Power rankings (Jul 2026) |
| LLM-Stats | https://llm-stats.com/ | 300+ models by intelligence, speed, price |
| Kilo.ai | https://kilo.ai/leaderboard | Live leaderboard from 3M+ devs |
| Artificial Analysis | https://artificialanalysis.ai/articles/cursor-composer-2-5-coding-agent-index | Coding Agent Index |
| LLM-Stats Benchmarks | https://llm-stats.com/benchmarks | AI Benchmarks 2026 |
| NxCode | https://www.nxcode.io/resources/news/best-ai-for-coding-2026-complete-ranking | Best AI for Coding rankings |
| AIMultiple | https://aimultiple.com/ai-coding-benchmark | Claude Code vs Cursor benchmark |

---

## Summary Ranking (by $20 task capacity)

| Rank | Tool | Tasks/Mo | $/Task | Scale Score | SWE-Bench |
|------|------|----------|--------|-------------|-----------|
| 1 | Google Antigravity 2.0 | 1,200–1,600 | $0.014 | 85% | N/A |
| 2 | Kimi K2.7 Code | 600–1,000 | $0.025 | 92% | 76.8% |
| 3 | Ollama Cloud | 600–900 | $0.027 | 98% | ~75% (model-dependent) |
| 4 | VS Code + Kiro | 500–1,000 | $0.027 | 95% | N/A |
| 5 | GitHub Copilot | 300–500 | $0.050 | 80% | 56.0% |
| 6 | Microsoft Copilot | 300–400 | $0.057 | 80% | N/A |
| 7 | Cursor AI | 250–500 | $0.053 | 50% | 79.8% |
| 8 | OpenAI Codex | 200–400 | $0.067 | 70% | ~72% |
| 9 | Claude Code (CLI) | 150–250 | $0.100 | 60% | 80.8% |
| ∞ | Ollama (Local) | Unlimited | $0 | 100% | ~55% |

---

## Optimal $20 Strategy (Multi-Tool Rotation)

1. **Phase 1 — Scaffolding:** Google Antigravity or Ollama Local (free/cheap bulk generation)
2. **Phase 2 — Velocity:** Cursor AI (while project is <5K lines and context costs are low)
3. **Phase 3 — Iteration:** Kimi K2.7 Code (prompt caching makes growing projects cheaper)
4. **Phase 4 — Hard Problems:** Kiro specs or Claude Code (pay premium only for complex integration)
5. **Phase 5 — CI/CD:** GitHub Copilot Agent (auto-assigns issues → PRs)
