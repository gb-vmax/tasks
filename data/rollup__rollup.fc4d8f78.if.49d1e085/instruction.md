# Bug Report

### Describe the bug

When using the `-p` flag to specify multiple plugins separated by commas, only some of the plugins are being loaded. It seems like the first plugin in a comma-separated list is being skipped.

### Reproduction

```bash
# Try to load multiple plugins with comma separation
rollup -i input.js -o output.js -p node-resolve,commonjs,buble

# Only commonjs and buble are loaded, node-resolve is ignored
```

### Expected behavior

All three plugins (node-resolve, commonjs, and buble) should be loaded and applied to the build. The comma-separated plugin list should work as documented.

### Additional context

This also affects plugins with the `plugin=value` syntax. If you try something like:

```bash
rollup -i input.js -o output.js -p "plugin1=config,plugin2,plugin3"
```

The first plugin after splitting seems to be dropped. This is breaking our build pipeline that relies on passing multiple plugins via the command line.

---
Repository: /testbed
