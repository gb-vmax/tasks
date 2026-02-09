# Bug Report

### Describe the bug

I'm experiencing an issue with character escaping in regular expressions. When processing certain special characters, some of them are not being properly escaped, which causes unexpected behavior in pattern matching.

### Reproduction

```js
// When using special characters that should be escaped
const input = "test{content}more";
const subset = ['{', '}'];

// The resulting regex doesn't match correctly
// Expected to match both { and } characters
// But the pattern seems to be missing some characters
```

After some investigation, it looks like the regex pattern being generated is incomplete - not all special characters from the input subset are being included in the final expression.

### Expected behavior

All characters in the subset should be properly escaped and included in the resulting regular expression pattern. The pattern should match all characters that were provided in the input array.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
