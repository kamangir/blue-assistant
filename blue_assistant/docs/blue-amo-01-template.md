# blue-amo 1

yaml:::get:::object_name:::script

```bash
@select blue-amo-$(@@timestamp)
@assistant script run - script=blue_amo .

@assets publish push .

@assistant build_README
```

set:::object_name blue-amo-2025-02-03-seaz7v

yaml:::get:::object_name:::output

assets:::get:::object_name/thumbnail-workflow.png