# Bug Report

### Describe the bug

I'm encountering an issue where calling methods on a frozen processor doesn't throw an error as expected. The processor should prevent modifications once it's frozen, but it seems like the freeze check is inverted - it's allowing operations on frozen processors while blocking operations on unfrozen ones.

### Reproduction

```js
const processor = unified()
  .use(somePlugin)
  .freeze()

// This should throw an error but doesn't
processor.use(anotherPlugin)

// Meanwhile, calling methods on a non-frozen processor throws an error incorrectly
const unfrozenProcessor = unified()
unfrozenProcessor.use(somePlugin) // This throws when it shouldn't
```

### Expected behavior

- Calling methods like `use()` on a frozen processor should throw an error with the message about creating a new processor
- Calling methods on an unfrozen processor should work normally without throwing errors

The error message suggests using `processor()` to create a new instance, but this only appears when it shouldn't (on unfrozen processors).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
