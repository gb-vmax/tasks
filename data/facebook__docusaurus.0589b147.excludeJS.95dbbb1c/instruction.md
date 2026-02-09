# Bug Report

### Describe the bug

After a recent update, the site fails to build with JavaScript parsing errors. The build process is throwing errors about unexpected tokens in what appears to be modern JavaScript syntax that should be getting transpiled.

### Reproduction

1. Set up a Docusaurus project with custom client-side code
2. Add some modern JS syntax (e.g., optional chaining, nullish coalescing) in the client directory
3. Run the build command
4. Build fails with syntax errors

The error messages indicate that JavaScript files aren't being transpiled properly, particularly files that should normally go through Babel transformation.

### Expected behavior

All JavaScript files in the client directory should be transpiled by Babel to ensure compatibility. The build should complete successfully without syntax errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently - builds were working fine before. It's affecting both development and production builds.

---
Repository: /testbed
