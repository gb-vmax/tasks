# Bug Report

### Describe the bug

After a recent update, the `createProcessor()` function from `@mdx-js/mdx` is returning an object with methods instead of the expected processor instance. This breaks existing code that relies on the standard processor API.

### Reproduction

```js
import { createProcessor } from '@mdx-js/mdx'

const processor = createProcessor()

// This now fails - processor doesn't have the expected methods
processor.use(remarkGfm)
processor.process('# Hello')
```

The function now returns a custom object with `process`, `transform`, `validate`, and `reset` methods, but these don't match the unified processor interface that's expected.

### Expected behavior

`createProcessor()` should return a unified processor instance that supports the standard processor methods like `use()`, `parse()`, `stringify()`, etc. The returned value should be compatible with the unified ecosystem and allow chaining plugins.

### Additional context

This appears to have changed the entire return type and behavior of the function. Code that was working before now throws errors because the processor doesn't have methods like `use()` or behave like a standard unified processor.

---
Repository: /testbed
