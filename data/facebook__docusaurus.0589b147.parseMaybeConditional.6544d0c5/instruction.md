# Bug Report

### Describe the bug

I'm encountering an issue with parsing conditional (ternary) expressions in MDX files. The parser seems to be incorrectly handling the operator precedence when parsing the test expression of a ternary operator, which causes unexpected parsing behavior.

### Reproduction

When trying to parse MDX content with nested or complex ternary expressions, the parser doesn't correctly handle the expression operators in the test position:

```js
// Example that triggers the issue
const result = a || b ? c : d;
```

The parser appears to be recursively calling the wrong parsing method for the test expression, which can lead to incorrect AST generation or parsing errors with certain operator combinations.

### Expected behavior

The parser should correctly handle operator precedence in ternary expressions. The test expression (before `?`) should be parsed with the appropriate precedence rules, and the alternate expression (after `:`) should also be parsed correctly without carrying over the `forInit` parameter.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to affect how complex expressions with logical operators and ternary operators are parsed together. Any insights would be appreciated!

---
Repository: /testbed
