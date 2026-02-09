# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown. When using backticks to create inline code spans, the parser seems to be matching closing backticks incorrectly. Specifically, if I have inline code with different numbers of opening and closing backticks, the behavior is unexpected.

### Reproduction

```markdown
This is `code` with single backticks - works fine

This is ``code`` with double backticks - also works

But when I try ``code` (two opening, one closing) or `code`` (one opening, two closing), the parsing doesn't work as expected
```

The issue appears when the number of opening and closing backticks don't match exactly. The parser seems to be accepting any number of closing backticks that is greater than or equal to the opening count, rather than requiring an exact match.

### Expected behavior

Inline code should only close when the exact same number of backticks is encountered. For example:
- `` `code` `` should work
- `` ``code`` `` should work  
- `` ``code` `` should NOT close the code span (should keep looking for two backticks)
- `` `code`` `` should NOT close the code span (should keep looking for one backtick)

### System Info
- Using remark@15.0.1
- This affects markdown parsing in general

---
Repository: /testbed
