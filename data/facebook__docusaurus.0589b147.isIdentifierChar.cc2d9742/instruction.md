# Bug Report

### Describe the bug

I'm encountering an issue with identifier parsing in MDX content. Certain valid characters that should be allowed in identifiers are being rejected, causing parsing errors.

### Reproduction

When using identifiers that contain specific boundary characters (like `:` or `[`), the parser incorrectly treats them as invalid:

```mdx
export const test:value = 123;
```

or 

```mdx
export const test[index] = 'value';
```

These should be valid in certain contexts but are being rejected by the identifier character validation.

### Expected behavior

The parser should correctly identify valid identifier characters according to the specification. Characters at certain code point boundaries should be properly handled.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
