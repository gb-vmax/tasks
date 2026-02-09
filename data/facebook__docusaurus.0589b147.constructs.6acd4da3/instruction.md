# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where certain syntax extensions aren't being properly recognized or applied. It seems like constructs that should be added "before" existing ones are not being inserted at the correct position, causing parsing to fail or produce unexpected results.

### Reproduction

```js
// When trying to parse MDX with custom syntax extensions
const parser = unified()
  .use(remarkParse)
  .use(remarkMdx, {
    extensions: [
      {
        add: 'before',
        // ... extension config
      }
    ]
  })

// The extension doesn't seem to take effect properly
// Expected: Extension should be applied before existing constructs
// Actual: Extension is not being applied in the correct order
```

### Expected behavior

Custom syntax extensions with `add: 'before'` should be inserted at the beginning of the constructs array, allowing them to be processed before the default constructs. The parser should correctly handle the ordering of syntax extensions.

### Additional context

This appears to affect the internal construct handling in the micromark syntax extension logic. The issue manifests when multiple extensions are registered and their ordering matters for correct parsing behavior.

---
Repository: /testbed
