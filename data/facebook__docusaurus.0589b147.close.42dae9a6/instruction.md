# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where certain closing tokens aren't being handled properly. It seems like the logic for handling optional callbacks during token closing has been inverted - callbacks that should be executed are being skipped, and the exit handler is being called without the token parameter.

### Reproduction

When compiling MDX content with nested elements that have closing callbacks, the compiler fails to properly invoke the callbacks and loses track of the token context.

```js
// MDX content with nested structure
const mdxContent = `
<CustomComponent>
  <NestedElement>
    Content here
  </NestedElement>
</CustomComponent>
`

// Compile with custom handlers
compile(mdxContent, {
  // handlers that expect callbacks on close
})
```

### Expected behavior

- When a closing token has an associated callback (`and` parameter), it should be executed
- The exit handler should receive the token parameter to maintain proper context
- Nested elements should close in the correct order with all callbacks firing

### Actual behavior

- Callbacks are only called when they don't exist (inverted logic)
- Token information is lost when calling the exit handler
- This breaks proper cleanup and context management during compilation

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
