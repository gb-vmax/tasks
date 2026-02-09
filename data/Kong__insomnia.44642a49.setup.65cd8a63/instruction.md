# Bug Report

### Describe the bug

The esbuild configuration for path resolution seems to have an issue with module path transformation. When building the project, modules that should be resolved from `/umd/` to `/esm/` directories are not being correctly transformed, which may cause module resolution failures or incorrect module loading.

### Reproduction

The issue appears to be in the `umd2esm` plugin configuration in `packages/insomnia-inso/esbuild.ts`. When the build process tries to resolve modules matching the pattern `vscode-.*`, `estree-walker`, or `jsonc-parser`, the path transformation doesn't work as expected.

For example:
1. A module path like `node_modules/some-package/umd/index.js` should be transformed to `node_modules/some-package/esm/index.js`
2. Instead, the path remains pointing to the `/umd/` directory

This affects both Unix-style paths (with `/`) and Windows-style paths (with `\`).

### Expected behavior

The plugin should correctly transform module paths from `/umd/` directories to `/esm/` directories for both Unix and Windows path formats, allowing proper ESM module resolution during the build process.

### System Info
- Package: insomnia-inso
- Build tool: esbuild

---
Repository: /testbed
