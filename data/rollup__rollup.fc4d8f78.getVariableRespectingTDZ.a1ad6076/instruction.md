# Bug Report

### Describe the bug

I'm encountering an issue where identifiers in the Temporal Dead Zone (TDZ) are not being handled correctly. When referencing variables before their declaration in certain scopes, the bundler is not properly detecting potential TDZ violations and is treating them as unknown expressions when they should be treated as known variables, or vice versa.

### Reproduction

```js
// Example code that triggers the issue
function test() {
  console.log(x); // Should recognize TDZ violation
  let x = 5;
}

// Or with more complex scoping
{
  const y = z + 1; // Reference to z before declaration
  const z = 10;
}
```

The behavior seems inverted - cases that should be flagged as TDZ issues are being treated as safe, while safe references are being marked as problematic.

### Expected behavior

Variables referenced before their declaration should be properly identified as being in the TDZ and handled accordingly. The analysis should correctly determine when a reference is safe vs. when it's in a temporal dead zone.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
