# Bug Report

### Describe the bug

After a recent update, the sidebar items generator is receiving incorrect document properties. When using custom sidebar generators, the document objects passed to the generator function have changed - they now contain `permalink` and `sourceDir` properties instead of the expected `id` and `sourceDirName` properties.

### Reproduction

```js
module.exports = {
  docs: {
    sidebar: {
      generator: ({docs}) => {
        // This now fails - docs[0].id is undefined
        console.log(docs[0].id); // undefined
        console.log(docs[0].sourceDirName); // undefined
        
        // These properties exist instead
        console.log(docs[0].permalink); // '/docs/some-doc'
        console.log(docs[0].sourceDir); // 'some-dir'
        
        return docs.map(doc => ({
          type: 'doc',
          id: doc.id, // This breaks!
        }));
      }
    }
  }
}
```

### Expected behavior

The document objects passed to sidebar generators should include the `id` and `sourceDirName` properties as documented, allowing generators to reference documents by their IDs and organize them based on their source directory names.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is breaking existing custom sidebar generators that rely on these properties.

---
Repository: /testbed
