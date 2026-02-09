# Bug Report

### Describe the bug

When using Date objects in front matter, they are not being properly converted to strings anymore. This causes validation issues when Date objects are provided as front matter values.

### Reproduction

```js
const frontMatter = {
  date: new Date('2024-01-15'),
  title: 'My Post'
}

// The date object is not being converted to a string
// This causes issues with validation/processing
```

### Expected behavior

Date objects in front matter should be automatically converted to strings, similar to how number values are handled. Previously this worked correctly, but now Date objects are passed through without conversion.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
