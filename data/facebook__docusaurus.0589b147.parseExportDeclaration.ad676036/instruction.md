# Bug Report

### Describe the bug

I'm experiencing an issue with MDX export declarations not being parsed correctly. When trying to use export statements in MDX files, the exports appear to be ignored or not processed properly.

### Reproduction

```mdx
export const metadata = {
  title: 'My Page',
  description: 'A test page'
}

export function MyComponent() {
  return <div>Hello</div>
}

# My Content

Regular MDX content here.
```

When this MDX is processed, the exported declarations seem to be missing or incomplete. The parser appears to return early without actually parsing the export statement.

### Expected behavior

Export declarations in MDX files should be fully parsed and available for use. Both named exports (like `metadata` and `MyComponent` above) should be properly extracted and usable.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

Has anyone else run into this? It seems like the export parsing logic might have regressed in the latest version.

---
Repository: /testbed
