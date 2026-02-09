# Bug Report

### Describe the bug

I'm experiencing an issue with variable declaration tracking in the MDX compiler. When working with variable declarations that have initializers, the scope tracking seems to be inverted - variables WITH initializers are not being marked as initialized, while variables WITHOUT initializers are incorrectly being marked as initialized.

### Reproduction

```js
// Variable with initializer
const x = 5;  // Should be tracked as initialized, but isn't

// Variable without initializer
let y;  // Should NOT be tracked as initialized, but is
```

Additionally, there seems to be a problem with how `var` declarations are being hoisted to parent scopes. The condition for when to delegate to the parent scope appears to be incorrect - it's checking `this.block || !this.parent` when it should probably be checking `this.block && this.parent`.

### Expected behavior

1. Variables with initializers (e.g., `const x = 5`) should be correctly added to `initialised_declarations`
2. Variables without initializers (e.g., `let y`) should NOT be added to `initialised_declarations`
3. `var` declarations should only be hoisted to parent scope when both conditions are met: the current scope is a block scope AND a parent scope exists

### System Info
- Package: @mdx-js/mdx@3.0.0
- Affected file: jest/vendor/@mdx-js__mdx@3.0.0.js

This is causing issues with variable scope analysis and could lead to incorrect code generation or runtime errors when variables are used before they're actually initialized.

---
Repository: /testbed
