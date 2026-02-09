# Bug Report

### Describe the bug

I'm encountering an issue with scope handling in the MDX parser after a recent update. It appears that variable declarations are not being tracked correctly, which is causing parsing errors in certain MDX files.

### Reproduction

When parsing MDX content with variable declarations in nested scopes, the parser seems to be confusing variable scope tracking. Here's a minimal example:

```mdx
export const outer = 1;

function test() {
  const inner = 2;
  {
    var blockScoped = 3;
  }
}
```

The parser is not correctly distinguishing between `var` declarations and lexically scoped declarations (`let`/`const`), leading to incorrect scope resolution.

### Expected behavior

The parser should maintain separate tracking for:
- `var` declarations (function-scoped)
- Lexical declarations like `let`/`const` (block-scoped)
- Function declarations

Each scope should initialize with empty arrays for these different declaration types, and the `inClassFieldInit` flag should properly track whether we're inside a class field initializer (boolean value).

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after some recent changes to the scope initialization logic. The scope tracking is critical for proper variable resolution in MDX files.

---
Repository: /testbed
