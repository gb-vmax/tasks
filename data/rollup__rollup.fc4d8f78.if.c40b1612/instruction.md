# Bug Report

### Describe the bug

When passing plugins via the command line with inline code or key-value syntax (like `-p plugin=value` or `-p "{transform(c,i){...}}"`), the plugins are not being loaded correctly. Additionally, when using comma-separated plugin names (e.g., `-p node-resolve,commonjs,buble`), the first plugin in the list is being skipped.

### Reproduction

```bash
# This doesn't work - plugin with = syntax not loaded
rollup input.js -p plugin=value

# This doesn't work - inline plugin code not loaded  
rollup input.js -p "{transform(code){return code;}}"

# This partially works but skips the first plugin
rollup input.js -p node-resolve,commonjs,buble
# Only commonjs and buble are loaded, node-resolve is skipped
```

### Expected behavior

- Plugins with `=` syntax (e.g., `plugin=value`) should be loaded properly
- Inline plugin code with `{}` should be executed
- When using comma-separated plugin names, ALL plugins should be loaded including the first one

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
