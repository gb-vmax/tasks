# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. It seems like the parser is incorrectly handling the binding context for `var` vs `let`/`const` declarations, which is causing validation errors or unexpected behavior when using certain variable patterns.

### Reproduction

```js
// In an MDX file
var { foo } = { foo: 'bar' }

// Or with const/let
const { baz } = { baz: 'qux' }
```

The parser appears to be applying the wrong binding type check for these declarations. Variables declared with `var` should be treated differently from block-scoped declarations (`let`/`const`) in terms of their binding validation.

### Expected behavior

The parser should correctly distinguish between `var` declarations (which should use `BIND_VAR`) and `let`/`const` declarations (which should use `BIND_LEXICAL`). Currently it seems like the logic is inverted.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
