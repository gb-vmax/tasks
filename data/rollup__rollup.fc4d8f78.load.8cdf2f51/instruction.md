# Bug Report

### Describe the bug

I'm having an issue with the stdin plugin when using file extensions. When I try to read from stdin with a specific extension (e.g., `.js` or `.ts`), the content is not being loaded properly. It seems like the plugin is not recognizing stdin input when an extension suffix is provided.

### Reproduction

```js
// Using stdin with an extension
rollup --plugin stdin:.js

// Or programmatically:
{
  plugins: [stdinPlugin('js')]
}
```

When piping content to stdin with an extension specified, the input is not being processed. Without the extension it works fine, but as soon as I add one (like `.js`, `.ts`, etc.) the stdin content is ignored.

### Expected behavior

The stdin plugin should correctly load content from stdin regardless of whether an extension suffix is provided or not. Both of these should work:
- `echo "console.log('test')" | rollup --plugin stdin`
- `echo "console.log('test')" | rollup --plugin stdin:.js`

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
