# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where calling methods on an unfrozen processor throws an error about it being frozen. This seems backwards - the error is being thrown when the processor is NOT frozen, which prevents me from using a working processor instance.

### Reproduction

```js
const processor = unified().use(remarkParse).use(remarkMdx);

// This should work but throws an error
processor.parse('# Hello');
```

The error message says:
```
Cannot call `` on a frozen processor.
Create a new processor first, by calling it: use `processor()` instead of `processor`.
```

This happens when trying to use any method on a processor that should be usable. It seems like the frozen check is inverted - it's preventing operations on processors that aren't frozen, when it should be doing the opposite.

### Expected behavior

Methods should be callable on unfrozen processors. The error should only be thrown when trying to call methods on a processor that has been frozen, not on a regular working processor instance.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
