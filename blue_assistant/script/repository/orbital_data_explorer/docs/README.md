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
      max_nodes: 100
      test_mode:
        max_nodes: 5
      depends-on: web_crawl

    extraction:
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
      output: 'To access the Orbital Data Explorer (ODE) using STAC (SpatioTemporal
        Asset Catalog) terminology, you need to conceptualize ODE as a STAC catalog.
        In this context:


        1. **Catalog**: ODE itself is considered the main catalog.

        2. **Collections**: Each separate dataset within ODE is considered a collection.
        These collections group related data and metadata, similar to how STAC collections
        work.

        3. **Items**: The individual objects or datacubes within each dataset are
        considered items. These items represent specific data entities and can include
        relevant metadata and links to the actual data.


        To effectively access and utilize ODE in this format, ensure that you map
        the datasets and objects in ODE into STAC collections and items, respectively,
        while adhering to STAC specifications for interoperability and data retrieval.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_002:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: "To achieve the objective of accessing the Orbital Data Explorer (ODE)\
        \ using STAC terminology, consider the following points:\n\n1. **ODE as a\
        \ Catalog**:\n   - Treat the entire Orbital Data Explorer as a STAC catalog.\
        \ This means ODE is the top-level container for all the data resources you're\
        \ aiming to access.\n\n2. **Datasets as Collections**:\n   - Each dataset\
        \ within the ODE should be considered as a separate STAC collection. A collection\
        \ is a group of related data, which in this case corresponds to each dataset\
        \ available in ODE.\n\n3. **Items as Objects/Datacubes**:\n   - The individual\
        \ items within each dataset/collection are referred to as objects or datacubes.\
        \ In STAC terms, these items encapsulate the specific data instances or files.\n\
        \nThese mappings from ODE concepts to STAC terminology will allow you to structure\
        \ your access and organization of data in terms that align with the STAC specification."
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_003:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve the objective of accessing the Orbital Data Explorer (ODE)
        using SpatioTemporal Asset Catalog (STAC) terminology, it''s important to
        understand the mapping between STAC concepts and the structure of ODE:


        1. **Catalog**: In STAC terminology, a catalog is the entry point that organizes
        datasets and provides metadata about them. In this context, the entire ODE
        is treated as a catalog.


        2. **Collection**: A collection in STAC is a group of related data items.
        Each separate dataset within ODE can be considered as a collection. These
        collections contain metadata that describes the dataset, including its spatial
        and temporal extent, data provider, and other relevant information.


        3. **Items**: Items are the individual records or data points within a collection.
        In the context of ODE, these are referred to as objects or datacubes. Each
        item contains metadata about the specific data object, including its properties,
        assets (e.g., data files), and geospatial and temporal information.


        By mapping ODE''s structure to STAC terminology, you can use standardized
        methods and tools designed for STAC to explore and access the datasets within
        ODE. This entails viewing the ODE as a catalog, with each dataset represented
        as a collection, and each data point within those datasets represented as
        an item (objects or datacubes).'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_004:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve your objective of accessing the Orbital Data Explorer (ODE)
        using STAC terminology, you need to understand the structure as outlined in
        your description:


        1. **Catalog**: ODE acts as a catalog, which is the top-level entry point
        in the STAC hierarchy. As a catalog, it organizes various datasets and collections.


        2. **Collections**: Each dataset within ODE is considered a collection. In
        STAC, a collection is a grouping of related data items, usually around a theme
        or topic. For ODE, this might mean different types of satellite data or data
        from different missions.


        3. **Items**: Within each collection, there are items. These items are referred
        to as objects or datacubes in your context. In STAC, items are the individual
        pieces of data that users can query.


        To proceed with your objective of accessing ODE using STAC, you should:


        - Identify the specific datasets in ODE that you want to treat as collections.

        - Understand the structure and metadata associated with each collection to
        effectively utilize STAC''s querying capabilities.

        - Develop or utilize existing tools that can communicate using STAC APIs to
        find and access the specific items or datacubes you need from the collections
        in ODE.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
    extraction_005:
      action: generate_text
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve your objective of accessing the Orbital Data Explorer (ODE)
        using STAC terminology, you can map the elements of ODE to the structure provided
        by the STAC specification as follows:


        1. **Catalog**: In the STAC model, a catalog is a container for storing metadata
        about datasets (collections) and their associated items. In your case, the
        entire ODE serves as this catalog.


        2. **Collections**: Each separate dataset within the ODE is considered a collection.
        A collection contains metadata about the dataset itself and can include one
        or more items.


        3. **Items**: Within each collection, there are individual elements known
        as items. In your framework, these items are referred to as objects or datacubes.
        Each item represents a specific piece of data or a discreet data unit within
        the dataset.


        Mapping ODE to STAC terminology allows you to structure the ODE data in a
        way that aligns with the STAC specification, facilitating easier access, discovery,
        and interoperability of geospatial data. By treating ODE as a STAC catalog
        composed of collections and items, you can efficiently explore and utilize
        the data available in ODE.'
      prompt: ':::context_prompt :::extraction_prompt wip

        '
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
      max_iterations: 5
      runnable: false
      seed_urls: :::crawl_seeds
      test_mode:
        max_iterations: 5
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


![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-03-16-bj8ghf/thumbnail-workflow.png?raw=true)

[orbital-data-explorer-2025-03-16-bj8ghf](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-bj8ghf.tar.gz)

🔥

---

- [round 1](./round-1.md)
