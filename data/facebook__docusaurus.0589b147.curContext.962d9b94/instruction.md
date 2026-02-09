# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing after a recent update. The parser seems to be accessing the wrong context when processing nested braces, leading to unexpected behavior or crashes.

### Reproduction

```jsx
const mdx = `
export const Component = () => {
  return (
    <div>
      {items.map(item => {
        return <span>{item.name}</span>
      })}
    </div>
  )
}
`

// Parsing this MDX content fails or produces incorrect results
```

The issue appears when there are nested braces/blocks in JSX expressions within MDX files. The parser doesn't correctly determine the context for brace handling.

### Expected behavior

The MDX parser should correctly handle nested braces in JSX expressions and properly determine whether a brace is starting a block or an object literal based on the current parsing context.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
