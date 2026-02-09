# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where elements that should be passed through are being filtered out instead. It seems like the passThrough logic is inverted - nodes that are specified in the passThrough array are not being included in the output.

### Reproduction

```js
const mdx = `
# Hello

<CustomComponent />

Some text
`

const options = {
  passThrough: ['CustomComponent']
}

// CustomComponent should be passed through but it's being filtered out
const result = compile(mdx, options)
```

When I specify components in the `passThrough` option, they're not appearing in the compiled output. Instead, only components NOT in the passThrough array are being included, which is the opposite of what should happen.

### Expected behavior

Components listed in the `passThrough` array should be preserved in the output and passed through without transformation. Currently it seems to be doing the inverse - filtering out the components that are specified in passThrough.

### Additional context

This appears to have broken recently. The passThrough functionality used to work correctly but now behaves in reverse.

---
Repository: /testbed
