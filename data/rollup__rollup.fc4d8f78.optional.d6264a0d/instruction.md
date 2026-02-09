# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining detection in member expressions. When checking if a member expression uses optional chaining (the `?.` operator), the result is always incorrect - it returns `true` when it should be `false` and vice versa.

### Reproduction

```js
// Example 1: Non-optional member access
const expr1 = obj.property
// expr1.optional returns true (expected: false)

// Example 2: Optional chaining
const expr2 = obj?.property
// expr2.optional returns false (expected: true)
```

The `optional` property on `MemberExpression` nodes appears to be inverted - it's returning the opposite boolean value of what it should be.

### Expected behavior

- For regular member access (`obj.property`), the `optional` property should return `false`
- For optional chaining (`obj?.property`), the `optional` property should return `true`

### System Info
- Rollup version: latest
- Node version: 18.x

This is breaking any code that relies on detecting whether optional chaining is being used in member expressions.

---
Repository: /testbed
