# Bug Report

### Describe the bug

I'm encountering an issue with link destination parsing in MDX. When using angle bracket notation for links (e.g., `<url>`), the parser is incorrectly handling the opening `<` character, which causes the link to be parsed as raw text instead of an enclosed destination.

### Reproduction

```markdown
[link text](<https://example.com>)
```

Expected: The URL should be parsed as an enclosed destination (angle bracket format)
Actual: The URL is being parsed as raw text, breaking the link syntax

This also affects other angle bracket enclosed destinations:
```markdown
[another link](<path/to/file.md>)
```

### Expected behavior

Links with angle bracket enclosed destinations should be correctly parsed and recognized. The `<` character (code 60) should trigger the enclosed destination parsing path, not the raw destination path.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have broken recently, as angle bracket notation for links was working in previous versions. The parser seems to be taking the wrong branch when it encounters the opening angle bracket.

---
Repository: /testbed
