# Bug Report

### Describe the bug

I'm encountering an issue with module resolution in the esbuild configuration. When building the project, modules are not being resolved correctly, causing build failures or runtime errors.

The problem appears to be related to how paths are being resolved for certain dependencies like `vscode-*`, `estree-walker`, and `jsonc-parser`. The build process seems to be looking in the wrong directories for these modules.

### Reproduction

1. Set up a project that uses the insomnia-inso package
2. Include dependencies that match the pattern `vscode-.*`, `estree-walker`, or `jsonc-parser`
3. Run the build process
4. Observe that modules cannot be found or are resolved to incorrect paths

### Expected behavior

The build should correctly resolve module paths by:
- Using the correct resolve directory context
- Properly converting UMD paths to ESM paths (not converting ESM back to UMD)
- Successfully locating and bundling the required dependencies

### System Info
- Package: insomnia-inso
- Build tool: esbuild

---
Repository: /testbed
