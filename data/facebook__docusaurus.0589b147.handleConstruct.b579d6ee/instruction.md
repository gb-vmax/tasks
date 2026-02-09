# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain constructs are being incorrectly rejected during tokenization. It appears that the logic for checking whether a construct should be disabled has been inverted, causing valid constructs to be rejected and disabled constructs to be processed.

### Reproduction

```js
// When parsing MDX content with custom constructs
const result = await compile('# My heading\n\nSome content', {
  remarkPlugins: [
    // plugin with custom construct
  ]
})

// The construct gets rejected even though it's not in the disable list
// This causes parsing to fail or produce unexpected output
```

### Expected behavior

Constructs that are NOT in the disable list should be processed normally. Only constructs explicitly added to `context.parser.constructs.disable.null` should be rejected with `nok`.

Additionally, the `context.currentConstruct` should be set when the construct is NOT partial, not when it IS partial.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken parsing for several standard MDX elements. Any help would be appreciated!

---
Repository: /testbed
