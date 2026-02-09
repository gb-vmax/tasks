# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where syntax extensions are not being properly merged. When adding custom syntax extensions, they seem to be overwriting existing handlers instead of being added alongside them.

### Reproduction

```js
const processor = remark()
  .use(pluginA) // Adds handler for code 'X'
  .use(pluginB) // Also adds handler for code 'X'

// Expected: Both handlers should be present
// Actual: Only one handler is registered
```

When multiple plugins try to register handlers for the same syntax code, only the first one gets registered. The subsequent plugins' handlers are being ignored completely.

### Expected behavior

Multiple syntax extension handlers for the same code should be merged into an array, allowing both plugins to work together. The parser should call all registered handlers in sequence.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is blocking our use case where we need to chain multiple transformations on the same syntax elements. Any help would be appreciated!

---
Repository: /testbed
