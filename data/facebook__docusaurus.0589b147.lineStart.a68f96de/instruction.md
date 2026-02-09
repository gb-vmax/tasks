# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where lazy continuation lines are being handled incorrectly. It seems like the parser is not properly detecting when a line should be treated as a lazy continuation versus a new block.

### Reproduction

```markdown
::: directive
Some content here
This line should continue the directive
:::
```

When parsing the above markdown with directives, the continuation lines are being rejected when they should be accepted (or vice versa). The behavior seems inverted - lines that should be part of the directive content are being treated as separate blocks, and lines that should start new blocks are being included in the directive.

### Expected behavior

The parser should correctly identify lazy continuation lines and include them as part of the directive content when appropriate. Lines that are lazy continuations should remain within the directive block, while non-lazy lines should properly terminate the directive.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
