# Bug Report

### Describe the bug

The docs plugin seems to be swallowing errors during version loading. When there's an error loading a version, the error is caught but not re-thrown, which causes the build to continue silently instead of failing as expected.

### Reproduction

1. Set up a docs plugin with multiple versions
2. Introduce an error in one of the version configurations (e.g., invalid markdown, missing files, etc.)
3. Run the build
4. The build completes without throwing an error, even though version loading failed

### Expected behavior

When `loadVersion()` encounters an error while loading version metadata, it should:
1. Log the error message with the version name
2. Re-throw the error to stop the build process
3. Allow the error to propagate up so the build fails properly

Currently, errors are being caught but the function returns `undefined` instead of throwing, which causes downstream issues and makes debugging very difficult.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
