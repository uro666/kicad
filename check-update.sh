#!/bin/sh


curl -s "https://gitlab.com/kicad/code/kicad/-/tags" |grep "tags/" |sed -e 's,.*tags/,,;s,\".*,,;' |grep -E '' |grep -v '.*-rc.*$'|grep -v '7.99.0$'  |sort -V |tail -n1
