# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing where backtick sequences in code spans are not being handled correctly. When I use multiple backticks to delimit inline code (like ``` `` ` `` ```), the parser seems to be matching them incorrectly.

### Reproduction

```markdown
This is `normal code` which works fine.

But this `` code with `backtick` inside `` doesn't parse correctly.

And this ``` code with ``two backticks`` inside ``` also fails.
```

When parsing the above markdown, the inline code blocks with nested backticks don't get recognized properly. The closing backtick sequence doesn't match up with the opening sequence as expected.

### Expected behavior

According to CommonMark spec, inline code should allow you to use multiple backticks as delimiters, and the opening and closing sequences must have the same number of backticks. For example:
- `` ` `` should render as a single backtick
- ``` `` ``` should render as two backticks

The parser should correctly match opening and closing sequences of the same length.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
