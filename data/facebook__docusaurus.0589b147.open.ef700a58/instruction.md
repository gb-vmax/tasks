# Bug Report

### Describe the bug

Image syntax in MDX is not being parsed correctly. When using the standard Markdown image syntax `![alt text](url)`, the parser fails to properly recognize and process the image markup.

### Reproduction

```markdown
![Example Image](https://example.com/image.png)
```

When this is processed, the image syntax is not being recognized as valid and the content is not rendered as expected.

### Expected behavior

The parser should correctly identify and process the image syntax `![...]` and render it as an image element. The label image marker should be properly closed after consuming the opening bracket.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
