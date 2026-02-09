# Bug Report

### Describe the bug

Footnote definitions in GFM (GitHub Flavored Markdown) are not being parsed correctly. When I have a footnote definition that spans multiple lines, the continuation lines are not being recognized as part of the definition.

### Reproduction

```markdown
Here is some text with a footnote[^1].

[^1]: This is a footnote definition
    that continues on the next line
    and even more lines after that.
```

The footnote definition should include all the indented continuation lines, but it seems like only the first line is being captured.

### Expected behavior

Multi-line footnote definitions should be fully parsed, with all continuation lines (properly indented) included as part of the footnote content. The parser should recognize indented lines following the initial definition as part of the same footnote.

### Additional context

This appears to be related to how the tokenizer handles footnote definition continuation. The issue manifests when trying to render markdown documents that use the standard GFM footnote syntax with multi-line definitions.

---
Repository: /testbed
