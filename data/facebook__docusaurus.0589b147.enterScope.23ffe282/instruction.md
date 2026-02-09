# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where scope flags are not being properly preserved when entering a new scope. This causes incorrect parsing behavior for code blocks that rely on specific scope contexts (like function scopes, class scopes, etc.).

### Reproduction

When parsing MDX content that contains nested scopes, the parser seems to lose track of the scope flags. For example:

```mdx
export function MyComponent() {
  const [state, setState] = useState(0);
  
  return (
    <div>
      {state}
    </div>
  );
}
```

The parser appears to be creating scopes without the correct flags, which leads to unexpected parsing results for variable declarations and other scope-dependent syntax.

### Expected behavior

The scope stack should maintain the correct flags (like `SCOPE_FUNCTION`, `SCOPE_ASYNC`, etc.) when entering new scopes. This is critical for properly parsing JavaScript/JSX syntax within MDX files.

### Additional context

This seems to affect any MDX content with nested scopes - functions, classes, blocks, etc. The scope information is essential for the parser to correctly handle variable bindings and syntax validation.

---
Repository: /testbed
