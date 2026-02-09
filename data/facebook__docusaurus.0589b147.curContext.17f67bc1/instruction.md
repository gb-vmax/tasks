# Bug Report

### Describe the bug

I'm encountering an issue with JSX/MDX parsing where the parser seems to be returning incorrect context information. This appears to be affecting how braces are interpreted in certain nested structures.

### Reproduction

When parsing MDX content with nested JSX expressions, the context tracking seems off. For example:

```jsx
<Component>
  {items.map(item => (
    <div key={item.id}>
      {item.name}
    </div>
  ))}
</Component>
```

The parser appears to be looking at the wrong context level when determining whether braces should be treated as block statements or expressions. This causes parsing errors or unexpected behavior in nested JSX scenarios.

### Expected behavior

The parser should correctly track context depth and return the appropriate current context, allowing braces to be properly interpreted based on their actual nesting level.

### Additional context

This seems to affect MDX files with:
- Nested JSX expressions
- Arrow functions inside JSX
- Multiple levels of component nesting

The issue manifests as incorrect parsing behavior where the context lookup returns the wrong parent context.

---
Repository: /testbed
