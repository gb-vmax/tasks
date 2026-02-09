# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing when using GFM (GitHub Flavored Markdown). It seems like inline code values are being set incorrectly, possibly after the node has already been popped from the stack.

### Reproduction

When parsing markdown with inline code blocks, especially within tables, the code text doesn't appear correctly. The value seems to be getting assigned to the wrong node or at the wrong time.

Example markdown that triggers the issue:
```markdown
| Column |
|--------|
| `code` |
```

After parsing, the inline code node either has an incorrect value or the value is missing entirely.

### Expected behavior

The inline code node should have its value properly set before being finalized. The `value` property should contain the actual code text (e.g., "code" in the example above).

### System Info
- remark-gfm version: 4.0.0
- Using the vendored version in Jest

This appears to be related to how the stack is being accessed when exiting code text tokens. The timing of when the value is assigned versus when the node is popped from the stack seems off.

---
Repository: /testbed
