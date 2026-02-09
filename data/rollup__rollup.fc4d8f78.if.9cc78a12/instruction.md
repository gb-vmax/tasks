# Bug Report

### Describe the bug

I'm getting an error when trying to use `output.manualChunks` in my rollup configuration. The error message says the option is not supported, but I'm not using `inlineDynamicImports` at all - it's just set to the default value (false).

### Reproduction

```js
export default {
  input: 'src/main.js',
  output: {
    dir: 'dist',
    format: 'es',
    manualChunks: {
      vendor: ['react', 'react-dom']
    }
  }
}
```

When I run the build, I get an error saying that `output.manualChunks` is not supported, even though I'm not using `inlineDynamicImports`. 

### Expected behavior

The build should work fine when using `manualChunks` without `inlineDynamicImports`. The error should only be thrown when both options are used together, not when `inlineDynamicImports` is false or undefined.

### Additional context

This seems to have started happening recently. My configuration used to work without any issues. The error message is confusing because it suggests there's a conflict with `inlineDynamicImports`, but that option isn't even set in my config.

---
Repository: /testbed
