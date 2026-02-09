# Bug Report

### Describe the bug

Footnote definitions in GFM (GitHub Flavored Markdown) are not being parsed correctly. When using footnote syntax like `[^1]: footnote text`, the content appears to be treated incorrectly, causing issues with nested content rendering.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is a footnote definition.
    It can have multiple lines.
    
    And even multiple paragraphs.
```

When parsing the above markdown, the footnote definition doesn't handle nested block content properly. The indented continuation lines and nested paragraphs within the footnote are not being recognized as part of the footnote container.

### Expected behavior

The footnote definition should act as a container that can hold nested block-level content (paragraphs, lists, code blocks, etc.). All properly indented content following the footnote label should be parsed as children of that footnote definition.

### Additional context

This seems to affect how nested elements within footnotes are structured in the AST. The footnote definition should be treated as a container element to properly handle multi-line and multi-paragraph footnote content according to GFM spec.

---
Repository: /testbed
