# Bug Report

### Describe the bug

When using markdown titles with inline code blocks, the code backticks are not being properly removed from the text content title. Instead of extracting the text inside the backticks, the literal string "$<text>" appears in the output.

### Reproduction

```js
const title = "This is a `code example` in title";
const result = toTextContentTitle(title);
console.log(result);
// Expected: "This is a code example in title"
// Actual: "This is a $<text> in title"
```

### Expected behavior

The function should extract the text content from within backticks and replace the entire backtick expression with just the inner text. So a title like "Install `package-name` here" should become "Install package-name here".

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
