# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where the heading text is not being properly captured. When parsing markdown headings (the `#` style headings), the text content seems to be getting lost or not processed correctly.

### Reproduction

```markdown
# My Heading
## Another Heading
### Nested Heading
```

When parsing the above markdown, the heading structure is recognized but the actual text content ("My Heading", "Another Heading", "Nested Heading") is not being properly extracted or stored.

### Expected behavior

The parser should correctly capture and preserve the heading text content. For example:
- `# My Heading` should parse with text "My Heading"
- `## Another Heading` should parse with text "Another Heading"
- And so on...

Currently it seems like the text is being skipped or the data isn't being properly exited before moving to the next parsing state.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
