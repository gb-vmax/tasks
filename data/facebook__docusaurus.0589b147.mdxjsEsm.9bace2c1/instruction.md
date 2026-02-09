# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where `export` statements are not being recognized correctly. When I try to use export declarations in my MDX files, they don't seem to be processed properly and the parser appears to skip over them.

### Reproduction

```mdx
---
title: Test
---

export const metadata = {
  title: 'My Page'
}

export function MyComponent() {
  return <div>Hello</div>
}

# My Content

Some text here.
```

When processing this MDX file, the export statements are not being handled as expected. It seems like the parser is only recognizing `import` statements but ignoring `export` declarations.

### Expected behavior

Both `import` and `export` statements should be properly parsed and processed in MDX files. Export declarations should be treated the same way as import statements when tokenizing ESM code blocks.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
