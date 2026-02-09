# Bug Report

### Describe the bug

I'm experiencing an issue with contextual keyword parsing in MDX. It seems like certain contextual keywords are being incorrectly identified, causing parsing errors or unexpected behavior when they contain escape sequences.

### Reproduction

```jsx
// This MDX content fails to parse correctly
const mdxContent = `
export const test = "value"

function Component() {
  return <div>test</div>
}
`
```

When processing MDX files with contextual keywords (like `export`, `import`, etc.) that may contain escape sequences, the parser doesn't handle them as expected. Keywords that should be recognized aren't being caught, or vice versa.

### Expected behavior

Contextual keywords should be properly identified regardless of whether they contain escape sequences. The parser should correctly distinguish between actual contextual keywords and regular identifiers.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
