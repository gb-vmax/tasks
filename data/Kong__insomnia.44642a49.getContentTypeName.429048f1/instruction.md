# Bug Report

### Describe the bug

The `getContentTypeName` function is returning incorrect content type names. When `useLong` is `true`, it returns the short name instead of the long name, and vice versa. This is causing display issues in the UI where content types are shown with the wrong format.

### Reproduction

```js
// When useLong is true, expecting long name but getting short name
const longName = getContentTypeName('application/json', true);
console.log(longName); // Returns 'JSON' instead of 'JavaScript Object Notation'

// When useLong is false, expecting short name but getting long name  
const shortName = getContentTypeName('application/json', false);
console.log(shortName); // Returns 'JavaScript Object Notation' instead of 'JSON'
```

### Expected behavior

- When `useLong` is `true`, the function should return the long/descriptive name of the content type
- When `useLong` is `false`, the function should return the short/abbreviated name of the content type

### System Info
- Insomnia version: latest
- OS: Windows 11

---
Repository: /testbed
