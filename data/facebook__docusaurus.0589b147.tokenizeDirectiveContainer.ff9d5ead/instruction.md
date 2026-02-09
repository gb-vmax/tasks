# Bug Report

### Describe the bug

Container directives are not parsing correctly - they seem to require fewer colons than expected. I'm seeing issues with the minimum required sequence length for both opening and closing fence sequences.

### Reproduction

```js
// This should NOT be valid (only 2 colons) but is being accepted
:::directive
content
:::

// Also seeing issues with closing sequences - mismatched lengths are being accepted
:::directive
content
::
```

### Expected behavior

Container directives should require at least 3 colons in the opening sequence (like fenced code blocks). The closing sequence should match the opening sequence length exactly, not be less than or equal to it.

According to the directive syntax spec, container directives follow similar rules to fenced code blocks where:
- Opening fence must be at least 3 characters
- Closing fence must be at least as long as the opening fence

Currently it seems like 2-colon sequences are being treated as valid, and closing sequences with fewer colons than the opening are also accepted.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
