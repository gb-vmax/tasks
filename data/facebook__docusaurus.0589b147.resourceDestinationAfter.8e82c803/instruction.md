# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where whitespace handling in resource URLs seems to be broken. Links with certain whitespace patterns are not being parsed correctly.

### Reproduction

```markdown
[link](https://example.com/path  )
```

When processing markdown links that have trailing spaces or specific whitespace patterns in the URL portion, the parser doesn't handle them as expected. The link either fails to parse entirely or produces unexpected output.

### Expected behavior

The parser should correctly handle whitespace in resource destinations according to the markdown spec. Links with trailing or embedded whitespace should be processed consistently.

### Additional context

This seems to affect the tokenization logic for resource destinations in links. The issue appears when the parser encounters whitespace after the destination URL but before the closing parenthesis.

---
Repository: /testbed
