# Bug Report

### Describe the bug

When using HTML tag objects with uppercase tag names in the configuration, the validation is now incorrectly accepting them even though the tag name doesn't match the allowed list. This causes issues with HTML tag injection.

### Reproduction

```js
const htmlTag = {
  tagName: 'SCRIPT',
  attributes: {
    src: 'example.js'
  }
}

// This should throw an error but doesn't
// The validation passes even though 'SCRIPT' is not in the lowercase htmlTags list
```

### Expected behavior

The validation should reject HTML tag objects where the tagName uses uppercase letters, or it should properly validate against the allowed tags list regardless of case. Currently it seems like the validation logic has been changed and is not working as intended.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
