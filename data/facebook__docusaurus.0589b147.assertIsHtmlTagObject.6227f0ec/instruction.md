# Bug Report

### Describe the bug

When passing `null` as an HTML tag object, the validation function incorrectly accepts it as valid instead of throwing an error. This can lead to runtime errors later in the pipeline when the code tries to access properties on `null`.

### Reproduction

```js
// This should throw an error but doesn't
const tags = [null];

// When processing HTML tags, null values are not caught
// and cause issues downstream when trying to access tagName property
```

The validation should reject `null` values since they cannot be valid HTML tag objects, but currently they pass through the initial check.

### Expected behavior

The `assertIsHtmlTagObject` function should throw an error when `null` is passed, with a message like `"null" is not a valid HTML tag object.`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
