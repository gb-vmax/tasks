# Bug Report

### Describe the bug

I'm encountering an issue with markdown space handling where consecutive spaces aren't being processed correctly. It seems like the token entry is happening at the wrong time, causing spaces to not be properly grouped together.

### Reproduction

```js
// When parsing markdown with multiple consecutive spaces
const markdown = "text    more text"; // 4 spaces between words

// The spaces are not being tokenized as a single group
// Instead, each space seems to create its own token or they're being handled incorrectly
```

### Expected behavior

Multiple consecutive spaces should be grouped together and entered as a single token of the appropriate type, with the token entry happening before consuming the first space character.

### System Info
- remark version: 15.0.1

This is affecting markdown parsing where whitespace handling is critical. The issue appears to be related to how the `factorySpace` function manages token creation timing.

---
Repository: /testbed
