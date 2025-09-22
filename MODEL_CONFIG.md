# Strix Model Configuration Examples

## Environment Variables Configuration

### DeepSeek Models
```bash
export STRIX_LLM="deepseek-chat"
export DEEPSEEK_API_KEY="your_deepseek_api_key_here"
# Optional: custom API base
export STRIX_API_BASE="https://api.deepseek.com"
```

### GLM Models (Zhipu AI)
```bash
export STRIX_LLM="glm-4-flash"
export GLM_API_KEY="your_glm_api_key_here"
# Optional: custom API base
export STRIX_API_BASE="https://open.bigmodel.cn/api/paas/v4"
```

### Custom OpenAI-Compatible API
```bash
export STRIX_LLM="gpt-4"  # or any model name your API supports
export STRIX_API_BASE="https://your-custom-api.com/v1"
export STRIX_API_KEY="your_custom_api_key_here"
# or use OPENAI_API_KEY
export OPENAI_API_KEY="your_custom_api_key_here"
```

### OpenAI Models (Default)
```bash
export STRIX_LLM="openai/gpt-5"
export OPENAI_API_KEY="your_openai_api_key_here"
```

## Available Models

### DeepSeek Models
- `deepseek-chat` - General purpose chat model
- `deepseek-coder` - Code optimized model
- `deepseek-v2.5` - Latest version
- `deepseek-r1` - Reasoning optimized model

### GLM Models (Zhipu AI)
- `glm-4` - Latest general model
- `glm-4-air` - Lightweight model
- `glm-4-airx` - Enhanced lightweight model
- `glm-4-flash` - Fast model
- `glm-4v` - Multimodal model
- `glm-z1-air` - Zhipu series lightweight
- `glm-z1-airx` - Zhipu series enhanced
- `glm-z1-preview` - Zhipu series preview

### OpenAI Models
- `openai/gpt-5` - Default model
- `openai/gpt-5-mini` - Mini version
- `openai/gpt-5-nano` - Nano version
- `openai/o1-mini` - Reasoning model mini
- `openai/o1-preview` - Reasoning model preview

## Usage Examples

### Using DeepSeek for Security Testing
```bash
cd /path/to/strix
export STRIX_LLM="deepseek-chat"
export DEEPSEEK_API_KEY="your_key_here"
strix --target https://example.com --instruction "Test for XSS vulnerabilities"
```

### Using GLM for Code Analysis
```bash
cd /path/to/strix
export STRIX_LLM="glm-4-flash"
export GLM_API_KEY="your_key_here"
strix --target /path/to/code --scan-type repository --instruction "Analyze security issues"
```

### Using Custom API
```bash
cd /path/to/strix
export STRIX_LLM="gpt-4"
export STRIX_API_BASE="https://your-api.com/v1"
export STRIX_API_KEY="your_key_here"
strix --target https://example.com --instruction "Perform security assessment"
```

## Configuration Priority

1. Explicit parameters in LLMConfig constructor
2. Environment variables:
   - `STRIX_API_KEY` / `LLM_API_KEY`
   - `DEEPSEEK_API_KEY` (for DeepSeek models)
   - `GLM_API_KEY` / `ZHIPU_API_KEY` (for GLM models)
   - `OPENAI_API_KEY` (fallback)
3. Default values

## Notes

- All models support the same security testing capabilities
- Custom API base URLs must be OpenAI-compatible
- API keys are required for all models
- Temperature and other parameters can be adjusted as needed