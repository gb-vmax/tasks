# Bug Report

### Describe the bug

I'm experiencing an issue with webpack transpilation where JavaScript files in `node_modules` are not being processed correctly. It seems like the exclusion logic for determining which files should be transpiled has changed behavior.

After a recent update, my build is failing because certain modules that should be transpiled are being excluded, or vice versa. The webpack configuration appears to be treating files differently than before.

### Reproduction

The issue occurs during the webpack build process when:

1. Building a Docusaurus project with custom dependencies
2. Some npm packages in `node_modules` that contain JSX or modern JS syntax
3. The build either fails or produces unexpected output because files that should be transpiled are skipped

I noticed this affects specifically:
- Files within the client directory structure
- Docusaurus-related packages in node_modules
- Other libraries that need transpilation

### Expected behavior

The webpack configuration should:
- Always transpile files from the client directory
- Transpile Docusaurus packages found in node_modules
- Skip transpilation for other node_modules except those explicitly listed in `LibrariesToTranspile`

### System Info
- Docusaurus version: latest
- Node version: 18.x

The transpilation logic seems to have inverted or changed in a way that's causing incorrect file exclusions.

---
Repository: /testbed
