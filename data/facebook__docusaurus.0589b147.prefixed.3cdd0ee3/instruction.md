# Bug Report

### Describe the bug

I'm encountering an issue with code block parsing in markdown. When I have indented code blocks (4+ spaces), they're not being recognized correctly. The parser seems to be treating them as regular text instead of code blocks.

### Reproduction

```markdown
This is a paragraph.

    This should be a code block
    with multiple lines
    indented by 4 spaces

But it's not being parsed as code.
```

When parsing the above markdown, the indented section should be recognized as a code block, but it's being treated as normal paragraph text instead.

### Expected behavior

Text indented by 4 or more spaces should be parsed as a code block. This is standard markdown syntax and was working in previous versions.

### Additional context

This seems to have started happening recently. I'm using the remark parser and the issue appears to be related to how continuation lines are being processed for indented content.

---
Repository: /testbed
