# Bug Report

### Describe the bug

I'm encountering an issue with keyword parsing in MDX code blocks. It seems like JavaScript keywords (like `const`, `let`, `function`, etc.) are not being recognized correctly and are being treated as regular identifiers instead.

### Reproduction

When I try to use MDX with code that contains JavaScript keywords, they're not being tokenized properly:

```mdx
# Example

```js
const myVariable = 42;
let anotherVar = "test";
function myFunc() {
  return true;
}
```
```

The keywords `const`, `let`, and `function` should be recognized as keywords, but they're being treated as regular names/identifiers.

### Expected behavior

JavaScript keywords should be properly identified and tokenized as keywords, not as generic name tokens. This affects syntax highlighting and potentially other downstream processing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
