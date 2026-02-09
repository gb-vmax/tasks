# Bug Report

### Describe the bug

I'm encountering an issue with markdown rendering where certain inline constructs are being escaped incorrectly when they shouldn't be. It seems like the pattern matching logic for determining whether to escape characters based on context is not working as expected.

### Reproduction

```js
// When rendering markdown with nested constructs
const markdown = remark()
  .use(remarkStringify)
  .stringify(ast)

// Characters that should NOT be escaped in certain contexts
// are being escaped anyway, or vice versa
```

The problem appears to be related to how the library determines whether a pattern is "in scope" for a given construct. When I have nested markdown elements, the escaping behavior doesn't match what I'd expect based on the context.

### Expected behavior

The pattern matching should correctly identify when a construct is in scope by checking:
1. If the pattern IS in the allowed constructs (inConstruct)
2. AND the pattern is NOT in the disallowed constructs (notInConstruct)

Both conditions should be satisfied for the pattern to be considered in scope.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is causing issues with markdown output where special characters are either over-escaped or under-escaped depending on the nesting level of the constructs.

---
Repository: /testbed
