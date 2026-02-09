# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where linked text chunks are not being properly connected. It seems like the reference chain between consecutive text tokens is broken, causing the `previous` and `next` pointers to not link correctly.

### Reproduction

When parsing markdown content with multiple text chunks, the token chain appears to be malformed:

```js
// Parse markdown with consecutive text content
const result = remark.parse('Some text content here');

// The token.next reference points to itself instead of the next token
// This breaks any logic that relies on traversing the token chain
```

### Expected behavior

Text chunk tokens should maintain proper bidirectional links where:
- `token.next` points to the following token
- The following token's `previous` points back to the current token

Currently, it seems like the `previous` reference is being set after the condition check, which causes the logic to fail since `previous2` would always be the current token when checking `if (previous2)`.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
