# blue-amo 1

set:::object_name blue-amo-2025-02-03-p33e2j

yaml:::get:::object_name:::script.nodes

```bash
@select blue-amo-$(@@timestamp)
@assistant script run - script=blue_amo .

@assets publish push .

@assistant build_README
```

yaml:::get:::object_name:::output.script.nodes

assets:::get:::object_name/thumbnail-workflow.png