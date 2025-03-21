# RAG - round 3

## query pdf

[LangChain_QnA_RAG.ipynb](../../../notebooks/LangChain_QnA_RAG-3.ipynb)

Using [giza.pdf](https://kamangir-public.s3.ca-central-1.amazonaws.com/giza-v1/giza.pdf)

```bash
@RAG query_pdf \
	filename=giza \
	$(@mlflow tags search \
        contains=latest-giza \
        --log 0 \
        --count 1) \
	"What is the importance of Bash in AI? in less than 20 words."
```


```yaml
"Answer the following QUESTION based on the CONTEXT\n    given. If you do not know\
  \ the answer and the CONTEXT doesn't\n    contain the answer truthfully say \"I\
  \ don't know\"\n\n        CONTEXT:[Document(id='dc4c83ca-6544-4388-8ecb-3611da926068',\
  \ metadata={}, page_content='[17] Cloud Computing Services - Amazon Web Services\
  \ (AWS). awshttps://aws.amazon.com/ .\\n[18] UsetheDockercommandline-DockerDocs.\
  \ https://docs.docker.com/engine/reference/commandlin e/cli/.\\n[19] Amazon S3 -\
  \ Cloud Object Storage - AWS. https://aws.amazon.com/s3/ .\\n[20] Bash (unix shell)\
  \ - wikipedia. https://en.wikipedia.org/wiki/Bash_(Unix_shell) .\\n[21] Whatisashell?\
  \ (BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/ What-is-a-she\
  \ \\n[22] ShellExpansions(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Shell-Expan \\n[23] BraceExpansion(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Brace-Expan \\n[24] TildeExpansion(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Tilde-Expans'), Document(id='58242dd3-97ae-450c-b69a-df3014d55f57', metadata={},\
  \ page_content='[32] DirectoryStackBuiltins(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Direc \\n[33] nano - Text editor. https://www.nano-editor.org/ .\\n[34] argparse\
  \ \u2014 Parser for command-line options, arguments and s ub-commands \u2014 Python\
  \ 3.12.4\\ndocumentation. https://docs.python.org/3/library/argparse.html .\\n[35]\
  \ Click - The Pallets Projects. https://palletsprojects.com/p/click/ .\\n[36] Python\
  \ Fire. https://google.github.io/python-fire/ .\\n[37] Namespace-Wikipedia. https://en.wikipedia.org/wiki/Namespace#Emulating_n\
  \ amespaces .\\n[38] Aliases(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Aliases.html .\\n[39] Roy Thomas Fielding. Architectural Styles and the Design\
  \ of Network-based Softw are Architec-\\ntures. University of California, Irvine,\
  \ 2000.'), Document(id='94915c20-4ec8-4542-9454-bb027e8616ed', metadata={}, page_content='[25]\
  \ ShellParameterExpansion(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Sh \\n[26] CommandSubstitution(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Comman \\n8[27] ArithmeticExpansion(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Arithmet \\n[28] WordSplitting(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Word-Splittin \\n[29] BashStartupFiles(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Filename- \\n[30] ShellSyntax(BashReferenceManual). https://www.gnu.org/software/bash/manual/html_node/\
  \ Shell-Syntax.h \\n[31] De\uFB01nitions(BashReferenceManual): controloperator.\
  \ https://www.gnu.org/software/bash/manual/html_node/ D'), Document(id='38c7c9ff-b315-4d8a-aed6-b83e1699bff6',\
  \ metadata={}, page_content='machine(s) that carry them. Hence, the hypergraph is\
  \ a subset o f the state of the universal state\\nmachine. A command is a string\
  \ of characters that is meaningful to Bash[3]. Bash is a \u201CUnix shell Commands\\\
  n& Expan-\\nsionsand command language \uFB01rst released in 1989 that has been used\
  \ as t he default login shell for most\\nLinux distributions\u201D [ 20]. A shell\
  \ is a \u201Cmacro processor that executes commands\u201D [ 21], where \u201Cmacro\\\
  nprocessor means functionality where text and symbols are expand ed to create larger\
  \ expressions\u201D [ 21].\\nThere are seven kinds of expansions [22] in Bash. Expansions\\\
  nBrace Expansion [23] expands \u2018 a{d,c,b}e\u2019to \u2018ade ace abe \u2019\
  .Tilde Expansion [24] relates to words\\nthat begin with an unquoted tilde character\
  \ (\u02DC). Parameter and Variable Expansion [25] enable'), Document(id='4fe627f5-98d1-4c54-9928-009c7d0535d0',\
  \ metadata={}, page_content='propose expansions for Access and Automation in Sections\
  \ 2and3, respectively. We brie\uFB02y\\nreview a proposed view of Analytics as Access\
  \ to the outputs o f Automation in Section 4. Finally,\\nin Section 5, we review\
  \ a reference implementation of the proposed frame work [2] based on Bash[3]\\nexpansions\
  \ that call into Python[4] in multiple AI applications.\\nContents\\n1 Theoretical\
  \ Framework 1\\n2 Access 3\\n3 Automation 5\\n4 Analytics 5\\n5 AI 6\\n5.1 Vancouver\
  \ Watching ( vanwatch ). . . . . . . . . . . . . . . . . . . . . . . . . . . . .\
  \ . . 6\\n5.2palisades . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\
  \ . . . . . . . . . . . . . . . 8\\n1 Theoretical Framework\\nHypergraph\\nof Objects\\\
  n& Com-\\nmandsA group of operators maintain a growing space of commands in a set\
  \ of repositories , using a system'), Document(id='20a1febb-5405-4ceb-8149-e98d9ff63b1b',\
  \ metadata={}, page_content='that begin with an unquoted tilde character (\u02DC\
  ). Parameter and Variable Expansion [25] enable\\nthe use of variables, as ${variable\
  \ }, as well as more elaborate pattern matching forms such as${parameter/#pattern/string\
  \ }.Command Substitution \u201Callows the output of a command to re-\\nplace the\
  \ command itself\u201D [ 26].Arithmetic expansion [27] enables arithmetic operations\
  \ using the\\nform $(( expression )) andWord Splitting [28] governs the splitting\
  \ of the command to words.\\nFinally,Filename Expansion [29] enables the familiar\
  \ wildcard reference to \uFB01lenames using \u2018*\u2019 and \u2018?\u2019.\\nWe\
  \ are interested in a special category of valid bash commands [ 30] that start with\
  \ a specially\u2013crafted Command\\nSyntax callable, continue with a prescribed\
  \ sequence of identi\uFB01ers, and end with arguments. A callableis a'), Document(id='bbedb1d0-dd83-4b34-abfe-3e280ddbfc69',\
  \ metadata={}, page_content='algorithms [ 13,14]. State Ma-\\nchines A machine is\
  \ a state machine that is connected to many other m achines and sharessome of its\
  \ state\\nwith them for read and write. A shell is a stateful access mechanism to\
  \ a machine that an operator\\nuses to run commands. In a 2022 survey of developers,\
  \ 89% respo nded that they have a terminal open\\nat least half of the day [ 15].\
  \ Running a command in a shell can potentially modify the state of all\\nother machines.\
  \ Two examples of machines are a Raspberry Pi [ 16] that runs Linux and is connected\\\
  nto the AWS infrastructure [ 17] and a docker container [ 18] running in AWS Batch.\
  \ GNU Bash [ 3] is\\nan example of a shell.\\nThe operators act asynchronously while\
  \ communicating with each ot her. Multiple operators may'), Document(id='0d49c9dc-7201-4642-b259-5fb6fc8715fc',\
  \ metadata={}, page_content='https://github.com/kamangir/awesome-bash-cli .\\n[3]\
  \ Bash - GNU Project - Free Software Foundation. https://www.gnu.org/software/bash/\
  \ .\\n[4] Welcome to Python.org. https://www.python.org/ .\\n[5] Git - git Documentation.\
  \ https://git-scm.com/docs/git .\\n[6] Aboutpullrequests-GitHubDocs. https://docs.github.com/en/pull-requests/collaborat\
  \ ing-with-pull-req \\n[7] Machine Learning Service - Amazon SageMaker - AWS. https://aws.amazon.com/sagemaker/\
  \ .\\n[8] Alain Bretto. Hypergraph Theory; An Introduction . Springer, 2013.\\n[9]\
  \ E\uFB03cient Batch Computing - AWS Batch - AWS. https://aws.amazon.com/batch/\
  \ .\\n[10] B. Hendrickson and T.G. Kolda. Graph partitioning models for par allel\
  \ computing. Parallel\\nComputation , 26:1519\u20131545, 2000.'), Document(id='beed221c-f2b6-4e6d-8bb2-3d9f43d9db1b',\
  \ metadata={}, page_content='Access, Automation, Analytics, AI\\nArash Abadpour\
  \ - arash@abadpour.com\\nMarch 21, 2025\\n\u201C... the four A\u2019s that we\u2019\
  re after ... (1) Accessibility when I ask a quest ion I want to be able\\nto access\
  \ the data that allows me to answer the question that I\u2019m as king (2) Automation\\\
  nour ability to make routine tasks that are presently done by humans so that they\
  \ can be\\ndone by machines ... (3) Analytics we want to be able to generate insigh\
  \ ts that might not\\notherwise be obvious to us (4) AI ... - James C. Slife , The\
  \ Future of Warfare: Preparing\\nU.S. Military Forces for Competition and Contestation,\
  \ GSF 2024 [ 1].\u201D\\nAbstract\\nFirst, we develop a mathematical model to discuss\
  \ the \u201CFour A \u2019s\u201D in Section 1. Then, we\\npropose expansions for\
  \ Access and Automation in Sections 2and3, respectively. We brie\uFB02y'), Document(id='d68cc066-4a26-4811-9306-f53fc6f08d6f',\
  \ metadata={}, page_content='environment. For example, an itemin aSTAC collection\
  \ [41] (a datacube) or a dataset in Kaggle[42]\\nare objects. A curated dataset,\
  \ a model trained on it, and the mo del\u2019s predictions on a datacube, are\\\
  nexamples of other objects. Object\\nPointers An object may be selected,\\n@select\
  \ <object-name>\\nWhen<object-name> is selected, \u2018 .\u2019 expands to <object-name>\
  \ . Similarly, \u2018 ..\u2019, \u2018...\u2019, and so\\non, as deep as needed,\
  \ expand to the names of the previously selec ted object and the one before that.\\\
  nCommands default the objects they consume and modify to \u2018 .\u2019, \u2018\
  ..\u2019, and so on. Therefore, because\\nthe commands in a script generally use\
  \ the same objects, selecting t he objects enables their names to\\nbe replaced\
  \ with pointers. Often the defaults of the commands are designed to enable the omission\
  \ of')]\n        QUESTION:What is the importance of Bash in AI? in less than 20\
  \ words.\n        ANSWER:\n        \n        Bash is a crucial component in AI due\
  \ to its powerful command language and expansions that enable efficient automation\
  \ and integration of AI applications."

```

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
