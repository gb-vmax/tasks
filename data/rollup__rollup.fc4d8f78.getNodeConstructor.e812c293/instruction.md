# Bug Report

### Describe the bug

I'm experiencing an issue where node construction fails when there are leading or trailing whitespace characters in node type names. The system appears to be looking up node constructors using the raw name string without trimming whitespace first.

### Reproduction

```js
// This fails to get the correct node constructor
const nodeName = 'Identifier '; // note the trailing space
const constructor = getNodeConstructor(nodeName);

// Expected: IdentifierNode constructor
// Actual: Falls back to empty string key or undefined
```

When node type names have any whitespace padding, the lookup fails and falls back to an incorrect default constructor instead of finding the matching node type.

### Expected behavior

The node constructor lookup should handle whitespace in node type names gracefully and return the correct constructor. Either by trimming the input or by having a more robust lookup mechanism.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently, possibly after a change to how node types are resolved. It's causing issues in our build pipeline where node names might have inconsistent whitespace.

---
Repository: /testbed
