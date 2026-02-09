# Bug Report

### Describe the bug

When Docusaurus config validation encounters an error in a plugin or theme configuration, the error message path is being formatted incorrectly. String keys in the configuration path are being displayed with bracket notation instead of dot notation.

### Reproduction

Create a Docusaurus config with an invalid plugin configuration:

```js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        someInvalidOption: 'value'
      }
    ]
  ]
}
```

When validation fails, the error message shows something like:
```
Bad Docusaurus plugin value [someInvalidOption]
```

### Expected behavior

The error message should use dot notation for string keys:
```
Bad Docusaurus plugin value .someInvalidOption
```

This makes the error path more readable and consistent with standard JavaScript object notation. Bracket notation should only be used for numeric indices (array access).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
