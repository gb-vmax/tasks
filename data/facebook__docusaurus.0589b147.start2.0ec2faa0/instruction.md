# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain constructs are being incorrectly rejected or accepted. It seems like the tokenizer is applying the wrong logic when checking whether a construct should be disabled.

### Reproduction

When trying to parse MDX content with specific constructs, I'm seeing unexpected behavior:

```js
// MDX content that should be parsed correctly
const mdxContent = `
# Heading

Some content with constructs that should work
`;

// The parser is rejecting valid constructs or accepting disabled ones
const result = compile(mdxContent, {
  /* ... options ... */
});
```

The issue appears to be related to how partial constructs and disabled constructs are being handled during tokenization. Valid constructs are being rejected when they shouldn't be, and the `currentConstruct` context seems to be set incorrectly.

### Expected behavior

- Partial constructs should be handled correctly according to their configuration
- Disabled constructs should be properly rejected
- Non-disabled constructs should be allowed to proceed with tokenization

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression in the tokenizer logic. Any help would be appreciated!

---
Repository: /testbed
