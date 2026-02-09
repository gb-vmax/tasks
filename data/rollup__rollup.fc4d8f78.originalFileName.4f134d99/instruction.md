# Bug Report

### Describe the bug

The deprecation warning message for `originalFileName` is showing the wrong information. When I access `originalFileName` on an emitted asset during file name generation, the warning says I'm accessing `originalFileNames` (plural) and tells me to use `originalFileName` instead - which is what I'm already using!

### Reproduction

```js
// In a plugin's generateBundle hook
export default {
  plugins: [{
    name: 'test-plugin',
    generateBundle(options, bundle) {
      this.emitFile({
        type: 'asset',
        name: 'test.txt',
        source: 'content',
        fileName: (assetInfo) => {
          // Accessing originalFileName here
          console.log(assetInfo.originalFileName);
          return 'output.txt';
        }
      });
    }
  }]
}
```

### Expected behavior

The deprecation warning should say:
- "Accessing the **originalFileName** property..." (not originalFileNames)
- "Use the **originalFileNames** property instead" (not originalFileName)

Currently it's backwards - the warning claims I'm accessing `originalFileNames` when I'm actually accessing `originalFileName`, and tells me to use `originalFileName` which doesn't make sense since that's what triggered the warning.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
