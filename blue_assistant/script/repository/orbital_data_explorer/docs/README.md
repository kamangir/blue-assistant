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
      cache: extraction_cache/ode_rsl_wustl_edu_mars_pagehelp_Content_Web_Interface_User_Account_sign_in_htm.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve the objective of accessing the Orbital Data Explorer (ODE)
        using STAC terminology:


        1. **ODE as a Catalog**: Consider the entire ODE platform as a catalog.


        2. **Collections**: Treat each separate dataset in the ODE as a collection.
        These collections contain individual items.


        3. **Items**: Refer to the individual items within each collection as objects
        or datacubes.


        There are no specific steps in the provided text regarding interacting with
        ODE using STAC terminology. However, the text provides instructions for signing
        into the ODE:


        - Click the user icon to access the sign-in menu.

        - Click "Sign in" and fill in your email address and password.

        - Click the "Sign in" button.

        - In case of a forgotten password, a "Forgot password" option is available,
        which will send a password reset link to your email.


        This information is essential for gaining access to the ODE platform, where
        STAC terminology can then be applied to interact with datasets.'
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
      url: https://ode.rsl.wustl.edu/mars/pagehelp/Content/Web_Interface/User_Account/sign_in.htm
    extraction_002:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_productsearch.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To access the Orbital Data Explorer (ODE) using STAC terminology, consider
        the following relevant information:


        1. **Catalog**: ODE can be considered as the main catalog in the STAC framework.

        2. **Collections**: Each separate dataset within ODE is considered a collection.
        These collections encompass various datasets available in the ODE.

        3. **Items**: Within each collection, specific items are referred to as objects
        or datacubes.


        This setup aligns with the STAC structure where:

        - The catalog contains collections.

        - Each collection contains items (referred to as objects or datacubes in this
        context).'
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Product Search You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/productsearch
    extraction_003:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mars_tools.txt
      completed: true
      depends-on: expanding_the_extractions
      output: "Based on the information provided, the objective is to access the Orbital\
        \ Data Explorer (ODE) using STAC (SpatioTemporal Asset Catalog) terminology.\
        \ Here\u2019s the relevant information extracted:\n\n1. **Catalog**: ODE itself\
        \ is considered the catalog in this context.\n2. **Collections**: Each separate\
        \ dataset within ODE is considered a collection.\n3. **Items**: The datasets\
        \ within each collection are referred to as items, which can be objects or\
        \ datacubes.\n\nNo additional specific details about how to implement this\
        \ was provided in the text."
      prompt: ':::context_prompt :::extraction_prompt Mars Orbital Data Explorer -
        Tools You are an anonymous user. Sign in Create a free account Read account
        help Your cart contents Your cart is empty. Show cart Home Data Product Search
        Map Search Tools Data Set Browser Download Help & Resources

        '
      url: https://ode.rsl.wustl.edu/mars/tools
    extraction_004:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To access the Orbital Data Explorer (ODE) using STAC terminology, consider
        the following information:


        1. **Catalog**: The entire ODE system is viewed as a catalog. In this case,
        ODE refers specifically to the Mercury Orbital Data Explorer.


        2. **Collections**: Within ODE, each dataset is treated as a collection. These
        collections correspond to the various datasets associated with the Mercury
        mission.


        3. **Items (Objects or Datacubes)**: Within each collection, the specific
        data products can be considered as items. These items could include various
        data files and datacubes that are part of the datasets within ODE.


        4. **Data Product Search**: Utilize the Data Product Search to locate specific
        orbital science products using parameters such as missions, instruments, data
        sets, time, location, and product IDs.


        5. **Data Set Browser**: Use the Data Set Browser to navigate through the
        available orbital data set files stored in the Planetary Data System (PDS)
        archives.


        6. **Download Cart**: Items or data products can be added to a download cart,
        from which they can be downloaded after search.


        This approach allows you to interact with and retrieve data from the Mercury
        Orbital Data Explorer using a structured and organized methodology consistent
        with STAC terminology.'
      prompt: ':::context_prompt :::extraction_prompt Mercury Orbital Data Explorer
        - Home Page You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Home Data Product
        Search Map Search Tools Data Set Browser Download Help & Resources Welcome
        to The Mercury Orbital Data Explorer The PDS Geosciences Node Mercury Orbital
        Data Explorer (ODE) provides search, display, and download tools for the PDS
        science data archives of the Messenger mission. Choose one of the above tabs
        to start using ODE. JavaScript must be enabled for the ODE website to function
        properly Browser Frames must be enabled for the ODE website to function properly
        Important Note: ODE has detected that JavaScript is not currently enabled
        in your browser. Please enable JavaScript to allow the website to function
        properly. Data Product Search Search for orbital science products across missions,
        instruments, and data sets via time, location, and product ids. What''s New
        See what''s new with ODE Additional Tools Product Type Coverage Help & Resources
        Access the ODE help, find additional resources, and see what''s coming Data
        Set Browser Browse through the orbital data set files stored in the PDS archives
        Available Data Sets A full list of mission, instrument, and product types
        available in Mercury ODE Download Cart Download products added to the cart
        from the product search Mars ODE Lunar ODE Mercury ODE Venus ODE The Mercury
        Orbital Data Explorer is produced by the PDS Geosciences Node at Washington
        University in St. Louis. Send comments and questions to ode@wunder.wustl.edu
        .

        '
      url: https://ode.rsl.wustl.edu/mercury/
    extraction_005:
      action: generate_text
      cache: extraction_cache/ode_rsl_wustl_edu_mercury_account_acctCreate_aspx.txt
      completed: true
      depends-on: expanding_the_extractions
      output: 'To achieve the objective of accessing the Orbital Data Explorer (ODE)
        using SpatioTemporal Asset Catalog (STAC) terminology, the relevant information
        extracted from the provided text is as follows:


        1. **ODE as a Catalog**: The Orbital Data Explorer can be considered the catalog
        in STAC terminology.


        2. **Collections**: Each separate dataset within ODE can be identified as
        a collection. These collections contain various data relevant to different
        space missions or agencies, such as those from PDS, ESA, and JAXA.


        3. **Items (Objects or Datacubes)**: The individual observations or sets of
        data within these collections are considered items. These are referred to
        as objects or datacubes.


        4. **Access**: You can access ODE data without any charge. However, creating
        a free account provides additional benefits like tracking search history,
        bookmarking searches and observations, and reviewing cart history.


        5. **Account Creation**: To create an account, users need a valid email address
        and a password that is 8 to 32 characters long. Supported password characters
        include letters, numbers, and a specified set of symbols.


        6. **Technical Requirements**: JavaScript must be enabled in your browser
        to use the ODE website effectively.


        7. **Contact for Assistance**: For issues or assistance with ODE, users can
        contact ode@wunder.wustl.edu.


        By organizing the ODE using these STAC-related terms, users can systematically
        access and interact with the data available in the Orbital Data Explorer.'
      prompt: ':::context_prompt :::extraction_prompt Mercury Orbital Data Explorer
        - Home Page {1} ##LOC[OK]## {1} ##LOC[OK]## ##LOC[Cancel]## {1} ##LOC[OK]##
        ##LOC[Cancel]## You are an anonymous user. Sign in Create a free account Read
        account help Your cart contents Your cart is empty. Show cart Welcome to the
        Orbital Data Explorer. All data are available at no charge. We offer a free
        login option, which allows users to track search history, bookmark searches
        and individual observations (PDS, ESA, and JAXA products), and review cart
        history. More information can be found in the ODE help. To report problems
        or request assistance, contact us at ode@wunder.wustl.edu Create Account Email
        address* Enter valid email address first. Password* Password must be 8 to
        32 characters long. You can use letters, numbers, and these symbols: ! @ #
        $ % ^ & * ? _ ~ - ( ) [ ] { } + = | ; : < > . / Remember my email address
        in this browser BotDetect CAPTCHA ASP.NET Form Validation Create account Important
        Note: ODE has detected that JavaScript is not currently enabled in your browser.
        Please enable JavaScript to allow the website to function properly.

        '
      url: https://ode.rsl.wustl.edu/mercury/account/acctCreate.aspx
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


![image](https://github.com/kamangir/assets/blob/main/orbital-data-explorer-2025-03-16-cajjx2/thumbnail-workflow.png?raw=true)

[orbital-data-explorer-2025-03-16-cajjx2](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-cajjx2.tar.gz)

🔥

---

- [round 1](./round-1.md)
