# Bug Report

### Describe the bug

I'm experiencing an issue with template literals in translation strings. When using template literals with expressions (e.g., `` `Hello ${name}` ``), they're being incorrectly treated as valid translation labels even though they contain dynamic content.

### Reproduction

```js
// This should NOT be valid but is being accepted
const translationKey = `user_${id}_profile`;

// This should also NOT be valid but passes validation
const message = `Hello ${userName}`;
```

Both of these template literals contain expressions and shouldn't be considered valid static translation labels, but the validation is passing them through.

### Expected behavior

Template literals with expressions should be rejected as invalid translation labels since they contain dynamic content. Only plain strings or template literals without any expressions should be accepted.

For example:
- `` `static_key` `` - should be valid ✓
- `"static_key"` - should be valid ✓  
- `` `dynamic_${var}` `` - should be invalid ✗
- `` `prefix_${id}_suffix` `` - should be invalid ✗

### Additional context

This seems to have started happening recently. The validation logic appears to be checking template literals but not properly filtering out ones that contain expressions.

---
Repository: /testbed
