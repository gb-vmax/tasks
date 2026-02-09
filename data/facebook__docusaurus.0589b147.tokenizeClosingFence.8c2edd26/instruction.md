# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where closing fences with more colons than the opening fence are not being properly rejected. The parser seems to accept closing sequences that exceed the opening sequence length, which shouldn't be valid according to the directive syntax specification.

### Reproduction

```markdown
::: note
This is a container directive
::::
```

In this example, the opening fence has 3 colons (`:::`) but the closing fence has 4 colons (`::::`). The parser currently accepts this as valid, but it should reject the closing fence since it has more colons than the opening fence.

Another example:
```markdown
:::: warning
Content here
::::::
```

Opening has 4 colons, closing has 6 - this should also be rejected but is currently being accepted.

### Expected behavior

The parser should only accept closing fences that have **exactly** the same number of colons as the opening fence, or potentially fewer (depending on the spec). Closing fences with more colons than the opening should be treated as content, not as a valid closing fence.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems like it could lead to unexpected parsing behavior when users accidentally add extra colons in their closing fences. Would appreciate if this could be looked into!

---
Repository: /testbed
