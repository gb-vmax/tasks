# Bug Report

### Describe the bug

The ESLint rule `string-literal-i18n-messages` is incorrectly flagging valid `translate()` calls that use string literals for the `message` property. It seems like the validation logic is inverted - it's reporting errors when it should pass, and passing when it should report errors.

### Reproduction

```js
// This should be valid but gets flagged as an error
translate({
  message: 'Hello world',
  description: 'Greeting message'
})

// This should be flagged but passes without error
translate({
  message: `Hello ${user}`,
  description: 'Dynamic greeting'
})
```

The rule is supposed to enforce that the `message` property uses plain string literals without template expressions, but it's doing the opposite.

### Expected behavior

- `translate()` calls with plain string literals in the `message` property should pass validation
- `translate()` calls with template literals or expressions in the `message` property should be flagged as errors

### System Info
- ESLint plugin version: latest
- Node version: 18.x

---
Repository: /testbed
