# Bug Report

### Describe the bug

There's an issue with footnote definition parsing where the size counter is being incremented at the wrong point in the code flow. This causes the parser to incorrectly track the label size when processing footnote definitions, and also the logic for detecting whether data has been encountered appears to be inverted.

### Reproduction

```markdown
[^1]: This is a footnote definition

Some text with a footnote reference[^1].
```

When parsing footnote definitions like the above, the internal size tracking gets out of sync. The size counter should be incremented during character consumption in the main loop, not after the closing bracket is processed. Additionally, the check for whether we've seen actual data (non-whitespace characters) seems backwards.

### Expected behavior

The parser should correctly track the size of footnote labels as characters are consumed, and properly distinguish between empty labels and labels with content. The size increment should happen during normal character processing, not after the label has been closed.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
