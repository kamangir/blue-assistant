#! /usr/bin/env bash

function test_blue_assistant_RAG_create_index() {
    local options=$1

    # TODO: enable
    return 0

    local docs_object_name=$RAG_DEFAULT_DOCUMENTS_OBJECT_NAME

    local index_object_name=test_blue_assistant_RAG_create_index-$(abcli_string_timestamp_short)

    blue_assistant_RAG create_index \
        ~upload,$options \
        $docs_object_name \
        $index_object_name
}
