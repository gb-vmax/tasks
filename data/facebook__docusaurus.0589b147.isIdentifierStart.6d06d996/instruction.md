# Bug Report

### Describe the bug

I'm encountering an issue with MDX identifier parsing where certain valid identifier characters are not being recognized correctly. Specifically, the characters `[` (code 91) and `{` (code 123) are being rejected as valid identifier start characters even though they should be accepted based on the identifier naming rules.

### Reproduction

```js
// These identifiers should be valid but are being rejected
const component1 = <Component name="test[" />
const component2 = <Component name="test{" />

// The parser fails to recognize these as valid identifier characters
```

When trying to use bracket or brace characters in certain contexts within MDX, the parser incorrectly rejects them.

### Expected behavior

The identifier parser should correctly handle all valid identifier start characters according to the specification. Characters with codes 91 and 123 should be properly recognized when they're valid in the context.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
