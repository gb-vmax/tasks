# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in remark. Text directives (starting with `:`) are not being recognized or processed correctly. The parser seems to be skipping over them entirely.

### Reproduction

```markdown
This is a :text-directive[with content] that should be parsed.

Another :simple-directive example here.
```

When processing this markdown, the text directives are not being transformed - they're just passed through as plain text instead of being recognized as directive nodes.

### Expected behavior

Text directives should be properly tokenized and converted into directive nodes in the AST, similar to how container and leaf directives are handled.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
