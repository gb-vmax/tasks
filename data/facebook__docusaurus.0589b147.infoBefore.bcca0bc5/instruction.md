# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX. When parsing code blocks, the behavior seems incorrect - the parser is not properly handling interrupt conditions for code fences, which affects how code blocks are recognized in certain contexts.

### Reproduction

```mdx
Some text
```js
const example = 'test'
```
More text
```

When the code fence appears in an interrupt context (like directly after text without a blank line), the parsing behavior is inverted from what it should be. The fence is either recognized when it shouldn't be, or not recognized when it should be.

### Expected behavior

Code fences should be properly recognized based on the interrupt state. The parser should correctly determine whether a code fence can interrupt the current context and handle the continuation logic appropriately.

### Additional context

This appears to be related to how the `infoBefore` function handles the interrupt check and the order of callbacks passed to `effects.check()`. The current logic seems to have the conditions backwards.

---
Repository: /testbed
