# Bug Report

### Describe the bug

I'm encountering an issue with directive containers when they end with EOF (no closing content). The parser seems to be calling token exit operations in the wrong order, which is causing problems with the AST structure.

### Reproduction

When parsing a directive container that ends at EOF without any content:

```markdown
:::note
:::
```

Or when there's a directive container at the end of the document:

```markdown
Some content here

:::warning
```

The parser doesn't properly handle the end-of-file case. The content token operations seem to be executed in an unexpected sequence.

### Expected behavior

The parser should correctly handle directive containers that end at EOF, properly entering and exiting tokens in the correct order regardless of whether there's content or not.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
