# Bug Report

### Describe the bug

I'm encountering an issue where MDX files with multiple export default declarations are not being properly validated. It seems like duplicate layout exports are being silently ignored instead of throwing an error as expected.

### Reproduction

```js
// example.mdx
export default function Layout1({ children }) {
  return <div className="layout1">{children}</div>
}

export default function Layout2({ children }) {
  return <div className="layout2">{children}</div>
}

# My Content

Some content here.
```

When processing this MDX file, I would expect an error about duplicate layouts, but instead it seems to process without any warnings or errors.

### Expected behavior

The compiler should fail with an error message like "Unexpected duplicate layout, expected a single layout" when encountering multiple `export default` declarations in an MDX file.

### Additional context

This appears to be a regression - I believe this validation was working correctly in previous versions. The duplicate export default should be caught and reported to help developers identify configuration issues in their MDX files.

---
Repository: /testbed
