# Bug Report

### Describe the bug

I'm experiencing an issue where accessing nested properties in object literals seems to cause infinite recursion or stack overflow errors in certain cases. This appears to happen when the same property path is accessed multiple times during bundling.

### Reproduction

```js
const obj = {
  nested: {
    prop: {
      deep: 'value'
    }
  }
}

// Accessing the same nested path multiple times
console.log(obj.nested.prop.deep)
console.log(obj.nested.prop.deep)
```

When bundling code like this, the build process hangs or crashes with a stack overflow. It seems like the property inclusion logic is getting stuck in some kind of loop.

### Expected behavior

The bundler should handle repeated access to the same nested property paths without issues. The build should complete successfully and the output should include the necessary code only once.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This might be related to how property paths are being tracked during the inclusion phase. The issue wasn't present in earlier versions.

---
Repository: /testbed
