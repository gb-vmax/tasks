# Bug Report

### Describe the bug

I'm experiencing an issue with scope tracking in the MDX analyzer. When parsing MDX expressions with nested scopes, the scope traversal seems to be getting confused and not properly maintaining the scope hierarchy.

### Reproduction

```js
// Example MDX with nested scopes
const mdxContent = `
export const Component = () => {
  const outer = 'test';
  
  return (
    <div>
      {(() => {
        const inner = 'nested';
        return <span>{outer} {inner}</span>;
      })()}
    </div>
  );
};
`;

// When analyzing this expression, the scope tracking
// doesn't correctly handle the nested function scope
```

### Expected behavior

The analyzer should correctly track scope entry and exit points, maintaining the proper parent-child relationship between nested scopes. Variables should be resolved to their correct containing scope.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have started happening recently. The scope parent tracking seems off when leaving nodes during AST traversal.

---
Repository: /testbed
