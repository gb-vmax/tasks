# Bug Report

### Incorrect variable selection in module re-exports

I'm experiencing an issue with re-exported modules where the wrong variable names are being used in the generated output. This seems to be affecting both default exports and namespace imports.

### Reproduction

When re-exporting from an external module with specific interop settings:

```js
// input module
export { default as foo } from 'external-package';
export * as bar from 'another-package';
```

The generated code uses incorrect variable references, causing runtime errors when trying to access the re-exported values.

### Expected behavior

The bundler should correctly resolve which variable to use based on the module's interop type and export mode. Default exports should use the appropriate helper variable when interop is needed, and namespace exports should use the correct variable depending on whether named exports mode is enabled.

### Additional context

This appears to be related to how the code determines which variable name to use when generating re-export statements. The logic for selecting between the default variable name and module variable name seems inverted, and similarly for namespace vs module variable selection.

The issue manifests at runtime when the generated bundle tries to access properties that don't exist on the selected variable.

---
Repository: /testbed
