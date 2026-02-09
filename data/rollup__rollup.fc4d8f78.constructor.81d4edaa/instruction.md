# Bug Report

### Plugin execution order is incorrect when using output plugins

I'm experiencing an issue where plugins are being executed in the wrong order when I have both input plugins and output plugins configured. It seems like output plugins are being run before input plugins, which is causing unexpected behavior in my build process.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm',
    plugins: [
      {
        name: 'output-plugin',
        renderStart() {
          console.log('Output plugin running');
        }
      }
    ]
  },
  plugins: [
    {
      name: 'input-plugin',
      buildStart() {
        console.log('Input plugin running');
      }
    }
  ]
};
```

Expected console output:
```
Input plugin running
Output plugin running
```

Actual behavior:
The order seems reversed - output plugins appear to be processed before input plugins in the internal plugin array. This is causing issues with plugins that depend on a specific execution order.

### Additional context

This wasn't an issue in previous versions. The plugin ordering seems to have changed recently, which is breaking my build pipeline that relies on input plugins running before output plugins.

---
Repository: /testbed
