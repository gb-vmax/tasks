# Bug Report

### Describe the bug

HTML closing tags in markdown are not being parsed correctly. When using closing tags with alphanumeric characters (like `</div>`, `</span>`, etc.), they are not recognized as valid HTML tags.

### Reproduction

```markdown
<div>Some content</div>
```

When processing this markdown, the closing tag `</div>` is not being properly tokenized. The parser seems to stop recognizing valid closing tag characters after the slash.

This also affects other common HTML tags:
```markdown
<p>Paragraph</p>
<span>Text</span>
<article>Content</article>
```

### Expected behavior

The parser should correctly identify and tokenize HTML closing tags that contain alphanumeric characters. Both opening and closing tags should be recognized as valid HTML within the markdown content.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
