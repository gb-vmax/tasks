# Bug Report

### Describe the bug

I'm experiencing an issue with contextual keyword parsing in MDX. It seems like certain contextual keywords are being incorrectly recognized or not recognized at all, leading to parsing failures or unexpected behavior.

### Reproduction

```js
// Using MDX with contextual keywords
const mdxContent = `
export const meta = {
  title: 'Test'
}

Some content here
`

// The parser fails to correctly identify contextual keywords
// when escape sequences are present or when comparing values
```

When parsing MDX content that contains contextual keywords (like `export`, `import`, etc.), the parser doesn't properly validate whether a token is actually a contextual keyword. This causes issues where:
1. Valid contextual keywords are rejected
2. Invalid tokens are incorrectly accepted as contextual keywords

### Expected behavior

The parser should correctly identify contextual keywords by:
- Checking that the token type matches a name token
- Verifying the value matches the expected keyword
- Properly handling escape sequences in the token

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
