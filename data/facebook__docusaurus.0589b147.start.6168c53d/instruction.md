# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/strong emphasis markdown rendering. When trying to use asterisks (`*`) or underscores (`_`) for emphasis in markdown text, the parser is not correctly recognizing the markers and the output is broken.

### Reproduction

```markdown
This is *italic* text and this is **bold** text.
```

Expected output should render italic and bold text, but instead the markers are not being matched properly and the emphasis syntax is not working as expected.

It seems like the parser is looking for the wrong character code when processing attention sequences (emphasis/strong markers). The opening and closing markers don't match up correctly.

### Steps to reproduce
1. Parse markdown text containing emphasis markers (`*` or `_`)
2. The emphasis is not applied correctly
3. Opening and closing markers fail to match

### Expected behavior
Emphasis markers should be properly paired and the text between them should be rendered with the appropriate styling (italic for single markers, bold for double markers).

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
