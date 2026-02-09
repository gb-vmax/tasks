# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where contextual keywords are not being validated correctly. When a required contextual keyword is present in the code, the parser throws an unexpected token error instead of continuing normally.

### Reproduction

```js
// Example MDX content that should parse successfully
export const meta = {
  title: 'Example'
}

# Hello World
```

When trying to parse MDX content with contextual keywords (like `export`, `import`, etc.), the parser fails even when the syntax is correct. It seems like the validation logic is inverted - it's throwing errors when it should accept the input and accepting when it should throw errors.

### Expected behavior

The parser should accept valid MDX syntax with contextual keywords and only throw errors when the expected keyword is actually missing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have broken after a recent change to the parser's contextual keyword handling. The behavior is backwards from what it should be.

---
Repository: /testbed
