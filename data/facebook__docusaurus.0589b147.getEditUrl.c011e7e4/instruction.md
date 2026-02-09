# Bug Report

### Describe the bug

When using `getEditUrl()` with file paths on Windows (containing backslashes), the function returns `undefined` instead of generating a proper edit URL. This breaks the "Edit this page" functionality on Windows systems.

### Reproduction

```js
const editUrl = 'https://github.com/user/repo/edit/main';
const fileRelativePath = 'docs\\intro.md'; // Windows path with backslashes

const result = getEditUrl(fileRelativePath, editUrl);
console.log(result); // undefined (expected: 'https://github.com/user/repo/edit/main/docs/intro.md')
```

### Expected behavior

The function should normalize Windows-style paths (with backslashes) to forward slashes and return a valid URL, regardless of the operating system.

### System Info
- OS: Windows 10
- Docusaurus version: latest

---
Repository: /testbed
