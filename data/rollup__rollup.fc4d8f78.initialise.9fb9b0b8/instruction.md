# Bug Report

### Describe the bug

When using JSX elements with custom import sources, the import source is not being added to the context correctly. The `importSource` is being read from `this.jsxMode` before it's actually set by `getRenderingMode()`, resulting in `undefined` being passed to `addImportSource()`.

### Reproduction

```jsx
// Configure rollup with JSX and custom importSource
export default {
  plugins: [
    jsx({
      jsxImportSource: '@custom/jsx-runtime'
    })
  ]
}

// Component file
const Component = () => {
  return <div>Hello</div>
}
```

### Expected behavior

The custom JSX import source should be properly registered and the appropriate imports should be added to the output bundle. Currently, the import source configuration is being ignored because it's read before being set.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
