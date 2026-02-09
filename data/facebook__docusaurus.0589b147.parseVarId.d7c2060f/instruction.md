# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in MDX files. It appears that `var` declarations are being treated with the wrong binding scope, which causes unexpected behavior when parsing MDX content.

### Reproduction

When parsing MDX with variable declarations, `var` statements seem to be incorrectly scoped as lexical bindings instead of var bindings. This affects how variables are hoisted and scoped within the MDX content.

```js
// In an MDX file
export const MyComponent = () => {
  var x = 1;
  // var should have function scope, not block scope
  if (true) {
    var x = 2; // This should work but behaves incorrectly
  }
}
```

The parser is treating `var` declarations as if they have lexical (block) scope like `let` and `const`, when they should have function scope according to JavaScript semantics.

### Expected behavior

`var` declarations should be parsed with `BIND_VAR` binding type to maintain proper function-level scoping, while `let` and `const` should use `BIND_LEXICAL` for block-level scoping.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression from a recent change. The binding types appear to be swapped for var vs let/const declarations.

---
Repository: /testbed
