# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the closing fence validation seems to be incorrect. When I use a directive container with a closing fence that has the same number of colons as the opening fence, it's not being recognized properly.

### Reproduction

```markdown
:::note
Some content here
:::
```

The closing fence `:::` should properly close the container that was opened with `:::`, but it appears the parser is rejecting it. This happens specifically when the opening and closing fences have exactly the same number of colons.

### Expected behavior

A directive container should be properly closed when the closing fence has the same number of colons (or more) as the opening fence. The closing `:::` should match and close the opening `:::`.

### Additional context

This seems to have started happening recently. I noticed that containers with more colons in the closing fence than the opening fence work fine (e.g., opening with `:::` and closing with `::::`), but equal-length fences don't work as expected.

---
Repository: /testbed
