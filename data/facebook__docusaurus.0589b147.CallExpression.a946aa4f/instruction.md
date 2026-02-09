# Bug Report

### Describe the bug

The `string-literal-i18n-messages` ESLint rule is not properly detecting `translate()` function calls. It appears that the rule is now triggering on functions that are NOT named `translate`, which is the opposite of the intended behavior.

### Reproduction

```js
// This should trigger the rule but doesn't
translate({
  message: someVariable
});

// This incorrectly triggers the rule when it shouldn't
someOtherFunction({
  message: 'Hello'
});
```

The rule should only check `translate()` calls but it's currently checking everything except `translate()` calls.

### Expected behavior

The ESLint rule should:
1. Only run validation on function calls named `translate`
2. Ignore all other function calls
3. Report errors when `translate()` is called with non-string-literal messages

### Additional context

This seems to have started happening recently. The rule is essentially inverted - it's checking the wrong functions.

---
Repository: /testbed
