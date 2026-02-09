# Bug Report

### Describe the bug

I'm encountering an issue with MDX link parsing where links with unbalanced parentheses in the URL are not being parsed correctly. When a URL contains parentheses that don't have matching pairs, the link destination parsing fails or produces unexpected results.

### Reproduction

```mdx
[Link text](https://example.com/page)

[Another link](https://example.com/path(with)parens)
```

The first link works fine, but when trying to parse links with parentheses in the URL (like Wikipedia URLs or other sites that use parentheses in their paths), the parser doesn't handle them properly.

### Expected behavior

Links with parentheses in the URL should be parsed correctly, even when the parentheses are not balanced or when there's only an opening parenthesis without a closing one. The parser should recognize the end of the URL based on whitespace or end of line, not just on parenthesis balance.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
