# Bug Report

### Describe the bug

Markdown links with empty destinations are not being parsed correctly. When a link has no URL (just parentheses with nothing inside), the parser fails to handle it properly.

### Reproduction

```markdown
[link text]()
```

When parsing this markdown, the link is not recognized or processed as expected. The parser seems to be checking for the wrong character code when determining if a resource destination is empty.

### Expected behavior

Links with empty destinations should be parsed correctly. The parser should properly detect when the closing parenthesis is encountered immediately after the opening parenthesis (indicating an empty destination) and handle this case appropriately.

### Additional context

This appears to affect basic markdown link syntax where the destination URL is optional or empty. The issue manifests when processing link references that have the format `[text]()` with no content between the parentheses.

---
Repository: /testbed
