# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing in remark-directive. When using container directives with closing fences, the parser is not correctly handling certain edge cases with the fence sequences.

### Reproduction

```markdown
::: myDirective
Content here
:::
```

When the closing fence has a specific number of colons, the directive doesn't parse correctly. The parser seems to be rejecting valid closing fences or accepting invalid ones.

For example:
- A closing fence with the same number of colons as the opening should close the container
- A closing fence with fewer colons should not close the container

But the behavior I'm seeing is inconsistent with what I'd expect from the markdown spec.

### Expected behavior

The container directive should properly match opening and closing fences based on the number of colons in the sequence. A closing fence should only be valid if it has at least as many colons as the opening fence, and it should be on its own line (or followed only by whitespace).

### Additional context

This affects parsing of nested directives and edge cases where the closing fence might have extra characters or unusual formatting. The issue seems related to how the parser validates the closing fence sequence length and checks for end-of-line conditions.

---
Repository: /testbed
