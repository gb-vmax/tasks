# Bug Report

### Describe the bug

I'm experiencing an issue with HTML tag validation in Docusaurus. When passing certain values to the HTML tags API, the validation logic doesn't properly reject invalid inputs. Specifically, `null` values are being accepted when they should throw an error.

### Reproduction

```js
// This should throw an error but doesn't
const invalidTag = null;
// Expected to throw: "null is not a valid HTML tag object."
// But validation passes incorrectly
```

Also seeing issues with tag objects that have non-string tagName properties:

```js
const tagWithInvalidName = {
  tagName: 123  // Should be a string
};
// Expected to throw an error about invalid tagName
// But validation logic seems off
```

### Expected behavior

The validation should properly reject:
1. `null` values as invalid HTML tag objects
2. Tag objects where `tagName` is not a string type

The error messages should be thrown consistently for these invalid cases.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
