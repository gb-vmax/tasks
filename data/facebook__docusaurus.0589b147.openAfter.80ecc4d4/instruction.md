# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers in remark-directive where the parsing behavior seems incorrect when handling end-of-file and line ending conditions. 

When a directive container fence is followed by null (EOF) or a markdown line ending, the parser doesn't handle these cases properly. Specifically:

1. When the code is `null` (end of file), it should continue to `afterOpening` but the condition check appears inverted
2. When there's a markdown line ending and `self.interrupt` is set, the flow seems backwards - it returns `ok3` when interrupt is false instead of when it's true

### Reproduction

```markdown
:::directive
content here
```

(note: no closing fence, ends at EOF)

Or with interrupt scenarios:

```markdown
:::directive
:::
```

The parser doesn't correctly handle these edge cases, leading to unexpected parsing results or the directive container not being properly recognized.

### Expected behavior

- When reaching EOF after a directive container fence, it should properly exit and handle the opening
- The interrupt flag should be respected correctly - when `self.interrupt` is true, it should handle the case appropriately, not when it's false

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-based

---
Repository: /testbed
