# Bug Report

### Describe the bug

The redirect plugin is throwing an error saying it's not supposed to override existing files, but it's actually throwing this error when the file **doesn't exist**. This is preventing any redirect files from being written at all.

### Reproduction

```js
// When trying to create a redirect file
const redirectFile = {
  fileAbsolutePath: '/path/to/new/redirect.html',
  fileContent: '<meta http-equiv="refresh" content="0; url=/new-path" />'
}

await writeRedirectFile(redirectFile)
// Error: The redirect plugin is not supposed to override existing files.
// But the file doesn't even exist yet!
```

### Expected behavior

The plugin should:
1. Check if a file already exists at the target path
2. If it exists, throw an error to prevent overriding
3. If it doesn't exist, write the redirect file normally

Currently it's doing the opposite - it only tries to write the file when it already exists, and throws an error when the path is empty.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

This is blocking all redirect functionality since no files can be created.

---
Repository: /testbed
