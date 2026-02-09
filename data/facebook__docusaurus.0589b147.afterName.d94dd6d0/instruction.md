# Bug Report

### Describe the bug

I'm encountering an issue with inline text directives in remark-directive where the parser is incorrectly handling colons (`:`) after directive names. The directive parsing seems to be rejecting valid directives when it should be accepting them, or vice versa.

### Reproduction

```markdown
:directive-name:some text
```

When parsing the above inline text directive, the behavior around the colon character appears to be inverted - it's treating valid syntax as invalid or allowing invalid syntax to pass through.

### Expected behavior

The parser should correctly handle the colon character that follows directive names in inline text directives. Valid directives with proper colon placement should be parsed successfully, while invalid ones should be properly rejected.

### System Info
- remark-directive version: 3.0.0
- Node version: (latest)

This seems like it might be a logic error in the tokenization code for text directives. The condition checking for the colon character may have been inverted accidentally.

---
Repository: /testbed
