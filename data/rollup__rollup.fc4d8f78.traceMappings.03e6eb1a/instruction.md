# Bug Report

### Describe the bug

I'm experiencing issues with sourcemap generation after a recent update. The build process appears to hang or fail silently when processing files with sourcemaps, particularly when dealing with files that have multiple transformation steps.

### Reproduction

```js
// Build configuration with sourcemaps enabled
const config = {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    sourcemap: true
  }
}

// When building a file that goes through multiple transformations
// with sourcemaps at each step, the build either hangs or produces
// incomplete output
```

### Expected behavior

The build should complete successfully and generate valid sourcemaps that correctly trace back to the original source files, even when there are multiple transformation layers.

### Additional context

This seems to happen specifically when there are nested sourcemaps that need to be collapsed/merged. The build process either:
1. Never completes (appears to hang)
2. Completes but produces invalid or incomplete sourcemaps

The issue is intermittent but happens more frequently with larger codebases that have many intermediate transformation steps.

---
Repository: /testbed
