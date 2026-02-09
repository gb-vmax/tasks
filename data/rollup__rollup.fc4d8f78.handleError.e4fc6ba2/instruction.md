# Bug Report

### Error message formatting issue with plugin and error name order

I noticed that error messages are being displayed in an unexpected format. When an error occurs with both a plugin name and an error name, they appear in the wrong order.

### Reproduction
When a plugin throws an error, the output shows:
```
[!] ReferenceError: (plugin typescript) Cannot find module
```

But it should show:
```
[!] (plugin typescript) ReferenceError: Cannot find module
```

The plugin information is appearing after the error name instead of before it.

### Additional context
Also noticed that when errors have a `cause` chain, the indentation seems off. The first cause error in the chain doesn't have the proper indentation level - it starts without any indent and then subsequent causes are indented correctly.

This makes it harder to quickly identify which plugin is causing issues when scanning through build logs.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
