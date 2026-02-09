# Bug Report

### Describe the bug

I'm encountering an issue where calling methods on a frozen processor doesn't throw an error as expected. It seems like the validation logic for frozen processors is inverted - operations that should be blocked on frozen processors are being allowed, and vice versa.

### Reproduction

```js
// Create and freeze a processor
const processor = unified().freeze()

// This should throw an error but doesn't
processor.use(somePlugin)

// Meanwhile, calling methods on an unfrozen processor throws an error incorrectly
const unfrozenProcessor = unified()
unfrozenProcessor.use(somePlugin) // Throws error unexpectedly
```

### Expected behavior

- Calling methods like `use()` on a **frozen** processor should throw an error with a message about creating a new processor
- Calling methods on an **unfrozen** processor should work normally without throwing errors

Currently it seems to be doing the opposite - unfrozen processors are throwing errors while frozen ones are not.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
