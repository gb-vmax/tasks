# Bug Report

### Describe the bug

The swizzle command is incorrectly treating components with `forbidden` action status as safe to swizzle. When attempting to swizzle a component that should be forbidden, the command allows it to proceed instead of blocking the action.

### Reproduction

```js
// Given a theme component with the following config:
const componentConfig = {
  actions: {
    wrap: 'forbidden',
    eject: 'safe'
  }
}

// Attempting to wrap this component is allowed when it should be blocked
// The isSafeAction check returns true for 'forbidden' actions
```

Steps to reproduce:
1. Configure a theme component with a `forbidden` action status
2. Try to swizzle that component using the forbidden action
3. The command proceeds without warning/error

### Expected behavior

Components with `forbidden` action status should not be treated as safe. Only actions explicitly marked as `safe` should pass the safety check. Actions marked as `forbidden` or `unsafe` should both fail the `isSafeAction()` validation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
