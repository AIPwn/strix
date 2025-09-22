<div align="center">

# Strix

### Open-source AI hackers for your apps

[![Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Vercel AI Accelerator 2025](https://img.shields.io/badge/Vercel%20AI-Accelerator%202025-000000?style=flat&logo=vercel)](https://vercel.com/ai-accelerator)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange.svg)](https://github.com/usestrix/strix)

</div>

<div align="center">
<img src=".github/screenshot.png" alt="Strix Demo" width="800" style="border-radius: 16px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.2); transform: perspective(1000px) rotateX(2deg); transition: transform 0.3s ease;">
</div>

---

## 🦉 Strix Overview

Strix are autonomous AI agents that act just like real hackers - they run your code dynamically, find vulnerabilities, and validate them through actual exploitation. Built for developers and security teams who need fast, accurate security testing without the overhead of manual pentesting or the false positives of static analysis tools.

### 🚀 Quick Start

```bash
# Install
pipx install strix-agent

# Configure AI provider
export STRIX_LLM="openai/gpt-5"
export LLM_API_KEY="your-api-key"

# Run security assessment
strix --target ./app-directory

# Alternative: Use DeepSeek
export STRIX_LLM="deepseek-chat"
export DEEPSEEK_API_KEY="your-deepseek-key"

# Alternative: Use GLM
export STRIX_LLM="glm-4-flash"
export GLM_API_KEY="your-glm-key"

# Alternative: Use custom OpenAI-compatible API
export STRIX_LLM="gpt-4"
export STRIX_API_BASE="https://your-api.com/v1"
export STRIX_API_KEY="your-custom-key"
```

## Why Use Strix

- **Full Hacker Arsenal** - All the tools a professional hacker needs, built into the agents
- **Real Validation** - Dynamic testing and actual exploitation, thus much fewer false positives
- **Developer-First** - Seamlessly integrates into existing development workflows
- **Auto-Fix & Reporting** - Automated patching with detailed remediation and security reports

## ✨ Features

### 🛠️ Agentic Security Tools

- **🔌 Full HTTP Proxy** - Full request/response manipulation and analysis
- **🌐 Browser Automation** - Multi-tab browser for testing of XSS, CSRF, auth flows
- **💻 Terminal Environments** - Interactive shells for command execution and testing
- **🐍 Python Runtime** - Custom exploit development and validation
- **🔍 Reconnaissance** - Automated OSINT and attack surface mapping
- **📁 Code Analysis** - Static and dynamic analysis capabilities
- **📝 Knowledge Management** - Structured findings and attack documentation

### 🎯 Comprehensive Vulnerability Detection

- **Access Control** - IDOR, privilege escalation, auth bypass
- **Injection Attacks** - SQL, NoSQL, command injection
- **Server-Side** - SSRF, XXE, deserialization flaws
- **Client-Side** - XSS, prototype pollution, DOM vulnerabilities
- **Business Logic** - Race conditions, workflow manipulation
- **Authentication** - JWT vulnerabilities, session management
- **Infrastructure** - Misconfigurations, exposed services

### 🕸️ Graph of Agents

- **Distributed Workflows** - Specialized agents for different attacks and assets
- **Scalable Testing** - Parallel execution for fast comprehensive coverage
- **Dynamic Coordination** - Agents collaborate and share discoveries


## 🤖 Supported AI Models

Strix supports multiple LLM providers through OpenAI-compatible APIs:

### OpenAI Models
```bash
export STRIX_LLM="openai/gpt-5"
export LLM_API_KEY="your-openai-key"
```

### DeepSeek Models
```bash
export STRIX_LLM="deepseek-chat"  # or deepseek-coder, deepseek-v2.5, deepseek-r1
export DEEPSEEK_API_KEY="your-deepseek-key"
```

### GLM Models (Zhipu AI)
```bash
export STRIX_LLM="glm-4-flash"  # or glm-4, glm-4-air, glm-4v, etc.
export GLM_API_KEY="your-glm-key"
```

### Custom OpenAI-Compatible API
```bash
export STRIX_LLM="any-model-name"
export STRIX_API_BASE="https://your-api-endpoint.com/v1"
export STRIX_API_KEY="your-api-key"
```

### Environment Variables Priority
1. Explicit parameters in configuration
2. `STRIX_API_KEY` / `LLM_API_KEY`
3. Model-specific keys (`DEEPSEEK_API_KEY`, `GLM_API_KEY`, `ZHIPU_API_KEY`)
4. `OPENAI_API_KEY` (fallback)

See [MODEL_CONFIG.md](MODEL_CONFIG.md) for detailed configuration options.

## 💻 Usage Examples

```bash
# Local codebase analysis
strix --target ./app-directory

# Repository security review
strix --target https://github.com/org/repo

# Web application assessment
strix --target https://your-app.com

# Focused testing
strix --target api.your-app.com --instruction "Prioritize authentication and authorization testing"
```

### ⚙️ Configuration

```bash
# Required
export STRIX_LLM="openai/gpt-5"
export LLM_API_KEY="your-api-key"

# Recommended
export PERPLEXITY_API_KEY="your-api-key"
```

[📚 View supported AI models](https://docs.litellm.ai/docs/providers)

## 🏆 Enterprise Platform

Our managed platform provides:

- **📈 Executive Dashboards**
- **🧠 Custom Fine-Tuned Models**
- **⚙️ CI/CD Integration**
- **🔍 Large-Scale Scanning**
- **🔌 Third-Party Integrations**
- **🎯 Enterprise Support**

[**Get Enterprise Demo →**](https://form.typeform.com/to/ljtvl6X0)

## 🔒 Security Architecture

- **Container Isolation** - All testing in sandboxed Docker environments
- **Local Processing** - Testing runs locally, no data sent to external services

> [!NOTE]
> Strix is currently in Alpha. Expect rapid updates and improvements.
