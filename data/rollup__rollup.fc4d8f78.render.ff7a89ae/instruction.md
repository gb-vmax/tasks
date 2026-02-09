# Bug Report

### Describe the bug

I'm encountering an issue with empty block statements being rendered incorrectly. When a block statement has no body (e.g., an empty `{}`), the closing brace appears to be getting removed or positioned incorrectly in the output code.

### Reproduction

```js
// Input code with empty block
function test() {
  if (condition) {}
}

// After bundling, the empty block is malformed
```

This seems to affect any empty block statement - empty if blocks, empty function bodies, empty try/catch blocks, etc. The closing brace position seems off.

### Expected behavior

Empty block statements should be preserved correctly in the output with both opening and closing braces intact at their proper positions.

### Additional context

This appears to be a rendering issue specifically with blocks that have zero statements in their body. Non-empty blocks seem to render fine.

---
Repository: /testbed
