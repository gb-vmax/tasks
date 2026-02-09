# Bug Report

### Describe the bug

I'm encountering an issue with link parsing in markdown when the link is followed by a caret character (`^`). The parser seems to be rejecting valid links in this scenario, even though they should be accepted according to CommonMark spec.

### Reproduction

```markdown
[link text](url)^some text after
```

When parsing the above markdown, the link is not being recognized properly when followed by `^`. The parser appears to be treating this as invalid syntax.

### Expected behavior

The link should be parsed correctly regardless of whether it's followed by a `^` character. The caret is just regular text that comes after the link and shouldn't affect link parsing.

### Additional context

This seems to be related to the footnote support logic. The parser is incorrectly handling the case where a link is followed by `^` even when footnote support is not enabled or relevant to the current context.

---
Repository: /testbed
