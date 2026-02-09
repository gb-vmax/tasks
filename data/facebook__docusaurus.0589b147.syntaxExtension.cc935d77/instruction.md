# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extension merging in MDX. When using custom syntax extensions, the extensions aren't being properly combined with existing ones. It seems like the extension constructs are being written to the wrong object, causing my custom syntax handlers to not work as expected.

### Reproduction

```js
const customExtension = {
  flow: {
    42: {
      tokenize: function(effects, ok, nok) {
        // custom tokenizer
      }
    }
  }
}

// Try to merge with existing extensions
const combined = syntaxExtension(baseExtensions, customExtension)

// Custom extension doesn't appear in the merged result
// Instead, the wrong object gets modified
```

### Expected behavior

When merging syntax extensions, the custom extension constructs should be properly added to the combined result. Both the base extensions and the new extensions should be available in the final merged object.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
