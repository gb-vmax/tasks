# Bug Report

### Describe the bug

I'm encountering an issue with literal value handling in the code generator. When processing literal nodes, string values are not being properly serialized/escaped, which causes incorrect output.

### Reproduction

```js
const ast = {
  type: 'Literal',
  value: 'hello\nworld',
  raw: null,
  regex: null,
  bigint: null
}

// The generated output is:
// hello
// world

// But it should be:
// "hello\nworld"
```

When the `raw` property is `null` and we have a string value with special characters (like newlines, quotes, etc.), the output is not properly formatted as a string literal. The value is written directly without quotes or escaping.

### Expected behavior

String literals should be properly escaped and quoted in the generated output. For example:
- `"hello\nworld"` should output as `"hello\nworld"` (with quotes and escaped newline)
- `"test's"` should output as `"test's"` or `'test\'s'` (with proper escaping)
- Numbers and other primitives should also be properly stringified

### System Info
- Package: @mdx-js/mdx
- Version: 3.0.0

---
Repository: /testbed
