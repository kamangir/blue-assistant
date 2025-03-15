# Blue Script

```yaml
script:
    vars:
        story: |
            Write a story about ...

    nodes:
        story:
            runnable: false
            completed: true
            action: generate_text
            prompt: >
                :::context
                :::story

        image:
            action: generate_image
            depends-on: story
            prompt: Generate an image to visualize :::story

```

```bash
```bash
@assistant \
	build_README \
	[push]
 . build @assistant/README.md.
@assistant \
	pypi \
	browse \
	[token]
 . browse pypi/@assistant.
@assistant \
	pypi \
	build \
	[browse,install,~rm_dist,~upload]
 . build pypi/@assistant.
@pypi \
	install
 . install pypi.
@assistant \
	pylint \
	[ignore=<ignore>] \
	[<args>]
 . pylint @assistant.
@assistant \
	pytest \
	[list,dryrun,~log,show_warning,~verbose] \
	[filename.py|filename.py::test]
 . pytest @assistant.
@assistant \
	test \
	[what=all|<test-name>,dryrun] \
	[dryrun]
 . test @assistant.
@assistant \
	test \
	list
 . list @assistant tests.
@assistant \
	browse \
	[actions|repo]
 . browse blue_assistant.
@hue \
	create_user \
	[dryrun] \
	[--bridge_ip <192.168.1.95>]
 . create a hue user.
@hue \
	list \
	[dryrun] \
	[--bridge_ip <192.168.1.95>] \
	[--username <Z8vk6ci5VBj-D1NpVuWNx2xxhCbwcMcCxSY8gcOI>] \
	[--verbose 1]
 . list hue lights.
@hue \
	set \
	[dryrun] \
	[--bridge_ip <192.168.1.95>] \
	[--username <Z8vk6ci5VBj-D1NpVuWNx2xxhCbwcMcCxSY8gcOI>] \
	[--light_id <light_id>] \
	[--hue <65535>] \
	[--saturation <254>] \
	[--verbose 1]
 . set hue lights.
@hue \
	test \
	[dryrun] \
	[--bridge_ip <192.168.1.95>] \
	[--username <Z8vk6ci5VBj-D1NpVuWNx2xxhCbwcMcCxSY8gcOI>] \
	[--light_id all | <light_id>] \
	[--interval <0.01>] \
	[--colormap <11>] \
	[--verbose 1]
 . test hue.
   colormap: https://docs.opencv.org/4.x/d3/d50/group__imgproc__colormap.html
@assistant \
	script \
	list \
	[--delim +] \
	[--log 0]
 . list scripts.
@assistant \
	script \
	run \
	[download,dryrun,~upload] \
	[script=<script>] \
	[-|<object-name>] \
	[--test_mode 1] \
	[--verbose 1]
 . run <object-name>.
   script: generic | blue_amo | hue | orbital_data_explorer
@web \
	crawl \
	[dryrun,~upload] \
	<url-1>+<url-2>+<url-3> \
	[-|<object-name>] \
	[--max_iterations <100000>]
 . crawl the urls.
@web \
	fetch \
	[dryrun,~upload] \
	<url> \
	[-|<object-name>]
 . fetch <url>.
```
```bash

---

[repository](./repository/)

