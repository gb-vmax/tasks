# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content rendering after a recent update. When using MDX files with layouts, the content doesn't render properly and the page appears broken or incomplete.

### Reproduction

```jsx
// Example MDX file with layout
export const meta = {
  title: 'My Page'
}

# Hello World

This is my content.
```

When this MDX file is processed, the resulting output seems truncated or malformed. The layout wrapper and content function generation appears to be incomplete.

### Expected behavior

The MDX file should compile correctly and render both the layout and content as expected. The generated JavaScript should include proper MDXContent and MDXLayout handling.

### System Info
- MDX version: 3.0.0
- Build tool: Jest/Webpack

Has anyone else encountered this? It seems like the compilation process is cutting off midway through generating the component structure.

---
Repository: /testbed
