# Bug Report

### Describe the bug
After a recent update, MDX files are not being processed correctly. It seems like the format detection logic is broken - files with `.mdx` extension are being treated as markdown instead of MDX, which causes components and JSX syntax to not work properly.

### Reproduction
```js
// Create a file with .mdx extension
const file = {
  extname: '.mdx'
}

// Try to compile it
compile(file)

// Expected: Should be processed as MDX format
// Actual: Gets processed as markdown, JSX components don't render
```

### Expected behavior
Files with `.mdx` extension should automatically be detected and processed as MDX format, allowing JSX components to work. Files with `.md` extension should be processed as markdown.

### Additional context
This appears to have broken after the latest changes. The format detection seems to always default to "mdx" now regardless of the actual file extension or explicit format option passed in.

---
Repository: /testbed
