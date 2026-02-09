# Bug Report

### Describe the bug

When trying to swizzle components, the safety check for swizzle actions is not working correctly. Components that should be marked as safe to swizzle are being rejected, and components that should be unsafe are being allowed through.

### Reproduction

```js
// Try to swizzle a component that has been marked as 'safe' in the theme config
// Expected: Should allow swizzling
// Actual: Swizzling is blocked

// Try to swizzle a component marked as 'unsafe'
// Expected: Should warn or block
// Actual: Swizzling is allowed
```

Steps to reproduce:
1. Set up a Docusaurus project with a theme that has swizzle configurations
2. Try to swizzle a component that's configured as 'safe' for a specific action
3. The swizzle operation fails even though it should be allowed
4. Try swizzling an 'unsafe' component and it goes through without proper warnings

### Expected behavior

The `isSafeAction` function should correctly identify when a component action is marked as 'safe' and allow swizzling. It should return `true` only when the action status is actually 'safe', not when it's 'unsafe' or other statuses.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken the entire swizzle safety mechanism. The logic for determining safe actions appears inverted or incorrect.

---
Repository: /testbed
