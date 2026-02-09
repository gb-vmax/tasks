# Bug Report

### Describe the bug

I'm encountering a problem with MDX parsing where the parser seems to be returning incorrect scope information. When parsing MDX content with nested scopes (like functions inside components), the scope tracking appears to be broken and returns numeric values instead of scope objects.

### Reproduction

```js
const mdx = `
export function MyComponent() {
  function nested() {
    const x = 1;
  }
  return <div>test</div>
}
`

// Parse the MDX content
// The parser should track scopes correctly but returns wrong data
```

When the parser processes nested function declarations or block scopes, it seems to lose track of the actual scope context and returns unexpected values.

### Expected behavior

The parser should correctly track and return scope objects when processing nested declarations. Scope information is critical for properly handling variable declarations and exports in MDX files.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
