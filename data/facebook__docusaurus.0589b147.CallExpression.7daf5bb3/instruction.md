# Bug Report

### Describe the bug

The eslint rule `string-literal-i18n-messages` is incorrectly flagging valid `translate()` calls that use string literals for the `message` property. It appears the rule logic has been inverted - it now reports an error when a proper string literal is provided, which is the opposite of the intended behavior.

### Reproduction

```js
// This should be valid but triggers an error
translate({
  message: 'Hello world',
  id: 'greeting'
})

// This should trigger an error but doesn't
translate({
  message: `Template ${variable}`,
  id: 'dynamic'
})
```

### Expected behavior

The rule should:
- Allow string literals without template expressions
- Report errors when template strings with expressions are used
- Report errors when the message property is not a simple string

Currently it's doing the reverse - flagging valid string literals as errors.

### System Info
- Package: @docusaurus/eslint-plugin
- Node version: 18.x

---
Repository: /testbed
