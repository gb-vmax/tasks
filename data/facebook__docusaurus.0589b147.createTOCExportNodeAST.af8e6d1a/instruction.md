# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation where the wrong AST creation function is being called for different TOC item types. When I have a document with both regular headings and sliced TOC items, the generated TOC structure appears to be swapped - headings are being processed as slices and slices are being processed as headings.

Additionally, it looks like the first TOC item is being skipped entirely from the exported TOC array.

### Reproduction

Create an MDX file with a mix of headings:

```md
# Main Title

## Section 1

### Subsection 1.1

## Section 2
```

When the TOC is generated, the item types don't match what they should be. For example, if you have a slice-type TOC item, it gets processed through the heading AST creator instead of the slice AST creator, and vice versa.

Also, the very first TOC item doesn't appear in the final TOC export at all.

### Expected behavior

- TOC items with `type: 'slice'` should be processed by `createTOCSliceAST()`
- TOC items with `type: 'heading'` should be processed by `createTOCHeadingAST()`
- All TOC items should be included in the exported array, including the first one

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
