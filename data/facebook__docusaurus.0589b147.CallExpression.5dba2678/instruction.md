# Bug Report

### Describe the bug

The `string-literal-i18n-messages` ESLint rule is incorrectly reporting errors for `translate()` calls that have a valid `message` property. It seems like the rule is now flagging valid translation calls as violations when they shouldn't be.

### Reproduction

```js
// This should be valid but gets flagged
translate({
  message: 'Hello world',
  description: 'Greeting message'
})

// This correctly gets flagged as expected
translate({
  description: 'Missing message property'
})
```

### Expected behavior

The rule should only report an error when the `message` property is missing or when it's not a string literal. Valid `translate()` calls with proper `message` properties should not trigger any warnings.

### Additional context

This seems to have started happening recently. The rule is now reporting false positives on code that was previously passing validation.

---
Repository: /testbed
