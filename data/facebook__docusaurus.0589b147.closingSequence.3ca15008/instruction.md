# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers in remark-directive where the closing fence sequence is not being validated correctly. When I try to close a container directive with a fence that should match the opening fence, it's either not closing properly or closing when it shouldn't.

### Reproduction

```markdown
:::note
This is a container directive
:::
```

The closing `:::` sequence doesn't seem to be matching the opening sequence correctly. Sometimes containers that should close don't close, and sometimes they close when they shouldn't based on the fence length.

### Expected behavior

The closing fence sequence should properly match the opening fence sequence length. A container opened with `:::` should only close with `:::` (same number of colons), and a container opened with `::::` should only close with `::::`.

### Additional context

This seems to affect how nested or adjacent directive containers are parsed. The validation logic for matching opening and closing fences appears to be inconsistent.

---
Repository: /testbed
