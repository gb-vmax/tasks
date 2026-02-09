# Bug Report

### Describe the bug

I'm encountering an issue with parsing numeric literals in MDX. It appears that bigint literals are not being parsed correctly - the raw value seems to be missing the first character and the bigint suffix detection is failing.

### Reproduction

When parsing MDX content that contains bigint literals, the parser doesn't correctly capture the full literal value. For example:

```js
// MDX content with bigint
const value = 123456789n;
```

The raw representation of the literal appears to be incorrectly sliced, starting from position `this.start + 1` instead of `this.start`, which causes the first character to be missing. Additionally, the bigint suffix check is looking for character code 78 (uppercase 'N') instead of 110 (lowercase 'n'), which means lowercase bigint literals won't be recognized properly.

### Expected behavior

- The raw literal value should include all characters from start to end
- Bigint literals ending with lowercase 'n' should be correctly identified and parsed
- The bigint property should be properly set with the numeric part (without the 'n' suffix)

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: latest

---
Repository: /testbed
