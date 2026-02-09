# Bug Report

### Describe the bug

I'm encountering an issue with nested image links in markdown parsing. When I have an image inside a link (like `[![alt](image.png)](url)`), the parser seems to get confused and doesn't handle them correctly.

### Reproduction

```markdown
[![Image Alt Text](https://example.com/image.png)](https://example.com/link)
```

When parsing this markdown, the nested image link structure doesn't get processed as expected. It seems like the parser is not correctly matching the opening and closing brackets for the outer link when there's an image inside.

### Expected behavior

The parser should correctly handle nested structures where an image is wrapped in a link. The outer link should be recognized and the inner image should be properly nested within it.

### Additional context

This appears to be related to how the label resolution logic handles balanced brackets in nested link/image scenarios. The issue manifests when trying to parse markdown that has this specific nesting pattern.

---
Repository: /testbed
