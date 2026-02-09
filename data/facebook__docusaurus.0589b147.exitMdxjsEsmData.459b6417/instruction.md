# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM data processing where the data handlers are being called in the wrong order. When parsing MDX files with ESM imports/exports, the exit handler is being invoked before the enter handler completes, which causes unexpected behavior in the token processing pipeline.

### Reproduction

```js
// MDX file with ESM syntax
export const foo = 'bar'

// When this gets processed, the exit handler runs before enter
// This breaks the expected token processing flow
```

The issue appears to be in the `exitMdxjsEsmData` function where the handlers are called in an incorrect sequence. The exit callback is being triggered before the enter callback finishes, which violates the expected enter/exit pattern for token processing.

### Expected behavior

The enter handler should complete its processing before the exit handler is called. This is the standard pattern for all other token types and ensures proper state management during parsing.

### System Info
- remark-mdx version: 3.0.0
- Parser: micromark-based

This seems like it could cause issues with any MDX files that use ESM syntax at the top level. Has anyone else run into this?

---
Repository: /testbed
