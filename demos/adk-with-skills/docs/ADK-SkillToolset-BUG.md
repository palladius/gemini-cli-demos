# Bug: SkillToolset Incompatibility with BuiltInCodeExecutor

**GitHub Issue:** [google/adk-python#5524](https://github.com/google/adk-python/issues/5524)
**Internal Reference:** [go/orcas-rfc-657](http://go/orcas-rfc-657)

## Overview

When using the ADK's `SkillToolset` in conjunction with an agent configured to use `BuiltInCodeExecutor`, model invocations fail with a `400 INVALID_ARGUMENT` error.

## Error Message

```
google.genai.errors.ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Please enable tool_config.include_server_side_tool_invocations to use Built-in tools with Function calling.', 'status': 'INVALID_ARGUMENT', ...}}
```

## Details

1.  **Attempted Fixes:**
    *   Adding `tool_config` with `include_server_side_tool_invocations=True` to the `Agent` constructor (rejected by Pydantic validation).
    *   Adding `tool_config` to the `Gemini` model constructor (parameters not propagated correctly).
    *   Using `Gemini.from_config` (method does not exist on the class).
2.  **Current Status:**
    *   A feature request/bug report has been filed at: https://github.com/google/adk-python/issues/5524
3.  **Workaround:**
    *   The demo currently uses a `FunctionTool` that manually executes the skill's script via `subprocess.run`.
    *   While functional, this bypasses the ADK's native skill management and is less integrated.

## Impact

Prevents idiomatic use of `SkillToolset` for agents requiring built-in code execution capabilities.
