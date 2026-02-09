# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX content that contains contextual keywords. When the parser encounters certain contextual identifiers (like `async`, `of`, `get`, `set`, etc.), it's throwing unexpected errors or behaving incorrectly.

### Reproduction

```js
// This MDX content fails to parse correctly
const mdxContent = `
export async function getData() {
  return { data: 'test' }
}
`

// Parser throws an error when it should accept the contextual keyword
```

The issue seems to occur specifically when contextual keywords are used in valid positions where they should be accepted as identifiers.

### Expected behavior

The parser should correctly handle contextual keywords in their appropriate contexts. When a contextual keyword appears where it's expected, parsing should succeed without errors.

### Additional context

This appears to have started happening recently. The parser seems to be rejecting valid MDX syntax that includes contextual keywords in positions where they should be allowed.

---
Repository: /testbed
