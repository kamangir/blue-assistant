# blue-amo

Story development and visualization, with an [AI DAG](./metadata.yaml)

```yaml
include:::noref ./metadata.yaml
```

set:::object_name blue-amo-2025-02-03-nswnx6

metadata:::get:::object_name:::output.script.nodes.generating_the_story.output

```bash
@select blue-amo-$(@@timestamp)
@assistant script run - \
    script=blue_amo .

@assets publish push .

@assistant build_README
```

details:::output
metadata:::get:::object_name:::output.script.nodes
details:::

details:::workflow
assets:::get:::object_name/thumbnail-workflow.png
details:::

assets:::get:::object_name/stitching_the_frames-2.png

object:::get:::object_name

---

assets:::blue-amo-2025-02-04-nwb6nc/stitching_the_frames-2.png

assets:::test_blue_assistant_script_run-2025-03-15-06pbpf/stitching_the_frames-2.png

assets:::test_blue_assistant_script_run-2025-03-15-qe3c7o/stitching_the_frames-2.png