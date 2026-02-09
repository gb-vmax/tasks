# Bug Report

### Describe the bug

When parsing markdown lists, whitespace handling in list item prefixes appears to be broken. The parser is now accepting list items without proper whitespace after the list marker, which doesn't follow standard markdown syntax.

### Reproduction

```markdown
1.Item without space after period
2.Another item without space
```

This should not be recognized as a valid list, but it seems to be parsed as one now.

Expected markdown:
```markdown
1. Item with proper space
2. Another item with proper space
```

### Expected behavior

List items should require at least one whitespace character after the list marker (e.g., `1.`, `-`, `*`) to be considered valid. Without this whitespace, the text should not be parsed as a list item.

### Additional context

This seems to have started happening recently. The parser is being too lenient with list syntax validation, which could lead to unexpected parsing results when processing markdown documents.

---
Repository: /testbed
