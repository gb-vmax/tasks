# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where the closing sequence isn't being properly validated. When using nested directive containers with different numbers of colons, the parser seems to be accepting closing sequences that should be rejected.

### Reproduction

```markdown
:::note
This is a note
::
```

The above should not be valid since the closing sequence (`::`) has fewer colons than the opening sequence (`:::`), but it appears to be accepted as a valid closing fence.

Similarly:

```markdown
:::warning
Content here
::::
```

This also seems to behave unexpectedly - a closing sequence with more colons than the opening should not match.

### Expected behavior

The parser should only accept a closing sequence that has **exactly** the same number of colons as the opening sequence. A closing sequence with fewer or more colons should not close the directive container.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
