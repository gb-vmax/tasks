# Bug Report

### Describe the bug

I'm experiencing a crash when parsing certain AST structures with node lists. The parser seems to be reading incorrect array lengths and iterating beyond the intended bounds, which causes unexpected behavior or crashes during AST conversion.

### Reproduction

```js
// This happens when converting buffer data to AST nodes
// The issue occurs with any AST structure that contains node lists

const ast = parseModule(code); // Crashes or produces malformed AST
```

The problem appears when the AST contains lists of nodes (like arrays of statements, parameters, etc.). The conversion process seems to read the wrong position for the length value and then iterates one extra time beyond what it should.

### Expected behavior

The AST should be parsed correctly without crashes, and node lists should contain the exact number of elements as specified in the buffer, with proper iteration bounds.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
