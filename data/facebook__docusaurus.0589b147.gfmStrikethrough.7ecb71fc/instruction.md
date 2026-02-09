# Bug Report

### Describe the bug

Strikethrough text rendering is broken in markdown parsing. When using double tildes (`~~text~~`) to create strikethrough formatting, the text is not being properly recognized or rendered.

### Reproduction

```markdown
This is ~~strikethrough~~ text.

Multiple ~~words~~ can be ~~struck through~~.
```

The strikethrough sequences are not being matched correctly, so the text either doesn't render with strikethrough formatting at all, or renders incorrectly.

### Expected behavior

Text wrapped in double tildes should render with strikethrough formatting applied. The opening `~~` should be properly paired with the closing `~~` to mark the text in between as strikethrough.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems to have started recently. The strikethrough matching logic might not be finding the correct opening/closing pairs.

---
Repository: /testbed
