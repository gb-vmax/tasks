# Bug Report

### Describe the bug

When using the markdown serializer, title quotes are not being handled correctly. It appears that titles are now being serialized with single quotes (`'`) by default instead of double quotes (`"`), and the validation logic seems inverted - it's throwing errors for valid quote characters instead of invalid ones.

### Reproduction

```js
const state = {
  options: {
    quote: '"'
  }
};

// This should work but throws an error
checkQuote(state);
// Error: Cannot serialize title with `"` for `options.quote`, expected `"`, or `'`
```

Also, when no quote option is specified:

```js
const state = {
  options: {}
};

// Default quote should be double quote but appears to be single quote
checkQuote(state);
```

### Expected behavior

- The default quote character should be `"` (double quote)
- Valid quote characters (`"` and `'`) should not throw errors
- Only invalid quote characters should trigger validation errors

### System Info
- remark version: 15.0.1

---
Repository: /testbed
