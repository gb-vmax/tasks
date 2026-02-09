# Bug Report

### Describe the bug

I'm encountering an issue with image syntax parsing when footnotes are enabled. It seems like images starting with `![^` are being incorrectly handled - they're either not parsing as images when they should, or parsing when they shouldn't.

### Reproduction

```markdown
![^test](image.png)
```

When footnotes support is enabled in the parser, this image syntax is not being recognized correctly. The behavior appears to be inverted from what's expected.

### Expected behavior

Images with `![^` syntax should be parsed as images regardless of footnote support configuration. The presence of `_hiddenFootnoteSupport` in the parser constructs shouldn't affect image parsing in this way.

### System Info
- remark version: 15.0.1
- Parser: micromark-core-commonmark

---
Repository: /testbed
