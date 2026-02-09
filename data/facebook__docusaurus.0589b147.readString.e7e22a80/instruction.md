# Bug Report

### Describe the bug

I'm encountering an issue with string parsing in MDX files where escape sequences in strings are not being handled correctly. When a string contains escaped characters (like `\n`, `\t`, or `\"`) the output is malformed.

### Reproduction

```js
const mdxContent = `
export const text = "Hello\\nWorld"
`

// After parsing, the string content is incorrect
// The escaped newline character is not in the right position
```

Another example:
```js
const str = "Test\\tstring"
// The tab escape sequence produces unexpected results
```

### Expected behavior

Escaped characters in strings should be properly parsed and positioned in the output string. For example, `"Hello\\nWorld"` should correctly produce a string with a newline character between "Hello" and "World".

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The escape sequences appear to be processed but the resulting string has characters in the wrong order or position.

---
Repository: /testbed
