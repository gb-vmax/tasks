# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the closing fence sequence doesn't behave correctly. When I have a container directive with a specific number of colons in the opening fence, the closing fence with the same number of colons is not being recognized properly.

### Reproduction

```markdown
:::note
Some content here
:::
```

The parser seems to have trouble matching the closing fence. It appears that when the opening and closing sequences have exactly the same number of colons, the container doesn't close as expected.

### Expected behavior

The directive container should properly close when the closing fence has the same number of colons (or more) as the opening fence. The parser should correctly identify matching fence sequences.

For example:
- Opening with `:::` should close with `:::` or `::::`
- The content between the fences should be properly contained

### Additional context

This seems related to how the tokenizer handles the sequence counting logic when processing the closing fence. The issue manifests when trying to parse standard container directive syntax.

---
Repository: /testbed
