# Bug Report

### Describe the bug

I'm experiencing an issue with automatic semicolon insertion (ASI) in MDX parsing. When parsing certain code blocks, the parser seems to be checking for line breaks in the wrong part of the input string, which causes it to incorrectly determine whether a semicolon can be inserted.

### Reproduction

```js
// This MDX code fails to parse correctly
const example = `
export const test = {
  value: 1
}

function foo() {
  return 42
}
`
```

The parser appears to be slicing the input string with reversed indices when checking for line breaks between tokens. This leads to incorrect ASI behavior where semicolons should be automatically inserted but aren't, or vice versa.

### Expected behavior

The parser should correctly identify line breaks between the last token end and the current token start to properly determine when semicolons can be automatically inserted according to JavaScript ASI rules.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
