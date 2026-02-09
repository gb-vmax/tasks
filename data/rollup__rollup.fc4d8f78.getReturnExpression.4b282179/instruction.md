# Bug Report

### Describe the bug

I'm experiencing an issue where function return values are not being properly analyzed in certain cases. It seems like the return expression is being computed incorrectly, leading to unexpected behavior during bundling.

### Reproduction

```js
function getValue() {
  return someExpression;
}

const result = getValue();
// The return value analysis appears to be incorrect here
```

When the function's return value is accessed, it seems like the return expression is being updated at the wrong time, causing the analysis to fail or produce incorrect results.

### Expected behavior

The return expression should be correctly computed and cached when first requested, not updated when it already exists. This is causing issues with tree-shaking and dead code elimination in my builds.

### Additional context

This appears to be related to how return value scopes handle expression caching. The logic for when to update the return expression seems inverted - it's updating when it shouldn't and not updating when it should.

---
Repository: /testbed
