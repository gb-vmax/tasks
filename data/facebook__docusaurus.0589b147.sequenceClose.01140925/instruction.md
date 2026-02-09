# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in markdown. When using backticks to create inline code spans, the parser seems to be matching closing backticks incorrectly. Specifically, if I have more closing backticks than opening backticks, the code span is still being closed even though it shouldn't match.

### Reproduction

```markdown
`code with extra backticks``
```

The above should only match a single backtick opener with a single backtick closer, leaving the extra backtick as plain text. However, it appears to be treating the double backticks at the end as a valid closing sequence.

Another example:
```markdown
`inline code```
```

This should leave the extra backticks unmatched, but the parser seems to be accepting the longer closing sequence.

### Expected behavior

Inline code spans should only close when the number of backticks in the closing sequence exactly matches the number in the opening sequence. If there are more backticks in the closing sequence, they should not match and should be treated as literal text.

For example:
- `` `code` `` should work (1 backtick opens, 1 backtick closes)
- `` `code`` `` should NOT close the code span (1 backtick opens, 2 backticks don't match)
- ``` ``code`` ``` should work (2 backticks open, 2 backticks close)

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
