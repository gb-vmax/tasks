# Bug Report

### Describe the bug

The `string-literal-i18n-messages` ESLint rule is reporting false positives when the `translate()` function is called with a valid object containing a `message` property that is a string literal.

### Reproduction

```js
// This should NOT trigger an error but currently does
translate({
  message: 'Hello world',
  description: 'Greeting message'
})

// This should trigger an error but currently does NOT
translate({
  description: 'Missing message property'
})
```

The rule seems to have inverted logic - it's flagging valid translate calls with proper string literal messages while ignoring calls that are actually missing the message property.

### Expected behavior

- `translate()` calls with a `message` property that contains a string literal should pass without errors
- `translate()` calls without a `message` property or with template literals/expressions should be flagged

### System Info
- eslint-plugin version: latest
- ESLint version: 8.x

---
Repository: /testbed
