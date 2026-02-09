# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain GFM (GitHub Flavored Markdown) syntax extensions are not being applied correctly. It seems like syntax constructs are being overwritten instead of properly extended when they should be preserved.

### Reproduction

When using remark-gfm with custom syntax extensions, the parser fails to recognize certain markdown features. For example:

```markdown
- [ ] Task list item
- [x] Completed task

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

These GFM features may not render properly depending on which extensions are loaded and in what order.

### Expected behavior

All GFM syntax extensions should be properly merged and applied. When multiple extensions define handlers for the same syntax construct, they should be combined rather than one overwriting the other.

### Additional context

This appears to be related to how syntax extension objects are being merged together. The logic for combining left and right extension properties seems inverted - it's only creating arrays for properties that already exist in the left object, when it should be doing the opposite.

---
Repository: /testbed
