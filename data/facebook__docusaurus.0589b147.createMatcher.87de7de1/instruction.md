# Bug Report

### Describe the bug

I'm experiencing an issue with pattern matching where an empty pattern array behaves unexpectedly. When I pass an empty array to the matcher function, it seems to match everything instead of matching nothing.

### Reproduction

```js
const matcher = createMatcher([]);

// This returns true but I would expect false
console.log(matcher('some-file.md')); // true
console.log(matcher('any-string')); // true
```

When no patterns are provided, I would expect the matcher to reject all inputs since there are no patterns to match against. However, it appears to be accepting everything.

### Expected behavior

When an empty pattern array is provided, the matcher should return `false` for all inputs since there are no patterns to match. Currently it's returning `true` for everything.

### System Info
- Package: @docusaurus/utils
- Using the `createMatcher` function from `globUtils`

---
Repository: /testbed
