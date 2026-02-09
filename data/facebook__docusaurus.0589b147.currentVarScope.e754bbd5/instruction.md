# Bug Report

### Describe the bug

I'm encountering an issue where parsing certain MDX content causes the parser to crash with an error about trying to access properties of `undefined`. This appears to be happening during scope resolution when processing variable declarations.

### Reproduction

```js
// This MDX content triggers the issue
const mdxContent = `
export const config = { value: 'test' }

<Component prop={config.value} />
`

// Parser crashes when trying to process this
```

The error occurs when the parser tries to resolve variable scopes, specifically when accessing scope properties. It seems like the scope stack iteration is going out of bounds and trying to access an undefined element.

### Expected behavior

The MDX parser should correctly handle variable scope resolution without crashing, even for edge cases where the scope stack might be traversed completely.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to happen specifically when there are export declarations followed by JSX components that reference those exports. The parser should gracefully handle these cases instead of throwing errors.

---
Repository: /testbed
