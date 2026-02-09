# Bug Report

### Describe the bug

I'm encountering an issue with link parsing in MDX where links followed by a caret character (`^`) are not being processed correctly. It seems like the parser is rejecting valid link syntax when a `^` character appears immediately after the closing bracket.

### Reproduction

```markdown
[link text](url)^some text
```

When the above MDX content is parsed, the link is not recognized properly. The parser appears to be incorrectly handling the case where a caret follows a link.

### Expected behavior

The link should be parsed normally regardless of what character follows it (including `^`). The caret character and subsequent text should be treated as separate content after the link.

For example:
```markdown
[click here](https://example.com)^footnote
```

Should parse the link `[click here](https://example.com)` correctly, with `^footnote` as following text.

### System Info
- @mdx-js/mdx version: 3.0.0
- Parser: micromark-based

This seems to have started happening recently. Links work fine when not followed by `^`, but fail when they are.

---
Repository: /testbed
