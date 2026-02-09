# Bug Report

### Describe the bug

When a version fails to load in the docs plugin, the error is silently swallowed and the plugin continues execution instead of properly propagating the error. This makes it difficult to debug issues with version loading since the build doesn't fail and no clear indication is given that something went wrong.

### Reproduction

1. Set up a docs plugin with multiple versions
2. Introduce an error in one of the version's configuration or content (e.g., malformed markdown, invalid frontmatter, or broken references)
3. Run the build process
4. The build completes successfully instead of failing, but the problematic version is missing from the output

### Expected behavior

When a version fails to load, the build should fail with a clear error message indicating which version caused the problem and why. This would help developers quickly identify and fix configuration or content issues.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
