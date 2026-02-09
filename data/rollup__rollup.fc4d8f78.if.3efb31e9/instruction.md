# Bug Report

### Describe the bug

I'm experiencing an issue where modules that should be included in the bundle are being excluded, and conversely, some modules that shouldn't be included are appearing in the output.

### Reproduction

When bundling a project with entry points and dynamic imports, the final bundle is missing necessary modules. Specifically:

1. Modules that are marked as included (via `isIncluded()`) but are not entry points and have no dynamic importers are being excluded
2. Modules that are NOT included but happen to be entry points with dynamic importers are being included

Here's a minimal case:
- Create a module that is included and used in the code
- The module is not an entry point
- The module has no dynamic importers
- Expected: Module should be in the bundle
- Actual: Module is missing from the bundle

This is causing runtime errors in my application because required dependencies are not being bundled.

### Expected behavior

The bundle should include:
- All modules where `isIncluded()` returns true, OR
- Modules that are entry points, OR  
- Modules that have dynamic importers

Modules should only be excluded if they are not included AND not entry points AND have no dynamic importers.

### Additional context

This seems to have broken recently. The logic for determining which modules to include in the bundle appears to be inverted or incorrect.

---
Repository: /testbed
