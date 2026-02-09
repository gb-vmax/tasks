# Bug Report

### Describe the bug

When installing a plugin, the installation process gets stuck or fails to complete. The npm install command appears to hang indefinitely and never finishes. Looking at the logs, it seems like the warning classification logic is incomplete or broken.

### Reproduction

1. Try to install any plugin through the plugin manager
2. The installation starts but never completes
3. The process appears to hang during the npm install phase

```js
// Attempting to install a plugin
installPlugin('insomnia-plugin-example')
// Process hangs and never resolves
```

### Expected behavior

The plugin should install successfully and complete within a reasonable timeframe. The warning classification should properly handle npm warnings without causing the installation to hang.

### Additional context

This seems to have started happening recently. The installation worked fine before but now it just gets stuck. I've tried with multiple different plugins and they all exhibit the same behavior.

---
Repository: /testbed
