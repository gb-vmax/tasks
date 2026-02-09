# Bug Report

### Describe the bug

Client modules are not being loaded correctly - the paths are getting resolved in the wrong order. When plugins try to load their client modules, the resulting paths are incorrect and the modules can't be found.

### Reproduction

1. Create a plugin with client modules
2. Configure the plugin with `getClientModules()` returning relative paths
3. Try to load the client modules
4. The resolved paths will be incorrect (arguments are swapped in `path.resolve`)

For example, if a plugin at `/plugins/my-plugin` returns a client module path `lib/client.js`, the current code resolves it incorrectly.

### Expected behavior

Client module paths should be resolved correctly by combining the plugin path with the relative module path in the proper order. The modules should load without path resolution errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
