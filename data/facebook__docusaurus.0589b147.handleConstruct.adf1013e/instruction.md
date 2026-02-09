# Bug Report

### Describe the bug

When parsing markdown with disabled constructs, the parser is incorrectly rejecting constructs that should be allowed. It seems like the logic for checking whether a construct is disabled has been inverted - constructs that are NOT in the disable list are being rejected instead of the ones that ARE in the list.

### Reproduction

```js
const processor = remark()
  .use(() => (tree, file) => {
    file.parser.constructs.disable.null = ['emphasis']
  })

const result = processor.processSync('This is **bold** text')
// Expected: bold text should be parsed normally
// Actual: bold text is being rejected even though it's not in the disable list
```

### Expected behavior

Only constructs that are explicitly listed in `context.parser.constructs.disable.null` should be disabled. Other constructs should continue to work normally.

Currently, it appears that constructs NOT in the disable list are being rejected, which is the opposite of the intended behavior.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
