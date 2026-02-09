# Bug Report

### Describe the bug

The `isIncluded` property on module info is returning incorrect values. When checking if a module is included during the build process, it's returning `null` during the GENERATE phase when it should be returning the actual inclusion status, and returning inverted boolean values during other phases.

### Reproduction

```js
// During plugin hooks
buildStart() {
  // Module info shows isIncluded as null during GENERATE phase
  const moduleInfo = this.getModuleInfo(moduleId);
  console.log(moduleInfo.isIncluded); // Expected: true/false, Actual: null
}

transform(code, id) {
  // Module info shows inverted isIncluded value
  const moduleInfo = this.getModuleInfo(id);
  console.log(moduleInfo.isIncluded); // Expected: true, Actual: false (or vice versa)
}
```

### Expected behavior

The `isIncluded` property should:
1. Return the correct boolean value indicating whether the module is included in the bundle
2. Not return `null` during the GENERATE phase
3. Not return inverted boolean values

### System Info

- Rollup version: latest
- Node version: 18.x

This is breaking plugins that rely on checking module inclusion status to make decisions about code transformation or asset generation.

---
Repository: /testbed
