# Bug Report

### Describe the bug

I'm encountering an issue with directive containers in remark-directive where the closing sequence validation seems to be off. When I try to use a directive container with the same number of colons for opening and closing, it's not being recognized properly.

### Reproduction

```markdown
:::note
This is a note
:::
```

The parser doesn't seem to accept this as a valid directive container even though the opening and closing sequences match (both have 3 colons). It appears that the closing sequence needs to have MORE colons than the opening sequence for it to work, which doesn't seem right.

### Expected behavior

A directive container should be valid when the closing sequence has the same number (or more) colons as the opening sequence. The example above with `:::` for both open and close should parse correctly as a valid directive container.

### System Info
- remark-directive version: 3.0.0
- Using this in a Jest environment

---
Repository: /testbed
