# Bug Report

### Describe the bug
When trying to use the `node:` prefix to load external configuration packages, the config path resolution fails. The CLI doesn't properly recognize the `node:` prefix format and fails to load the specified package.

### Reproduction
```bash
rollup --config node:my-config-package
```

The command fails to resolve the configuration package even when `rollup-config-my-config-package` or `my-config-package` is installed in node_modules.

### Expected behavior
The CLI should:
1. Recognize the `node:` prefix (5 characters)
2. Extract the package name correctly after the prefix
3. Attempt to resolve `rollup-config-{packageName}` first
4. Fall back to resolving `{packageName}` if the prefixed version doesn't exist
5. Show appropriate error message if neither package is found

### Additional context
This appears to have broken recently. Previously, using `--config node:package-name` worked correctly to load external configuration packages from node_modules.

---
Repository: /testbed
