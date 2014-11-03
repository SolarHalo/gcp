#!/bin/bash

if test -z "$GCP"
	then
	echo "\nnot GCP"
	GCP=..
	export GCP
else
	echo "GCP:$GCP"
fi
nohup $GCP/bin/executor.sh start &
