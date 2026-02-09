# Bug Report

### Describe the bug

I'm experiencing an issue with imported bindings where the wrong property is being used when collecting specifiers. It seems like the code is using `local` instead of `imported` when processing import declarations, which causes incorrect behavior when tracking dependencies.

### Reproduction

```js
// Given an import like:
import { foo as bar } from './module'

// The system should track 'foo' (the imported name from the module)
// But it's currently tracking 'bar' (the local name in the importing file)
```

This affects how dependencies are analyzed and can lead to:
- Incorrect tree-shaking decisions
- Missing imports in the generated bundle
- Wrong specifiers being collected for dependency tracking

### Expected behavior

When processing import declarations, the system should collect the `imported` property (the actual export name from the dependency) rather than the `local` property (the name used in the importing module).

For example, with `import { foo as bar } from './module'`:
- Expected: `foo` should be added to specifiers
- Actual: `bar` is being added instead

### Additional context

This appears to be affecting the `getImportedBindingsPerDependency` function and how it processes the `declaration.imports` array. The issue is particularly problematic when imports use aliases or when the local name differs from the exported name.

---
Repository: /testbed
