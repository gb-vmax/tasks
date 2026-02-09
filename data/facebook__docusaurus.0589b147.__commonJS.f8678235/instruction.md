# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module loading in the MDX vendor bundle. The CommonJS require wrapper seems to be returning the wrong value, which is causing modules to not load properly.

### Reproduction

When trying to use MDX components, the module exports are not being returned correctly. Instead of getting the module's exports object, something else is being returned from the require function.

This appears to be affecting the `__commonJS` helper function in the vendored MDX bundle. The issue manifests when:

1. A CommonJS module is required for the first time
2. The callback is executed to populate the module
3. The return value is incorrect

### Expected behavior

The `__commonJS` wrapper should return the `mod.exports` object after initializing the module, allowing proper access to the exported values from required modules.

### System Info
- MDX version: 3.0.0
- Jest vendor bundle

This seems like it might be a typo or logic error in the module loading code. The behavior changed recently and is breaking module resolution.

---
Repository: /testbed
