# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in MDX where links followed by a caret character (`^`) are not being processed correctly. The parser seems to be handling the `_hiddenFootnoteSupport` construct check in reverse, causing links to be rejected when they should be accepted and vice versa.

### Reproduction

```markdown
[link text](url)^

[another link](https://example.com)^some text
```

When parsing the above MDX content, links that are followed by a `^` character are either incorrectly accepted or rejected depending on whether `_hiddenFootnoteSupport` is present in the parser constructs.

### Expected behavior

Links should be parsed correctly regardless of whether they're followed by a caret character, with proper handling of the `_hiddenFootnoteSupport` construct check. The labelMarker exit should also occur in the correct order relative to labelLink.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
