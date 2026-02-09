# Bug Report

### Describe the bug

The `replace` method in WalkerBase is not working correctly when the `prop` parameter is a falsy value like an empty string or `0`. Currently, the method checks `if (parent && prop)` which means it won't perform replacements when `prop` is a valid but falsy property name.

### Reproduction

```js
const walker = new WalkerBase();
const parent = {
  '': ['old-value'],
  '0': 'old-value'
};

// This replacement is silently ignored even though '' is a valid property
walker.replace(parent, '', 0, 'new-value');
console.log(parent[''][0]); // Still 'old-value', expected 'new-value'

// This replacement is also ignored even though '0' is a valid property
walker.replace(parent, '0', null, 'new-value');
console.log(parent['0']); // Still 'old-value', expected 'new-value'
```

### Expected behavior

The `replace` method should work with any valid property name, including falsy values like empty strings or numeric strings. The check should only verify that `parent` exists, not that `prop` is truthy.

### Additional context

This affects AST manipulation where property names might be empty strings or other falsy but valid values. The current implementation incorrectly treats these as invalid cases.

---
Repository: /testbed
