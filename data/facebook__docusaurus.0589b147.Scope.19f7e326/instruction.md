# Bug Report

### Describe the bug

I'm experiencing an issue where scope variables are being shared across different parser instances instead of being isolated per scope. This appears to be causing unexpected behavior when parsing multiple MDX files or when scopes are nested.

### Reproduction

```js
// Parse two separate MDX files or create nested scopes
const parser1 = new Parser();
parser1.enterScope(SCOPE_FLAGS);
parser1.scopeStack[0].lexical.push('variable1');

const parser2 = new Parser();
parser2.enterScope(SCOPE_FLAGS);
parser2.scopeStack[0].lexical.push('variable2');

// Expected: parser1's lexical array should only contain 'variable1'
// Actual: parser1's lexical array contains both 'variable1' and 'variable2'
console.log(parser1.scopeStack[0].lexical); // ['variable1', 'variable2']
```

### Expected behavior

Each scope instance should maintain its own separate `lexical` and `functions` arrays. Variables declared in one scope should not leak into other scopes or parser instances.

### Additional context

This seems to affect the `lexical` and `functions` properties of the Scope object. When multiple scopes are created, they appear to be sharing the same array references instead of having independent arrays.

---
Repository: /testbed
