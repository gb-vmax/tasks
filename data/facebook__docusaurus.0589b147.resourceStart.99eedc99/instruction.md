# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where the resource marker token doesn't properly exit after being consumed. This appears to be causing the token stream to be malformed when processing markdown links with resources (like `[text](url)`).

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkStringify)

const input = '[link text](https://example.com)'
const result = processor.processSync(input)

// The AST shows an unclosed resourceMarker token
console.log(result)
```

### Expected behavior

The `resourceMarker` token should be properly closed with `effects.exit("resourceMarker")` after consuming the opening parenthesis character. The token stream should be well-formed with matching enter/exit calls for all tokens.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
