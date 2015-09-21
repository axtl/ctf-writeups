There are many different flows in the pcap which makes using the entire thing
in Wireshark pretty unpleasant. We start by splitting the main pcap into
individual files that each contain one flow. `pkt2flow` helps here.

There are still quite a few flows here, but as luck would have it, the most
obviously interesting one is at the first one (based on how `pkt2flow` names
the outputs. Either way, I ended up looking through all the flows, but most of
them were obviously TLS-encrypted or HSTS `301` redirects.

Using Wireshark to follow the TCP stream we see a Python script and some
encoded data at the end. Extract this information into a script. A little bit
of cleanup is needed at the end, but since we'll be writing a decoder, don't
bother cleaning this up just yet. Just put the encoded data in a global
constant or in a file (which is what I did; see script).

Reading through the encoder, it just randomly picks a number and uses that
as the index into a function array to choose an encoding function, then it
supplies the input to that function and stores the `index + 1` and the encoded
data back into the `tmp` variable; this repeats for a number of times, as
set by the `cnt` argument to the function. But this number isn't actually
relevant at all.

The encoded data contains everything we need. We add the relevant decoding
functions into a similar array, and write a `decode` function that:

1. splits the data into `encoding`, `content` where `encoding` is the previous
`index + 1` and content is everything else
2. using `index`, calls the appropriate decoding function
3. repeats until the decoded data starts with `flag{`

*Key*: `flag{li0ns_and_tig3rs_4nd_b34rs_0h_mi}`
