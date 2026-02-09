# Bug Report

### Describe the bug

I'm experiencing an issue with autolink detection in GFM (GitHub Flavored Markdown) where certain URLs are not being properly recognized or are being incorrectly parsed. It seems like the logic for checking balanced brackets/parentheses in autolinks isn't working as expected.

### Reproduction

When parsing markdown content with URLs that contain special characters or are positioned after certain label elements, the autolink detection fails or behaves unexpectedly.

For example:
```markdown
[label](url) https://example.com
```

Or with nested structures:
```markdown
![image](url) www.example.com/path
```

The URLs that should be automatically converted to links are either not detected or the parsing produces incorrect results.

### Expected behavior

URLs should be properly detected and converted to autolinks regardless of their position relative to other markdown elements like links or images. The parser should correctly handle the balance checking of preceding label elements.

### Additional context

This seems to be related to how the parser walks through events and checks for unbalanced label links/images before processing autolinks. The current behavior is inconsistent with what I'd expect from standard GFM processing.

---
Repository: /testbed
