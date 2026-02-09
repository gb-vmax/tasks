# Bug Report

### Describe the bug
When using `getUrl()` in plugin context, the returned URL has extra whitespace that wasn't there before. This breaks URL comparisons and causes issues with plugins that expect clean URL strings.

### Reproduction
```js
const request = context.request;
const url = request.getUrl();

// URL now has trailing/leading whitespace
console.log(url); // "https://example.com  " instead of "https://example.com"
console.log(url === "https://example.com"); // false when it should be true
```

### Expected behavior
`getUrl()` should return the URL without any extra whitespace, just like it did in previous versions. The URL string should be clean and ready to use for comparisons or string operations.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
