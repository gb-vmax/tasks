# Bug Report

### Describe the bug

I'm experiencing an issue with plugin filters when using regular expressions. The filter behavior seems to be inverted - patterns that should match are being excluded, and patterns that shouldn't match are being included.

### Reproduction

```js
const filter = createFilter({
  include: /\.js$/
});

// This returns false when it should return true
filter('src/index.js');

// This returns true when it should return false  
filter('src/styles.css');
```

The same issue occurs when using regex patterns in exclude filters - they behave opposite to what's expected.

### Expected behavior

When a regex pattern is provided to a filter:
- Files matching the pattern should be included (for `include` option)
- Files matching the pattern should be excluded (for `exclude` option)

Currently the behavior is inverted for regex patterns. String patterns seem to work correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
