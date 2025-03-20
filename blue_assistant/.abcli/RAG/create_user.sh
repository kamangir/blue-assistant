#! /usr/bin/env bash

function blue_assistant_RAG_create_index() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local docs_object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $docs_object_name

    local index_object_name=$(abcli_clarify_object $3 $docs_object_name-index-$(abcli_string_timestamp))

    abcli_mlflow_tags_set \
        $index_object_name \
        contains=RAG-index,docs=$docs_object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_assistant.RAG.create_index \
        --docs_object_name $docs_object_name \
        --index_object_name $index_object_name \
        "${@:4}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $index_object_name

    return 0
}
