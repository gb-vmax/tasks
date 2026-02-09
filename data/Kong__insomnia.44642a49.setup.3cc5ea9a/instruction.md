# Bug Report

### Describe the bug

After a recent update, the build process for `insomnia-inso` is failing to resolve module paths correctly. It seems like ESM modules are not being loaded properly, and the bundler is trying to load UMD versions instead (or vice versa).

### Reproduction

When building the project with esbuild, modules like `vscode-*`, `estree-walker`, or `jsonc-parser` are not being resolved to their correct paths. The build either fails or produces a bundle that doesn't work correctly at runtime.

Steps to reproduce:
1. Build the insomnia-inso package
2. The esbuild plugin that converts UMD to ESM paths appears to be applying transformations incorrectly
3. Module resolution fails or produces incorrect paths

### Expected behavior

The `umd2esm` plugin should correctly transform module paths from UMD to ESM format:
- Paths containing `/umd/` should be converted to `/esm/`
- Paths containing `\umd\` (Windows) should be converted to `\esm\`

The modules should resolve correctly and the build should complete successfully.

### System Info
- Package: insomnia-inso
- Build tool: esbuild

---
Repository: /testbed
