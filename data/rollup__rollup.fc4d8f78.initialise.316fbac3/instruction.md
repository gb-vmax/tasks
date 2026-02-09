# Bug Report

### Describe the bug

I'm encountering an issue with tagged template expressions where the arguments passed to the tag function appear to be incorrect. It seems like the first expression in the template literal is being excluded from the arguments array.

### Reproduction

```js
function myTag(strings, ...values) {
  console.log('strings:', strings);
  console.log('values:', values);
  return values;
}

const a = 1;
const b = 2;
const c = 3;

const result = myTag`Value: ${a}, ${b}, ${c}`;
// Expected values: [1, 2, 3]
// Actual values: [2, 3] (first expression is missing)
```

### Expected behavior

All template literal expressions should be included in the arguments passed to the tag function. In the example above, all three values (1, 2, 3) should be available in the `values` array.

### Additional context

This appears to be a recent regression. Tagged template expressions were working correctly in previous versions. The first expression value is consistently being dropped from the arguments list.

---
Repository: /testbed
