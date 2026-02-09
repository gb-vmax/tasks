# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where links with parentheses in the URL are not being handled correctly. When a URL contains parentheses (like Wikipedia links or other URLs with special characters), the parser seems to be cutting off the URL prematurely or not recognizing it as a valid link resource.

### Reproduction

```markdown
[Example link](https://en.wikipedia.org/wiki/Example_(disambiguation))
```

When parsing the above markdown, the link doesn't work as expected. The URL should include the full path with the parentheses, but it appears the parser is treating the opening parenthesis in the URL as something else.

Also seeing similar issues with:
```markdown
[Link with title](https://example.com/path "title text")
```

The title parsing seems to be affected when there are parentheses involved in the resource section.

### Expected behavior

The parser should correctly handle URLs containing parentheses and properly parse the resource section of markdown links, including both the URL and optional title text. Links like Wikipedia URLs with disambiguation pages should work without issues.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
