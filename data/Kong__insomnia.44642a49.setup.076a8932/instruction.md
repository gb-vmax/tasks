# Bug Report

### Describe the bug

After a recent update, the build is failing when trying to resolve module paths during the esbuild process. It seems like the module resolution for packages like `vscode-*`, `estree-walker`, and `jsonc-parser` is broken.

### Reproduction

When running the build, I'm getting errors related to module resolution. The build process can't find the correct ESM versions of certain dependencies.

Steps to reproduce:
1. Try to build the insomnia-inso package
2. The build fails during the module resolution phase
3. Error occurs when trying to resolve paths for vscode-related modules

### Expected behavior

The build should successfully resolve module paths by:
1. First resolving the actual UMD path using `require.resolve()`
2. Then transforming that resolved path to point to the ESM version
3. Returning the correct ESM path for bundling

### Additional context

This appears to be related to the `umd2esm` plugin in the esbuild configuration. The module resolution logic seems to be applying path transformations in the wrong order, trying to resolve a path that doesn't exist yet instead of resolving the actual module path first.

---
Repository: /testbed
