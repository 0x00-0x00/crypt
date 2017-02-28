#!/usr/bin/env perl
use Bytes::Random::Secure qw(
    random_bytes random_bytes_base64 random_bytes_hex
);

my $bytes = random_bytes_base64(32);
print $bytes;
