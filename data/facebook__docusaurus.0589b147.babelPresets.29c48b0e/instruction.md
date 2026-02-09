# Bug Report

### Describe the bug

After a recent update, the Babel preset configuration seems to be applying the wrong transform options. The client-side build is now using server-side transformations and vice versa, which is causing issues with the build output.

### Reproduction

When building a Docusaurus project, the Babel transforms are being applied incorrectly:

1. Client-side code is being transformed with server-side settings
2. Server-side code is being transformed with client-side settings

This results in incorrect code generation for both environments. For example, client bundles may include server-only code that shouldn't be there, and server bundles may be missing necessary transformations.

### Expected behavior

The Babel preset should correctly identify whether it's running in a server or client context and apply the appropriate transformations:
- Server builds should use server-specific transforms
- Client builds should use client-specific transforms

### Additional context

This appears to have started happening recently. The build completes without errors, but the generated code is not correct for the target environment.

---
Repository: /testbed
