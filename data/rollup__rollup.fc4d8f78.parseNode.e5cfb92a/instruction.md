# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where the AST node parsing doesn't seem to be working correctly. After making some changes to my code, I noticed that import expressions are not being properly initialized and the parent class methods aren't being called during the parsing phase.

### Reproduction

```js
// Dynamic import in my code
const module = await import('./my-module.js');

// The import expression node doesn't get fully parsed
// and parent node initialization is skipped
```

When I use dynamic imports in my bundled code, the AST parsing appears incomplete. It seems like the node hierarchy isn't being set up properly during the parse phase.

### Expected behavior

Dynamic import expressions should be fully parsed with all parent class initialization methods being called correctly. The AST node should have its complete structure initialized including any properties set by parent classes.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
