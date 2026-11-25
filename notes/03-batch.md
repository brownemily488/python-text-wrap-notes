# Ordered batch processing for Wrap prose

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
{
  "text": "small useful Python examples",
  "width": 12
}
```

Result:
```json
[
  "small useful",
  "Python",
  "examples"
]
```

## Case 2

Input:
```json
{
  "text": "https://example.com/long-path word",
  "width": 10
}
```

Result:
```json
[
  "https://example.com/long-path",
  "word"
]
```

## Case 3

Input:
```json
{
  "text": "",
  "width": 20
}
```

Result:
```json
[]
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

wrap returns lines within the chosen width. Disabling long-word splitting preserves URLs but can produce lines wider than the requested width.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
