# Bug Report

### Describe the bug

I'm encountering an issue with link parsing in MDX where links with empty destinations are not being handled correctly. When a link has no URL (just empty parentheses), the parser seems to be processing it incorrectly.

### Reproduction

```markdown
[link text]()
```

When parsing this MDX content, the link with empty parentheses `()` doesn't get processed as expected. The parser appears to be treating the closing parenthesis incorrectly.

### Expected behavior

Links with empty destinations should be parsed correctly. The parser should recognize `()` as an empty resource and handle it appropriately without throwing errors or producing malformed output.

### Additional context

This seems to affect basic link syntax where the destination URL is omitted but the parentheses are still present. Regular links with URLs work fine, but the edge case of empty parentheses is problematic.

---
Repository: /testbed
