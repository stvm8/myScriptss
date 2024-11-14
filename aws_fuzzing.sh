#!/bin/bash

i=0

for word in $(cat burp-parameter-names.txt); do
    cmd=$(aws lambda invoke --function-name CHANGE_ME --payload "{\"$word\":\"test\"}" --cli-binary-format raw-in-base64-out output);
    ((i=i+1))
    echo "Try $i: $word"
    if grep -q "Invalid event parameter" output;
    then
        rm output;
    else
        cat output; echo -e "\nFound parameter: $word" && break;
fi;
done
