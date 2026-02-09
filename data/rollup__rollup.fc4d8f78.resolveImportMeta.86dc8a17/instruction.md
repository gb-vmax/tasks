# Bug Report

### Describe the bug

When using `import.meta.url` in a Rollup config file, it returns an incorrect value. Instead of getting the file URL, it seems to be returning something else entirely. This is breaking my build setup that relies on `import.meta.url` to resolve paths correctly.

### Reproduction

```js
// rollup.config.js
import path from 'path';

const __dirname = path.dirname(new URL(import.meta.url).pathname);

export default {
  input: path.join(__dirname, 'src/index.js'),
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  }
};
```

When I run this config, the path resolution fails because `import.meta.url` doesn't contain the expected file:// URL format.

### Expected behavior

`import.meta.url` should return a proper file URL (e.g., `file:///path/to/rollup.config.js`) so that it can be used with the `URL` constructor to get the directory path.

### System Info

- Rollup version: latest
- Node.js version: 18.x
- OS: Linux

---
Repository: /testbed
