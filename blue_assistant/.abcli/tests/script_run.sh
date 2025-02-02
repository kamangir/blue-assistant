#! /usr/bin/env bash

function test_blue_assistant_script_run() {
    local options=$1

    abcli_eval ,$options \
        test_blue_assistant_script_run \
        ~upload,$options \
        $BLUE_ASSISTANT_TEST_OBJECT \
        "${@:2}"
}
