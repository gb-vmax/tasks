# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where links with parentheses in the URL are being parsed incorrectly. When a URL contains parentheses (like Wikipedia links or other URLs with special characters), the parser seems to be treating the opening parenthesis as the start of a title instead of part of the URL.

### Reproduction

```markdown
[Link text](https://example.com/page_(disambiguation))
```

When parsing this markdown, the link doesn't work as expected. The URL gets truncated or the parser throws an error because it's treating the `(` in the URL as something else.

Also happens with:
```markdown
[Wikipedia](https://en.wikipedia.org/wiki/Example_(concept))
```

### Expected behavior

The parser should correctly handle URLs that contain parentheses as part of the URL path. These are valid URLs and should be parsed as the destination, not confused with title syntax.

### System Info
- remark version: 15.0.1

This seems to have broken recently - URLs with parentheses used to work fine. Any help would be appreciated!

---
Repository: /testbed
