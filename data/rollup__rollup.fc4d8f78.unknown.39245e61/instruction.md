# Bug Report

### Describe the bug

When passing `false` or `0` as an option value, it gets incorrectly treated as if no value was provided. The option normalization logic seems to be using a falsy check instead of properly checking for `null` or `undefined`, which causes valid falsy values to be ignored.

### Reproduction

```js
// Example 1: Using false as option value
const options = {
  someFlag: false
};

// The false value is treated as if no value was provided
// Expected: false should be preserved as a valid option value

// Example 2: Using 0 as option value  
const config = {
  count: 0
};

// The 0 value is also incorrectly ignored
// Expected: 0 should be preserved as a valid option value
```

### Expected behavior

Falsy values like `false`, `0`, and empty strings should be treated as valid option values. Only `null` and `undefined` should be treated as "no value provided".

### System Info

This appears to be affecting the option normalization/merging logic where falsy values are being filtered out unintentionally.

---
Repository: /testbed
