# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where the heading depth/level is being calculated incorrectly. It seems like headings are being assigned the wrong depth value when processing markdown.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When parsing the above markdown, the heading depths don't match what's expected. For example:
- `# Heading 1` should have depth 1
- `## Heading 2` should have depth 2
- `### Heading 3` should have depth 3

But the actual depths being assigned appear to be off by one or completely wrong.

### Expected behavior

ATX headings should be parsed with the correct depth based on the number of `#` symbols:
- Single `#` → depth 1
- Double `##` → depth 2
- Triple `###` → depth 3
- And so on...

The heading depth should accurately reflect the number of hash symbols in the markdown source.

### Additional context

This affects any markdown content with ATX-style headings. The issue seems to have appeared recently and is causing incorrect heading hierarchy in the parsed output.

---
Repository: /testbed
