# Bug Report

### Describe the bug

I'm encountering an issue with conditional expressions where the literal value inference seems to be inverted. When both branches of a ternary operator have the same literal value, the bundler is returning the actual value instead of an unknown truthy/falsy placeholder, and vice versa.

### Reproduction

```js
// Case 1: Both branches return the same value
const result1 = someCondition ? true : true;
// Expected: Should recognize both branches are identical and return the literal value
// Actual: Returns UnknownTruthyValue instead

// Case 2: Both branches return different values but cast to the same boolean
const result2 = someCondition ? 1 : "string";
// Expected: Should return UnknownTruthyValue since both cast to truthy
// Actual: Returns the literal value instead
```

The logic appears to be backwards - when the consequent and alternate values are the same, it's treating them as different, and when they're different, it's treating them as the same.

### Expected behavior

When both branches of a conditional expression have identical literal values, the bundler should return that literal value for optimization purposes. When they have different literal values but cast to the same boolean value, it should return the appropriate unknown truthy/falsy value.

### System Info
- Latest version from main branch

---
Repository: /testbed
