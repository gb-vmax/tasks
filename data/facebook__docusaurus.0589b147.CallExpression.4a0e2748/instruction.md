# Bug Report

### Describe the bug

The `string-literal-i18n-messages` ESLint rule is not triggering on `translate()` function calls as expected. It appears that the rule is now ignoring all `translate()` calls and not validating whether the message argument is a proper string literal.

### Reproduction

```js
// This should trigger the rule but doesn't
translate({
  message: `Hello ${name}`,
  id: 'greeting'
})

// This should also trigger but doesn't
translate('just a string')

// Even this doesn't get caught
translate()
```

All of these cases should be flagged by the linter, but they're passing through without any warnings or errors.

### Expected behavior

The rule should report an error when:
1. `translate()` is called without an object argument
2. `translate()` is called with a message that contains template expressions
3. `translate()` is called with invalid arguments

### Additional context

This seems to have broken recently. The rule was working correctly before and properly catching cases where `translate()` was being used incorrectly. Now it's not catching any violations at all.

---
Repository: /testbed
