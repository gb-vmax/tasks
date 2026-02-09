# Bug Report

### Describe the bug

I'm experiencing an issue with autolink detection in GFM (GitHub Flavored Markdown) parsing. It seems like autolinks are not being recognized correctly when they appear after certain label elements (like links or images).

### Reproduction

```markdown
[label](url) https://example.com
```

When parsing the above markdown, the autolink `https://example.com` should be detected and converted to a clickable link, but it's not being recognized properly.

Similarly with images:

```markdown
![alt](image.png) https://example.com
```

The URL after the image should be autolinked but isn't working as expected.

### Expected behavior

URLs that appear after label links or images should still be automatically converted to clickable links. The autolink detection should work regardless of what precedes it in the text.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
