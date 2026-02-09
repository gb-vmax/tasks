# Bug Report

### Describe the bug

Strikethrough text is not rendering correctly in markdown when using GFM (GitHub Flavored Markdown). The strikethrough syntax `~~text~~` appears to be processed twice, which causes unexpected behavior in the output.

### Reproduction

```markdown
This is ~~strikethrough~~ text.

~~Multiple~~ ~~strikethrough~~ words in a sentence.
```

When parsing this markdown with the GFM plugin, the strikethrough formatting gets applied in an unexpected way, likely due to the extension being registered multiple times in the processing pipeline.

### Expected behavior

Strikethrough text should be rendered correctly with a single strikethrough effect. The `~~text~~` syntax should produce properly formatted strikethrough output without duplication or conflicts.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
