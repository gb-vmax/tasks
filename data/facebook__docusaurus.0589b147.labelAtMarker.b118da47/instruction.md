# Bug Report

### Describe the bug

Footnote definitions in GFM (GitHub Flavored Markdown) are not being parsed correctly. The parser appears to be looking for the wrong character code when processing footnote definition markers.

### Reproduction

```markdown
[^1]: This is a footnote definition
```

When parsing the above markdown, the footnote definition is not recognized properly. The parser seems to expect a different character than the standard `^` caret symbol used in GFM footnote syntax.

### Expected behavior

The parser should correctly identify and process footnote definitions that start with `[^` followed by the footnote label. The `^` character (code 94) should be recognized as the footnote definition marker.

### Additional context

This affects all footnote definitions in markdown documents. The footnotes are a standard part of GFM syntax and should work according to the specification.

---
Repository: /testbed
