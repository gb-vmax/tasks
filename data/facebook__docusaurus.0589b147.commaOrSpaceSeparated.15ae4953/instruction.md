# Bug Report

### Describe the bug

The `commaOrSpaceSeparated` property type is not working correctly after a recent update. When trying to access or use properties that should be parsed as comma or space separated values, I'm getting errors about it not being a function.

### Reproduction

```js
// Attempting to use an attribute that relies on commaOrSpaceSeparated
const element = {
  className: 'foo bar, baz'
}

// The property handler should parse this correctly
// but throws "commaOrSpaceSeparated is not a function"
```

### Expected behavior

The `commaOrSpaceSeparated` property should be directly callable as a function to parse values that can be separated by either commas or spaces. It should return an array of the separated values.

### Additional context

This seems to have broken after some changes to how the property types are exported. The other property types like `boolean`, `booleanish`, etc. still work fine, but `commaOrSpaceSeparated` specifically is causing issues.

---
Repository: /testbed
