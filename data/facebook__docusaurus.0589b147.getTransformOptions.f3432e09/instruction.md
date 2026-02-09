# Bug Report

### Describe the bug

I'm experiencing an issue with the Babel configuration in Docusaurus where the `compact` option is not being applied correctly for client-side builds. The code generated for the browser is not being compacted, resulting in unnecessarily large bundle sizes with extra whitespace and newlines.

### Reproduction

1. Create a new Docusaurus project or use an existing one
2. Build the project for production
3. Inspect the generated JavaScript bundles in the `build` directory
4. Notice that the client-side bundles contain unnecessary whitespace and newlines

The server-side code appears to be compacted correctly, but the client bundles are not.

### Expected behavior

Both server and client builds should have the `compact` option enabled to omit all optional newlines and whitespace when generating code. This should result in smaller bundle sizes for production builds.

### System Info
- Docusaurus version: Latest
- Node version: 18.x
- Build target: Production

---
Repository: /testbed
