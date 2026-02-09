# Bug Report

### Describe the bug

The redirect plugin is creating redirect files even when a file already exists at that path, which should be prevented. The security check that's supposed to prevent overriding existing files is not working correctly.

### Reproduction

```js
// Set up a redirect that points to a path where a file already exists
const redirects = [
  {
    from: '/old-page',
    to: '/new-page'
  }
];

// If a file already exists at the redirect target path, 
// the plugin should throw an error but instead it overwrites the file
```

Steps to reproduce:
1. Create a file at a specific path in your build output
2. Configure a redirect that would write to that same path
3. Run the build process
4. The existing file gets overwritten instead of throwing an error

### Expected behavior

The plugin should throw an error with the message "The redirect plugin is not supposed to override existing files." when trying to write a redirect file to a path where a file already exists. This is a security feature to prevent accidentally overwriting existing content.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
