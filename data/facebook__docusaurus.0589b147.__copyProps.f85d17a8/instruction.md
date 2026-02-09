# Bug Report

### Describe the bug

I'm experiencing issues with object property copying/enumeration after a recent update. It seems like the logic for determining whether properties should be copied has changed, and now objects that should have their properties copied are being skipped entirely.

### Reproduction

```js
// When trying to copy properties from a plain object
const source = {
  prop1: 'value1',
  prop2: 'value2'
}

const target = {}

// Properties are not being copied as expected
// The condition seems to be checking if source is BOTH an object AND a function
// which will never be true, so the copy never happens
```

Additionally, there seems to be an issue with how enumerable properties are being determined. Properties that should be enumerable are not showing up correctly.

### Expected behavior

- Properties should be copied from source objects to target objects
- The enumerable flag should be set correctly based on the property descriptor
- Both plain objects and functions should have their properties copied when appropriate

### System Info

- Node version: Latest
- Browser: N/A (build-time issue)

This is blocking our build process as modules aren't being properly exported/imported.

---
Repository: /testbed
