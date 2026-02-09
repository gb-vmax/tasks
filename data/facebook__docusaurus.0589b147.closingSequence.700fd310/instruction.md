# Bug Report

### Describe the bug

I'm encountering an issue with directive containers in remark-directive where the closing fence validation seems to be off. When I try to use a directive container with a closing fence that has the same number of colons as the opening fence, it's not being recognized properly.

### Reproduction

```markdown
:::note
This is a note
:::
```

The closing `:::` should match the opening `:::` and properly close the container, but it appears the parser is not accepting it as a valid closing fence.

### Expected behavior

When the closing fence has the same number of colons (3 in this case) as the opening fence, it should be recognized as a valid closing sequence and the directive container should be properly closed.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
