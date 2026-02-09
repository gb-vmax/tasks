# Bug Report

### Describe the bug

I'm encountering an error when trying to use the markdown serializer with the default quote option. The serializer is throwing an error saying it cannot serialize the title even though I'm using the default quote character.

### Reproduction

```js
const state = {
  options: {
    quote: '"'
  }
}

// This throws an error unexpectedly
checkQuote(state)
// Error: Cannot serialize title with `"` for `options.quote`, expected `"`, or `'`
```

The same thing happens when using single quotes:

```js
const state = {
  options: {
    quote: "'"
  }
}

checkQuote(state)
// Also throws the same error
```

### Expected behavior

The function should accept either `"` or `'` as valid quote options and return the marker without throwing an error. Both double quotes and single quotes are documented as valid options.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
