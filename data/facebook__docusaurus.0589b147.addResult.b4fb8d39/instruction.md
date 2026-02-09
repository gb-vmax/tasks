# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where constructs with `resolveAll` are being added to the `resolveAllConstructs` array even when they're already present. This appears to be causing duplicate processing of certain markdown elements.

### Reproduction

```js
// When parsing markdown with constructs that have resolveAll defined
const parser = createParser();
const construct = {
  resolveAll: (events) => { /* ... */ },
  resolve: (events) => { /* ... */ }
};

// The construct gets added multiple times to resolveAllConstructs
// causing it to be resolved multiple times
```

### Expected behavior

Constructs with `resolveAll` should only be added to the `resolveAllConstructs` array once, not every time they're encountered during parsing. The array should act as a set to prevent duplicate entries.

### Additional context

This seems to affect parsing performance and may lead to incorrect output when the same construct is processed multiple times. The logic appears to be inverted - it's adding constructs when they're already in the array instead of when they're not.

---
Repository: /testbed
