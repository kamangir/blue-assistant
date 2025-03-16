# orbital-data-explorer 🔥

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/).

```yaml
script:
  vars:
    crawl_seeds:
      - https://ode.rsl.wustl.edu/
      - https://oderest.rsl.wustl.edu/
      - https://pds-geosciences.wustl.edu/dataserv/default.htm
      - https://github.com/samiriff/mars-ode-data-access

    context_prompt: |
      Our objective is to access the Orbital Data Explorer, ODE for short, using STAC 
      terminology. For this purpose, we consider ODE as a catalog and each separate dataset 
      in ODE as a collection that contains items. We call these items objects or datacubes.

    extraction_prompt: |
      Extract the information relevant to this objective from the following text.

    summarize_prompt: |
      Summarize the following information in the context of this objective.

  nodes:
    web_crawl:
      action: web_crawl
      max_iterations: 100
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 2

    expanding_the_extractions:
      action: expanding_the_extractions
      max_nodes: 10
      test_mode:
        max_nodes: 5
      depends-on: web_crawl

    extraction:
      runnable: false
      action: generate_text
      prompt: >
        :::context_prompt
        :::extraction_prompt
        :::page_content
      depends-on: expanding_the_extractions

    generating_summary:
      runnable: false
      action: generate_text
      prompt: >
        :::context_prompt
        :::summarize_prompt
      depends-on: extraction

    writing_code:
      runnable: false
      action: generate_text
      depends-on: generating_summary

```
[metadata.yaml](../metadata.yaml)

```bash
@select orbital-data-explorer-$(@@timestamp)

@assistant script run - \
    script=orbital_data_explorer .

@publish tar .

@assets publish extensions=png,push .
```



<details>
<summary>output</summary>

```yaml
script:
  nodes:
    expanding_the_extractions:
      action: expanding_the_extractions
      completed: true
      depends-on: web_crawl
      max_nodes: 5
      test_mode:
        max_nodes: 5
    extraction_001:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      prompt: ':::context_prompt :::extraction_prompt wip

        '
      runnable: false
    extraction_002:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      prompt: ':::context_prompt :::extraction_prompt wip

        '
      runnable: false
    extraction_003:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      prompt: ':::context_prompt :::extraction_prompt wip

        '
      runnable: false
    extraction_004:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      prompt: ':::context_prompt :::extraction_prompt wip

        '
      runnable: false
    extraction_005:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      prompt: ':::context_prompt :::extraction_prompt wip

        '
      runnable: false
    generating_summary:
      action: generate_text
      completed: true
      depends-on: extraction
      prompt: ':::context_prompt :::summarize_prompt

        '
      runnable: false
    web_crawl:
      action: web_crawl
      completed: true
      max_iterations: 2
      runnable: false
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 2
    writing_code:
      action: generate_text
      completed: true
      depends-on: generating_summary
      runnable: false
  vars:
    context_prompt: "Our objective is to access the Orbital Data Explorer, ODE for\
      \ short, using STAC \nterminology. For this purpose, we consider ODE as a catalog\
      \ and each separate dataset \nin ODE as a collection that contains items. We\
      \ call these items objects or datacubes.\n"
    crawl_seeds:
    - https://ode.rsl.wustl.edu/
    - https://oderest.rsl.wustl.edu/
    - https://pds-geosciences.wustl.edu/dataserv/default.htm
    - https://github.com/samiriff/mars-ode-data-access
    extraction_prompt: 'Extract the information relevant to this objective from the
      following text.

      '
    summarize_prompt: 'Summarize the following information in the context of this
      objective.

      '

```

</details>


![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-03-16-rvkrt6/thumbnail-workflow.png?raw=true)

[orbital-data-explorer-2025-03-16-rvkrt6](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-rvkrt6.tar.gz)

🔥

---

- [round 1](./round-1.md)
