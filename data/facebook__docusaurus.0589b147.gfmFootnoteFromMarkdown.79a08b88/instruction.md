# Bug Report

### Describe the bug

I'm encountering an issue with GFM footnote parsing where footnote definitions and footnote calls seem to be getting mixed up. The parser appears to be confusing the enter/exit handlers for footnote definitions and calls, resulting in malformed AST output.

### Reproduction

```markdown
Here's some text with a footnote[^1].

[^1]: This is the footnote definition.
```

When parsing this markdown with GFM footnotes enabled, the resulting AST has incorrect node types. Footnote calls are being processed as definitions and vice versa.

### Expected behavior

Footnote definitions should be parsed as `footnoteDefinition` nodes and footnote calls should be parsed as `footnoteReference` nodes. The enter/exit handlers should match their respective node types so the AST structure is correct.

Currently seeing the handlers getting swapped - footnote calls trigger definition handlers and definitions trigger call handlers.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
