# Bug Report

### Describe the bug

I'm experiencing an issue where calling methods on a frozen processor is not throwing an error as expected. It seems like the validation logic is inverted - the processor allows method calls when it should be frozen and blocks them when it shouldn't be.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .freeze()

// This should throw an error but doesn't
processor.use(somePlugin)

// Meanwhile, calling methods on a non-frozen processor throws an error when it shouldn't
const unfrozenProcessor = unified()
  .use(remarkParse)

// This throws an error unexpectedly
unfrozenProcessor.use(anotherPlugin)
```

### Expected behavior

- Calling methods like `.use()` on a **frozen** processor should throw an error with message about creating a new processor
- Calling methods on a **non-frozen** processor should work normally without throwing errors

Currently, the behavior appears to be reversed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
