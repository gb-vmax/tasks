# Bug Report

### Describe the bug

The `evaluateSync` function is returning incorrect values - it seems to be returning `defaultValue` when the result is defined (not `undefined`) and returning the actual result only when it's `undefined`. This is completely backwards from what should happen.

### Reproduction

```js
const result = evaluateSync('1 + 1', {}, { defaultValue: 999 });
console.log(result); // Expected: 2, Actual: 999

const result2 = evaluateSync('undefined', {}, { defaultValue: 'fallback' });
console.log(result2); // Expected: 'fallback', Actual: undefined
```

The function appears to have the logic inverted - when a valid result exists, it returns the default value instead of the result, and when the result is undefined, it returns undefined instead of the default.

### Expected behavior

- When evaluation succeeds and returns a defined value, that value should be returned
- When evaluation results in `undefined` OR an error occurs with `throwOnError: false`, the `defaultValue` should be returned
- The `defaultValue` should only be used as a fallback, not as the primary return value

### Additional context

This is affecting any code that relies on `evaluateSync` with a `defaultValue` option. The current behavior makes the function essentially unusable since it always returns the wrong value.

---
Repository: /testbed
