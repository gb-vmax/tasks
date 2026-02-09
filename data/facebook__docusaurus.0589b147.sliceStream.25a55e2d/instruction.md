# Bug Report

### Describe the bug

I'm experiencing an issue with token slicing in the MDX parser. When processing tokens, it seems like the first character or element is being incorrectly skipped, which leads to malformed output or parsing errors.

### Reproduction

```js
// When parsing MDX content with tokens
const token = {
  type: 'text',
  value: 'Hello World',
  // ... other token properties
}

// The sliceStream function now skips the first element
// Expected: 'Hello World'
// Actual: 'ello World' (first character missing)
```

This affects any MDX content being processed through the tokenizer, causing the first character of tokens to be dropped during serialization.

### Expected behavior

The `sliceStream` function should process the entire token without skipping any characters. All token content should be preserved during the slicing operation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently and is breaking our MDX rendering pipeline. Any help would be appreciated!

---
Repository: /testbed
