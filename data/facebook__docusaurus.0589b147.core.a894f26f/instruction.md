# Bug Report

### Describe the bug

I'm experiencing an issue with HTML entity encoding when using the `subset` option. It seems like characters that should be encoded based on the subset pattern are being left unprocessed.

### Reproduction

```js
const result = core('Test "quoted" & <tag>', {
  subset: /["&<>]/g,
  format: (code) => `&#x${code.toString(16)};`
});

// Expected: Test &#x22;quoted&#x22; &#x26; &#x3c;tag&#x3e;
// Actual: Test "quoted" & <tag>
```

When I specify a `subset` option to control which characters get encoded, the function returns the original string unchanged instead of applying the encoding to the matched characters.

### Expected behavior

Characters matching the `subset` pattern should be encoded according to the provided format function, even when `escapeOnly` is not set.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
