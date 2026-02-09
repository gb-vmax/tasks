# Bug Report

### Describe the bug

I'm experiencing an issue with directive text labels in remark-directive. The label parsing seems to be broken - when I use text directives with labels, the markers and strings are not being processed in the correct order.

### Reproduction

```js
const input = ':directive[label text]{attr=value}'

// Parse the directive
const result = parse(input)

// The label markers and strings appear to be swapped
// Expected structure is not matching actual output
```

### Expected behavior

Text directive labels should be parsed correctly with proper marker and string identification. The label should be extracted as expected and the directive should maintain its proper structure.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to have broken recently, possibly after a refactoring of the tokenizer functions. The label parsing worked fine in earlier versions.

---
Repository: /testbed
