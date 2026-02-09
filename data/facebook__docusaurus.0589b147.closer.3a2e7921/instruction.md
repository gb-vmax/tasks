# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where the exit callbacks are not being properly invoked. It seems like the logic for handling token closures has been reversed - when there's no additional callback (`and` is falsy), the function tries to call it anyway, and when there IS a callback, it's being called but the main exit function is being skipped.

### Reproduction

```js
// When compiling MDX content with nested components
const mdx = `
# Hello

<CustomComponent>
  <NestedComponent />
</CustomComponent>
`

// The compiler fails to properly close tokens
// Exit handlers are not called correctly
compile(mdx)
```

### Expected behavior

When processing tokens during MDX compilation:
- If there's an additional callback (`and`), both the callback AND the exit function should be called
- If there's no additional callback, only the exit function should be called
- Token stack should be properly maintained throughout compilation

### Current behavior

The exit logic appears inverted - callbacks are being called when they don't exist, and the exit function is being skipped when callbacks are present. This causes the token stack to become corrupted during compilation.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
