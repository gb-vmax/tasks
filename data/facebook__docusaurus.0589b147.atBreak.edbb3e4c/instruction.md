# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading parsing where whitespace handling in ATX headings appears to be broken. After parsing headings with trailing sequences (like `## Heading ##`), subsequent whitespace is not being processed correctly.

### Reproduction

```markdown
## Heading with trailing sequence ##
```

When parsing this markdown, the whitespace after the trailing `##` sequence doesn't seem to be handled properly. The parser appears to skip over important whitespace processing steps.

### Expected behavior

The parser should correctly handle whitespace between the heading text and any trailing `#` sequences. Whitespace should be properly tokenized and the heading text should be correctly identified.

### Additional context

This seems to affect ATX-style headings (those starting with `#`) when they include trailing hash sequences. Regular headings without trailing sequences might work fine, but the issue manifests when the heading has both opening and closing `#` marks.

---
Repository: /testbed
