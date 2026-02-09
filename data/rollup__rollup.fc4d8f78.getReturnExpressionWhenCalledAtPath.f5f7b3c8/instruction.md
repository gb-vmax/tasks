# Bug Report

### Describe the bug

I'm encountering an issue with template literal method calls in my code. When calling methods on template literals (like `.trim()`, `.toLowerCase()`, etc.), the behavior seems incorrect and I'm getting unexpected results or errors.

### Reproduction

```js
const myTemplate = `  hello world  `;
const result = myTemplate.trim();
// Expected: "hello world"
// Actual: Unexpected behavior or error
```

Also happens with other string methods:

```js
const template = `HELLO`;
const lower = template.toLowerCase();
// Should work but doesn't behave as expected
```

### Expected behavior

Template literals should support standard string methods like `.trim()`, `.toLowerCase()`, `.toUpperCase()`, etc. and return the correct values just like regular strings do.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
