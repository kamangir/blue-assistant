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
      Our objective is to write Python code to access the Orbital Data Explorer, ODE for short,
      using STAC terminology. For this purpose, we consider ODE as a catalog and each separate
      dataset in ODE as a collection that contains items.

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
        max_nodes: 2
      depends-on: web_crawl

    extraction:
      action: generate_text
      prompt: >
        :::context_prompt
        :::extraction_prompt
        :::url_content
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

  versions:
    downloading_a_datacube:
      vars:
        context_prompt: |
          We want to write Python code to download data from the Orbital Data Explorer, ODE
          for short, using STAC terminology.
      nodes: {}

```
[metadata.yaml](../metadata.yaml)

```bash
@select orbital-data-explorer-$(@@timestamp)

@assistant script run - \
    script=orbital_data_explorer,version=downloading_a_datacube .

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
      max_nodes: 2
      test_mode:
        max_nodes: 2
    extraction_001:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_pagehelp_Content_Web_Interface_User_Account_sign_in_htm.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To download data from the Orbital Data Explorer (ODE) using STAC terminology\
        \ via Python, you need to focus on accessing and retrieving data. While the\
        \ provided text is largely about signing into the ODE system, it doesn't contain\
        \ specific STAC-related information or API endpoints directly associated with\
        \ data retrieval.\n\nHowever, here\u2019s a general approach based on standard\
        \ practices for accessing datasets using STAC and APIs:\n\n1. **Authentication:**\
        \ First, authenticate the user using the login information. The text provides\
        \ instructions on signing into the ODE:\n\n    ```python\n    import requests\n\
        \n    # Assuming ODE provides an API for authentication\n    login_url = \"\
        https://ode-website.com/api/login\"  # Replace this with the actual URL\n\
        \    \n    payload = {\n        'email': 'your_email@example.com',\n     \
        \   'password': 'your_password'\n    }\n    \n    session = requests.Session()\n\
        \    response = session.post(login_url, data=payload)\n    \n    if response.ok:\n\
        \        print(\"Successfully signed in!\")\n    else:\n        print(\"Sign\
        \ in failed!\")\n    ```\n\n2. **Access STAC API:** Once signed in, navigate\
        \ to the STAC API endpoint for ODE to search and download data. You might\
        \ need to use specific URLs or endpoints that relate to STAC item searches.\n\
        \n    ```python\n    stac_search_url = \"https://ode-website.com/api/stac/search\"\
        \  # Replace this with the actual STAC search endpoint\n\n    # A generic\
        \ STAC search payload\n    headers = {\n        'Content-Type': 'application/json'\n\
        \    }\n    \n    search_payload = {\n        \"collections\": [\"collection-id\"\
        ],\n        \"bbox\": [-180.0, -90.0, 180.0, 90.0],\n        \"datetime\"\
        : \"2022-01-01T00:00:00Z/2023-01-01T00:00:00Z\",\n        \"limit\": 10\n\
        \    }\n    \n    search_response = session.post(stac_search_url, headers=headers,\
        \ json=search_payload)\n    \n    if search_response.ok:\n        items =\
        \ search_response.json()\n        print(\"Retrieved STAC items:\", items)\n\
        \    else:\n        print(\"Failed to retrieve items!\")\n    ```\n\n3. **Downloading\
        \ Data:** Iterate over the results and download the needed data assets:\n\n\
        \    ```python\n    for item in items.get('features', []):\n        for asset_key,\
        \ asset in item['assets'].items():\n            download_url = asset['href']\n\
        \            print(f\"Downloading asset from {download_url}\")\n         \
        \   asset_response = session.get(download_url)\n            \n           \
        \ if asset_response.ok:\n                with open(f\"assets/{asset_key}.dat\"\
        , 'wb') as f:\n                    f.write(asset_response.content)\n     \
        \           print(f\"Downloaded {asset_key} successfully!\")\n           \
        \ else:\n                print(f\"Failed to download {asset_key}\")\n    ```\n\
        \nPlease note that the actual API endpoints, collections, and authentication\
        \ mechanisms must be replaced with the real URLs and parameters used by the\
        \ ODE system. Always refer to the official ODE documentation for correct details."
      prompt: ':::context_prompt :::extraction_prompt Sign In Skip To Main Content
        Account Settings Logout placeholder Account Settings Logout Filter: All Files
        Submit Search Sign In Signing into ODE with a user account is simple. Click
        on the user icon, which will show as not signed in. It will display the following
        menu, which contains the sign in option. Click on the "Sign in" link. This
        displays the log in page. Enter your email address and password. Then click
        the "Sign in" button. After successful log in, a confirmation message will
        be displayed briefly. Then the page will redirect to the past page in use
        or the home page. If you forgot your password, click the " Forgot password
        " button. It will send you an email containing a link to follow to reset your
        password.

        '
      url: https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/sign_in.htm
    extraction_002:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_pagehelp_Content_Web_Interface_User_Account_user_access_links_htm.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "To achieve the objective of downloading data from the Orbital Data\
        \ Explorer (ODE) using STAC (SpatioTemporal Asset Catalog) terminology, the\
        \ following steps and considerations are relevant:\n\n1. **Logging In**: \n\
        \   - Users need to sign into ODE to access features such as bookmarks, history,\
        \ and cart orders, which are used to organize and retrieve data.\n   - Once\
        \ signed in, users can utilize the dropdown menu in the website banner to\
        \ navigate different sections of the ODE.\n\n2. **Accessing Data for Different\
        \ Targets**:\n   - ODE provides access to data for different planetary targets,\
        \ including Mars, Mercury, Lunar, and Venus. \n   - Users can switch between\
        \ these targets using a dropdown menu, which allows navigation to different\
        \ versions of the ODE website corresponding to each target.\n\n3. **STAC Terminology\
        \ Utilization**:\n   - Use the navigational elements provided (Bookmarks,\
        \ History, and Cart Orders) to organize and retrieve data in a way that aligns\
        \ with STAC practices. STAC typically involves organizing data as collections,\
        \ items with metadata, and assets that can be accessed or downloaded.\n\n\
        4. **Navigational Features**:\n   - Utilize the navigational menu on the left\
        \ side of the page to select specific actions like viewing Bookmarks, History,\
        \ and Cart Orders.\n   - These features might be used to manage datasets and\
        \ download relevant data, similar to using STAC catalogs, collections, and\
        \ assets.\n\n5. **Data Retrieval**:\n   - Follow the links provided in the\
        \ user interface to access lists of bookmarks, history, and cart orders. These\
        \ lists are essential for managing and retrieving data efficiently.\n   -\
        \ Extract data using these organizational tools, potentially by automated\
        \ scripts written in Python to interact with these elements via web requests\
        \ if APIs are available.\n\nIn summary, understanding and leveraging the account,\
        \ navigational features, and organization of data (using Bookmarks, History,\
        \ Cart Orders) in ODE will facilitate downloading data adhering to STAC terminology\
        \ and practices. If APIs are available, you can automate interactions and\
        \ data management using Python."
      prompt: ':::context_prompt :::extraction_prompt User Access Links Skip To Main
        Content Account Settings Logout placeholder Account Settings Logout Filter:
        All Files Submit Search User Access Links Once a user is signed into ODE,
        the logged in icon will display, as well as a dropdown menu in the website
        banner. This dropdown menu includes a greeting based on user email address,
        links to bookmarks, history, cart orders, sign out, and a link to this help.
        The links to bookmarks , history , and cart orders will navigate to the same
        shared page for accessing the listed resources. The page also allows users
        to navigate to the same page in different versions of ODE ( Mars , Mercury
        , Lunar , and Venus ). It is necessary to view the corresponding ODEtarget
        website to access associated bookmarks, history, and cart orders. The left
        side of the page includes the navigational menu for selecting the page to
        view ( Bookmarks , History , and Cart Orders ). Follow these links for further
        details on each page: Bookmarks list History list Cart orders list In addition,
        a dropdown menu allows users to navigate to the same options of the other
        ODE targets. This drop down menu will take the user to the corresponding ODE
        version. From there, the corresponding bookmarks, history, and cart orders
        can be viewed

        '
      url: https://ode.rsl.wustl.edu/mercury/pagehelp/Content/Web_Interface/User_Account/user_access_links.htm
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
    context_prompt: 'We want to write Python code to download data from the Orbital
      Data Explorer, ODE

      for short, using STAC terminology.

      '
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
  versions:
    downloading_a_datacube:
      nodes: {}
      vars:
        context_prompt: 'We want to write Python code to download data from the Orbital
          Data Explorer, ODE

          for short, using STAC terminology.

          '

```

</details>


![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-03-16-wryjqi/thumbnail-workflow.png?raw=true)

[orbital-data-explorer-2025-03-16-wryjqi](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-wryjqi.tar.gz)

🔥

---

- [round 1](./round-1.md)
