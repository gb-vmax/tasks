# Bug Report

### Describe the bug

I'm experiencing an issue where the build process fails with a syntax error. It appears that the Chunk constructor is malformed or incomplete, causing the entire bundling process to crash.

### Reproduction

When attempting to bundle any project, the build fails immediately with a parse error. This happens regardless of the input configuration or modules being bundled.

Steps to reproduce:
1. Set up any rollup configuration
2. Attempt to build/bundle the project
3. The build crashes with a syntax error

### Expected behavior

The build should complete successfully and generate the expected output chunks.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to be a critical issue as it completely blocks the build process. Any help would be appreciated!

---
Repository: /testbed
