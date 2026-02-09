# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic import expressions where attributes are not being included correctly. It seems like there's a problem with how the `shouldIncludeDynamicAttributes` property is being set - the behavior is inverted from what I expect.

### Reproduction

```js
// When setting shouldIncludeDynamicAttributes to true
importExpression.shouldIncludeDynamicAttributes = true;

// The attributes are NOT included (but they should be)
// Conversely, when setting it to false:
importExpression.shouldIncludeDynamicAttributes = false;

// The attributes ARE included (which is the opposite of expected)
```

### Expected behavior

When `shouldIncludeDynamicAttributes` is set to `true`, dynamic attributes should be included in the import expression. When set to `false`, they should not be included.

Currently the behavior appears to be inverted - setting it to `true` excludes attributes and setting it to `false` includes them.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
