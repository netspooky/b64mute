# b64mute - Base64 Mutator

This program applies simple mutations to base64 encoded strings for obfuscation purposes. It applies an uneven chunk approach to concatenate arbitrary chunks with padding.

For more info read [this writeup](https://n0.lol/encmute/)!

## Usage ##

Generate a mutation from a string

    $ python3 b64mute.py -d "netspooky"
    bmU=dHNwb28=a3k=

Generate a mutation on a file:

    $ python3 b64mute.py -f test.txt
    aA==dHQ=cHM6Ly90d2k=dHRlcg==Lg==Y28=bS8=bg==ZQ==dA==c3Bvb2t5

Save the output to a file:

    $ python3 b64mute.py -d "admin:hunter2" -o out.txt

Test your string:

    $ base64 -d <<< "bmU=dHNwb28=a3k="
    netspooky

