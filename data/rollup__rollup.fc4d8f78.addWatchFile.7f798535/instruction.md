# Bug Report

### Describe the bug

When using `addWatchFile` in transform hooks, the dependencies are not being tracked properly. Files added via `addWatchFile` during transformation are not triggering rebuilds when they change, even though they should be watched.

### Reproduction

```js
export default {
  name: 'my-plugin',
  transform(code, id) {
    const configFile = './my-config.json';
    
    // Add a file to watch
    this.addWatchFile(configFile);
    
    // Transform based on config
    const config = fs.readFileSync(configFile, 'utf-8');
    return transformWithConfig(code, config);
  }
}
```

Steps to reproduce:
1. Create a plugin that uses `addWatchFile` in the transform hook
2. Add a dependency file during transformation
3. Modify the watched file
4. The build doesn't retrigger even though the file was added to the watch list

### Expected behavior

When a file is added via `addWatchFile` during the transform phase, changes to that file should trigger a rebuild. The file should be properly tracked as a transform dependency.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression - it was working in earlier versions. The watched files are being registered but not actually tracked as dependencies for the transform step.

---
Repository: /testbed
